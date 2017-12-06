from abc import abstractmethod


class Day(object):

	def __init__(self, file: str = None, inp: str = None):
		if file is not None:
			self.input = open(file).read()
		elif inp is not None:
			self.input = inp
		else:
			self.input = str()

		self.to_int = lambda x_list: [int(x) for x in x_list]
		self.to_string = lambda x_list: [str(x) for x in x_list]

		print(">>> " + self.__class__.__name__ + " <<<")

	@abstractmethod
	def run(self):
		pass

	@staticmethod
	def ask_input():
		return input("Enter input:\n> ")
