import math
from abc import abstractmethod


class Day(object):

	def __init__(self, file: str = None, inp: str = None):
		if file is not None:
			self.input = open(file).read()
		elif inp is not None:
			self.input = inp
		else:
			self.input = str()

		self.to_int = lambda x_list: [int(x) for x in x_list]
		self.to_string = lambda x_list: [str(x) for x in x_list]

		print(">>> " + self.__class__.__name__ + " <<<")

	@abstractmethod
	def run(self):
		pass

	@staticmethod
	def ask_input():
		return input("Enter input:\n> ")


class Day1(Day):

	def run(self):
		print(sum(
			[int(char) for index, char in enumerate(self.input) if char == self.input[(index + 1) % len(self.input)]]))


class Day2(Day):

	def run(self):
		rows = [self.to_int(s.split("\t")) for s in self.input.splitlines()]
		print(sum([max(row) - min(row) for row in rows]))


class Day3(Day):

	def run(self):
		self.input = int(self.input)

		corner = self.get_grid_corner(self.input)
		size = int(math.sqrt(corner))
		top, right, bottom, left = self.get_grid_borders(corner)

		target_x = 0
		target_y = 0

		if self.input in top:
			target_x = top.index(self.input)
		elif self.input in bottom:
			target_x = bottom.index(self.input)
			target_y = size - 1
		elif self.input in left:
			target_y = left.index(self.input)
		elif self.input in right:
			target_y = right.index(self.input)
			target_x = size - 1

		zero = math.floor(size / 2)

		distance_x = int(math.fabs(target_x - zero))
		distance_y = int(math.fabs(target_y - zero))

		distance = distance_x + distance_y

		print("Corner: " + str(corner) + " (" + str(size) + ")")
		print("Target -> X: " + str(target_x) + ", Y: " + str(target_y))
		print(distance)

	@staticmethod
	def get_grid_corner(target: int):
		closest_square = math.ceil(math.sqrt(target))
		if closest_square % 2 == 0:
			closest_square += 1

		return int(closest_square) ** 2

	@staticmethod
	def get_grid_borders(corner: int):
		size = int(math.sqrt(corner))

		corner_left = corner - size + 1
		bottom = [c for c in range(corner_left, corner + 1)]

		corner_top = corner_left - size + 1
		left = [c for c in range(corner_top, corner_left + 1)]

		corner_right = corner_top - size + 1
		top = [c for c in range(corner_right, corner_top + 1)]
		top.reverse()

		corner_bottom = corner_right - size + 2
		right = [c for c in range(corner_bottom, corner_right + 1)]
		right.reverse()

		return top, right, bottom, left


class Day4(Day):

	def run(self):
		lines = [l.split() for l in self.input.splitlines()]
		print(len([l for l in lines if self.is_line_valid(l)]))

	@staticmethod
	def is_line_valid(line: list):
		return len(line) == len(set(line))


class Day5(Day):

	def run(self):
		instructions = self.to_int(self.input.splitlines())
		steps = 0
		step = 0
		while 0 <= step < len(instructions):
			current_step = step
			step += instructions[current_step]

			instructions[current_step] += 1
			steps += 1

		print(steps)


class Day6(Day):

	def run(self):
		banks = self.to_int(self.input.split())
		configs = list()
		configs.append(self.banks_to_str(banks))

		while True:
			bank_index = banks.index(max(banks))
			amount_for_each = banks[bank_index] / (len(banks) - 1)

			if not amount_for_each == int(amount_for_each):
				amount_for_each = math.floor(amount_for_each)
				banks[bank_index] = 1
			else:
				banks[bank_index] = 0

			amount_for_each = int(amount_for_each)
			self.increase_selective(banks, bank_index, amount_for_each)

			str_bank = self.banks_to_str(banks)
			if str_bank in configs:
				break
			configs.append(str_bank)

		print(len(configs))

	@staticmethod
	def increase_selective(banks: list, avoid: int, amount: int):
		for i, b in enumerate(banks):
			if not i == avoid:
				banks[i] += amount
		return banks

	def banks_to_str(self, banks):
		return "/".join(self.to_string(banks))
