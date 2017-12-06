from app.day import Day


class Day4(Day):

	def part_1(self):
		lines = [l.split() for l in self.input.splitlines()]
		print(len([l for l in lines if self.is_line_valid(l)]))

	def part_2(self):
		pass

	@staticmethod
	def is_line_valid(line: list):
		return len(line) == len(set(line))
