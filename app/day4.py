from app.day import Day


class Day4(Day):

	def part_1(self):
		lines = [l.split() for l in self.input.splitlines()]
		print(len([l for l in lines if self.is_line_valid(l)]))

	def part_2(self):
		lines = [l.split() for l in self.input_2.splitlines()]
		valid = 0
		for line in lines:
			try:
				for i, word in enumerate(line):
					anagrams = [o for o in line[i + 1:] if self.is_anagram(word, o)]
					if len(anagrams) > 0:
						raise StopIteration
				valid += 1
			except StopIteration:
				pass

		print(valid)

	@staticmethod
	def is_line_valid(line: list):
		return len(line) == len(set(line))

	@staticmethod
	def is_anagram(first: str, second: str):
		list_first = list(first)
		list_second = list(second)
		list_first.sort()
		list_second.sort()

		return list_first == list_second
