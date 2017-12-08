from app.day import Day
from app.day1 import Day1
from app.day2 import Day2
from app.day3 import Day3
from app.day4 import Day4
from app.day5 import Day5
from app.day6 import Day6


def start(day: Day):
	print(">>> " + day.__class__.__name__ + " <<<")
	print("> Part 1")
	day.part_1()
	print("> Part 2")
	day.part_2()


if __name__ == "__main__":
	start(Day1(file = "resources/day1.input", file_2 = "resources/day1_2.input"))
	start(Day2(file = "resources/day2.input", file_2 = "resources/day2.input"))
	start(Day3(inp = "312051"))
	start(Day4(file = "resources/day4.input"))
	start(Day5(file = "resources/day5.input"))
	start(Day6(inp = "14 0 15 12 11 11 3 5 1 6 8 4 9 1 8 4"))
