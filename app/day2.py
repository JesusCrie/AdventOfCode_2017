from app.day import Day


class Day2(Day):

	def part_1(self):
		rows = [self.to_int(s.split("\t")) for s in self.input.splitlines()]
		print(sum([max(row) - min(row) for row in rows]))

	def part_2(self):
		pass
