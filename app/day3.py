import math

from app.day import Day


class GridPos:

	def __init__(self, x: int, y: int, value: int = 0):
		self.x = x
		self.y = y
		self.value = value

	def __eq__(self, other):
		if other is not GridPos:
			return False
		return self.x == other.x and self.y == other.y

	def __str__(self):
		return "[(" + str(self.x) + ", " + str(self.y) + ") -> " + str(self.value) + "]"


class Grid:

	def __init__(self):
		self.cells = list()

	def add(self, pos: GridPos):
		self.cells.append(pos)

	def get(self, x: int, y: int):
		target_index = self.cells.index(GridPos(x, y))
		if target_index is None:
			return GridPos(x, y)
		else:
			return self.cells[target_index]


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
		grid = Grid()
		grid.add(GridPos(0, 0, 1))

		last_x = 0
		last_y = 0
		side = 1
		while side < 10:
			x = last_x + 1
			y = last_y
			grid.add(GridPos(x, y))
			while y <= side:
				y += 1
				grid.add(GridPos(x, y))
				# TODO flemme

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
