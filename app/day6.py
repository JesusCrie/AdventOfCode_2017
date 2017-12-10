from app.day import Day


class Day6(Day):

	def part_1(self):
		banks = self.to_int(self.input.split())
		configs = list()
		configs.append(self.banks_to_str(banks))

		while True:
			bank_index = banks.index(max(banks))
			amount = banks[bank_index]
			banks[bank_index] = 0

			self.dispatch_from_index(banks, bank_index + 1, amount)

			str_bank = self.banks_to_str(banks)
			if str_bank in configs:
				break
			configs.append(str_bank)

		print(len(configs))

	def part_2(self):
		banks = self.to_int(self.input.split())
		configs = list()
		configs.append(self.banks_to_str(banks))

		while True:
			bank_index = banks.index(max(banks))
			amount = banks[bank_index]
			banks[bank_index] = 0

			self.dispatch_from_index(banks, bank_index + 1, amount)

			str_bank = self.banks_to_str(banks)
			if str_bank in configs:
				break
			configs.append(str_bank)

		print(len(configs))
		# Give up, need to use https://en.wikipedia.org/wiki/Cycle_detection#Floyd.27s_Tortoise_and_Hare

	@staticmethod
	def dispatch_from_index(banks: list, index: int, amount: int):
		while amount > 0:
			index = index % len(banks)
			banks[index] += 1
			amount -= 1
			index += 1

	def banks_to_str(self, banks):
		return "/".join(self.to_string(banks))
