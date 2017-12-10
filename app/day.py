from abc import abstractmethod


class Day(object):

	def __init__(self, file: str = None, inp: str = None, file_2: str = None, inp_2: str = None):
		if file is not None:
			self.input = open(file).read()
		elif inp is not None:
			self.input = inp
		else:
			self.input = str()

		if file_2 is not None:
			self.input_2 = open(file_2).read()
		elif inp_2 is not None:
			self.input_2 = inp_2
		else:
			self.input_2 = self.input

		self.to_int = lambda x_list: [int(x) for x in x_list]
		self.to_string = lambda x_list: [str(x) for x in x_list]

	@abstractmethod
	def part_1(self):
		pass

	@abstractmethod
	def part_2(self):
		pass

	@staticmethod
	def ask_input():
		return input("Enter input:\n> ")
