from app.day import *


def start(day: Day):
	day.run()


if __name__ == "__main__":
	start(Day1(file = "resources/day1.bbw"))
	start(Day2(file = "resources/day2.bbw"))
	start(Day3(inp = "312051"))
	start(Day4(file = "resources/day4.bbw"))
	start(Day5(file = "resources/day5.bbw"))
	start(Day6(inp = "14 0 15 12 11 11 3 5 1 6 8 4 9 1 8 4"))
