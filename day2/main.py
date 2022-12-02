import re
from enum import IntEnum

class Shape(IntEnum):
    X = 1
    Y = 2
    Z = 3

    def points(shape: str) -> int:
        if shape == Shape.X.name:
            return Shape.X.value
        if shape == Shape.Y.name:
            return Shape.Y.value
        if shape == Shape.Z.name:
            return Shape.Z.value

    def result(mine: str, other: str) -> int:
        if mine == Shape.transform(other):
            return GameResult.D.value

        if mine == "X" and other == "C":
            return GameResult.W.value
        if mine == "Y" and other == "A":
            return GameResult.W.value
        if mine == "Z" and other == "B":
            return GameResult.W.value

        return GameResult.L.value

    def transform(shape: str) -> str:
        if shape == "A":
            return "X"
        if shape == "B":
            return "Y"
        if shape == "C":
            return "Z"
        

class GameResult(IntEnum):
    L = 0
    D = 3
    W = 6


def calculate_total_points(rows: list) -> int:
    total_points = 0

    for row in rows:
        other, mine = re.split(' ', row)
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