from app.day import Day


class Day5(Day):

	def part_1(self):
		instructions = self.to_int(self.input.splitlines())
		steps = 0
		step = 0
		while 0 <= step < len(instructions):
			current_step = step
			step += instructions[current_step]

			instructions[current_step] += 1
			steps += 1

		print(steps)

	def part_2(self):
		pass
