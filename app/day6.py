from app.day import Day


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
