import re

def find_elf_calories(numbers: list) -> list:
    current = 0
    elf_calories = []
    for n in numbers:
        try:
            current += int(n)
        except: 
            elf_calories.append(current)
            current = 0

    elf_calories.sort(reverse=True)

    return sorted(elf_calories, reverse=True)

def main():
    f = open("input.txt", "r")
    numbers = re.split('\n', f.read())

    summed_calories = find_elf_calories(numbers=numbers)
    biggest = summed_calories[0]
    first_three_sum = sum(summed_calories[0:3])

    print("biggest", biggest)
    print("first three", first_three_sum)

if __name__ == "__main__":
    main()
    #73211