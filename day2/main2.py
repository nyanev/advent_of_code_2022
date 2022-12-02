import re
from enum import IntEnum

class Shape(IntEnum):
    A = 1
    B = 2
    C = 3

    def points(shape: str) -> int:
        if shape == Shape.A.name:
            return Shape.A.value
        if shape == Shape.B.name:
            return Shape.B.value
        if shape == Shape.C.name:
            return Shape.C.value

    def result(mine: str, other: str) -> int:
        if mine == other:
            return GameResult.D.value

        if mine == "A" and other == "C":
            return GameResult.W.value
        if mine == "B" and other == "A":
            return GameResult.W.value
        if mine == "C" and other == "B":
            return GameResult.W.value

        return GameResult.L.value

class GameResult(IntEnum):
    L = 0
    D = 3
    W = 6

def calculate_mine_shape(other: str, result: str) -> str:
    if result == "Y":
        return other

    if result == "X":
        if other == "C":
            return "B"
        if other == "A":
            return "C"
        if other == "B":
            return "A"

    if result == "Z":
        if other == "C":
            return "A"
        if other == "A":
            return "B"
        if other == "B":
            return "C"

def calculate_total_points(rows: list) -> int:
    total_points = 0

    for row in rows:
        other, result = re.split(' ', row)
        mine = calculate_mine_shape(other, result)
        print(mine)
        print(Shape.result(mine, other))
        total_points += Shape.points(mine) + Shape.result(mine, other)

    return total_points

def main():
    f = open("input.txt", "r")
    numbers = re.split('\n', f.read())

    summed_points = calculate_total_points(rows=numbers)
    print(summed_points)

if __name__ == "__main__":
    main()