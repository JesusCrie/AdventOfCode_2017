from app.day import Day


class Day1(Day):

	def part_1(self):
		valid_chars = [int(c) for i, c in enumerate(self.input) if c == self.get_matching(self.input, i, 1)]
		print(sum(valid_chars))

	def part_2(self):
		self.input_2 = self.to_int(self.input_2)
		step = int(len(self.input_2) / 2)
		valid = [c for i, c in enumerate(self.input_2) if c == self.get_matching(self.input_2, i, step)]

		print(sum(valid))

	@staticmethod
	def get_matching(num: str, index: int, step: int):
		next_index = (index + step) % len(num)
		return num[next_index]
