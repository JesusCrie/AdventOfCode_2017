import math

from app.day import Day


class GridPos:

	def __init__(self, x: int, y: int, value: int = 0):
		self.x = x
		self.y = y
		self.value = value

	def __eq__(self, other):
		if not isinstance(other, GridPos):
			return False
		return self.x == other.x and self.y == other.y

	def __str__(self):
		return "[(" + str(self.x) + ", " + str(self.y) + ") -> " + str(self.value) + "]"


class Grid:

	def __init__(self):
		self.cells = list()
		self.cells.append(GridPos(0, 0, 1))

	def add(self, pos: GridPos):
		self.cells.append(pos)
		return pos

	def __add_and_set__(self, pos: GridPos):
		top_left = self.get_value(pos.x - 1, pos.y + 1)
		top = self.get_value(pos.x, pos.y + 1)
		top_right = self.get_value(pos.x + 1, pos.y + 1)
		left = self.get_value(pos.x - 1, pos.y)
		right = self.get_value(pos.x + 1, pos.y)
		bottom_left = self.get_value(pos.x - 1, pos.y - 1)
		bottom = self.get_value(pos.x, pos.y - 1)
		bottom_right = self.get_value(pos.x + 1, pos.y - 1)

		pos.value = top_left + top + top_right + left + right + bottom_left + bottom + bottom_right
		self.add(pos)
		return pos

	def add_and_set(self, x: int, y: int):
		return self.__add_and_set__(GridPos(x, y))

	def get(self, x: int, y: int):
		try:
			target_index = self.cells.index(GridPos(x, y))
		except ValueError:
			target_index = None

		if target_index is None:
			return GridPos(x, y)
		else:
			return self.cells[target_index]

	def get_value(self, x: int, y: int):
		return self.get(x, y).value

	def get_last(self):
		return self.cells[len(self.cells) - 1]


class Day3(Day):

	def part_1(self):
		self.input = int(self.input)

		corner = self.get_grid_corner(self.input)
		size = int(math.sqrt(corner))
		top, right, bottom, left = self.get_grid_borders(corner)

		target_x = 0
		target_y = 0

		if self.input in top:
			target_x = top.index(self.input)
		elif self.input in bottom:
			target_x = bottom.index(self.input)
			target_y = size - 1
		elif self.input in left:
			target_y = left.index(self.input)
		elif self.input in right:
			target_y = right.index(self.input)
			target_x = size - 1

		zero = math.floor(size / 2)

		distance_x = int(math.fabs(target_x - zero))
		distance_y = int(math.fabs(target_y - zero))

		distance = distance_x + distance_y

		print("Corner: " + str(corner) + " (" + str(size) + ")")
		print("Target -> X: " + str(target_x) + ", Y: " + str(target_y))
		print(distance)

	def part_2(self):
		self.input_2 = int(self.input_2)
		grid = Grid()
		size = 3
		x = 0
		y = 0
		while True:
			try:
				# generate right
				x += 1
				grid.add_and_set(x, y)
				self.check_value(grid.get_last())
				for xx in range(size - 2):
					y += 1
					grid.add_and_set(x, y)
					self.check_value(grid.get_last())

				# generate top
				for xx in range(size - 1):
					x -= 1
					grid.add_and_set(x, y)
					self.check_value(grid.get_last())

				# generate left
				for xx in range(size - 1):
					y -= 1
					grid.add_and_set(x, y)
					self.check_value(grid.get_last())

				# generate bottom
				for xx in range(size - 1):
					x += 1
					grid.add_and_set(x, y)
					self.check_value(grid.get_last())

				size += 2
			except StopIteration:
				break

		print(grid.get_last().value)

	@staticmethod
	def get_grid_corner(target: int):
		closest_square = math.ceil(math.sqrt(target))
		if closest_square % 2 == 0:
			closest_square += 1

		return int(closest_square) ** 2

	@staticmethod
	def get_grid_borders(corner: int):
		size = int(math.sqrt(corner))

		corner_left = corner - size + 1
		bottom = [c for c in range(corner_left, corner + 1)]

		corner_top = corner_left - size + 1
		left = [c for c in range(corner_top, corner_left + 1)]

		corner_right = corner_top - size + 1
		top = [c for c in range(corner_right, corner_top + 1)]
		top.reverse()

		corner_bottom = corner_right - size + 2
		right = [c for c in range(corner_bottom, corner_right + 1)]
		right.reverse()

		return top, right, bottom, left

	def check_value(self, to_check: GridPos):
		if to_check.value > self.input_2:
			raise StopIteration
