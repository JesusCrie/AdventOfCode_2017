from app.day import Day


class Day2(Day):

	def part_1(self):
		rows = [self.to_int(s.split("\t")) for s in self.input.splitlines()]
		print(sum([max(row) - min(row) for row in rows]))

	def part_2(self):
		rows = [self.to_int(s.split("\t")) for s in self.input_2.splitlines()]

		total = 0
		for row in rows:
			for num in row:
				for other in row:
					if num == other:
						continue
					elif self.is_divisible(num, other):
						total += int(num / other)

		print(total)

	@staticmethod
	def is_divisible(first: int, second: int):
		return first % second == 0
