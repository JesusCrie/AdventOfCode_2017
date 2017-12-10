import re

from app.day import Day


class Program(object):

	def __init__(self, name: str, weight: int, childs: list):
		self.name = name
		self.weight = weight
		if childs is not None:
			self.childs = childs
		else:
			self.childs = list()

	def __str__(self):
		return self.name + " (" + str(self.weight) + ")"

	def __iter__(self):
		return self.childs.__iter__()

	def add_children(self, child: object):
		self.childs.append(child)

	def calculate_weight(self):
		return self.weight + sum(p.calculate_weight() for p in self)


class ProgramBuilder(object):

	def __init__(self, name: str, weight: int, childs: list = list()):
		self.name = name
		self.weight = weight
		self.childs_name = childs
		self.childs = list()

	def is_top(self):
		return len(self.childs_name) == 0

	def fill_child(self, child: Program):
		if child not in self.childs:
			self.childs.append(child)

	def auto_fill(self, child_dict: dict):
		for name in self.childs_name:
			res = child_dict.pop(name, None)
			if res is not None:
				self.childs.append(res)

	def is_complete(self):
		return len(self.childs) == len(self.childs_name)

	def complete(self):
		if not self.is_complete():
			raise RuntimeError("Not all childs are filled !")
		program = Program(self.name, self.weight, self.childs)

		return program


class ProgramStack:
	pattern = "(?P<name>[a-z]+) \((?P<weight>[0-9]+)\)(?: -> (?P<childs>(?:[a-z]+(?:, )?)+))?"

	def __init__(self):
		self.root = None
		self.top_stack = dict()  # {name, program}
		self.to_fill_stack = dict()  # {name, program builder}

	def proceed(self, raw_programs: list):
		self._parse(raw_programs)
		self._fill()
		self._finish()

	def _parse(self, raw_programs: list):
		for raw in raw_programs:
			builder = self._parse_and_prepare(raw)
			if builder.is_top():
				self.top_stack[builder.name] = builder.complete()
			else:
				self.to_fill_stack[builder.name] = builder

	def _fill(self):
		while len(self.to_fill_stack) > 0:
			for builder in tuple(self.to_fill_stack.values()):
				if len(self.to_fill_stack) == 1:
					return

				builder.auto_fill(self.top_stack)
				if builder.is_complete():
					self.top_stack[builder.name] = builder.complete()
					del self.to_fill_stack[builder.name]

	def _finish(self):
		k, self.root = self.to_fill_stack.popitem()
		self.root.auto_fill(self.top_stack)
		self.root = self.root.complete()
		del self.top_stack
		del self.to_fill_stack

	def _parse_and_prepare(self, raw: str):
		data = re.match(self.pattern, raw).groupdict()
		name = data["name"]
		weight = data["weight"]
		if data["childs"] is not None:
			raw_child = data["childs"].split(", ")
		else:
			raw_child = list()

		return ProgramBuilder(name, int(weight), raw_child)


class Day7(Day):

	def part_1(self):
		lines = self.input.splitlines()
		stack = ProgramStack()
		stack.proceed(lines)

		print(stack.root.name)

	def part_2(self):
		lines = self.input.splitlines()
		stack = ProgramStack()
		stack.proceed(lines)

		root = stack.root
		while len(root.childs) > 0:
			weights = {child: child.calculate_weight() for child in root}
			# TODO

	@staticmethod
	def get_alone_value(data: list):
		possible_values = [v for v in set(data) if data.count(v) == 1]
		if len(possible_values) == 0:
			return None
		else:
			return min(possible_values)
