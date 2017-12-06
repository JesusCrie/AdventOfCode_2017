from app.day import Day


class Day1(Day):

	def run(self):
		print(sum([int(char) for index, char in enumerate(self.input) if char == self.input[(index + 1) % len(self.input)]]))
