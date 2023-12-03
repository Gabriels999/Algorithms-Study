from utils import read_file


def get_digits(text: str) -> int:
    first_digit = [digit for digit in text if digit.isdigit()][0]
    last_digit = [digit for digit in reversed(text) if digit.isdigit()][0]
    return first_digit + last_digit


def solve_puzzle():
    data = read_file(f'AdventureOfCode/2023/inputs/day1.txt')
    total = 0
    for line in data:
        total+= int(get_digits(line))
    return total

print(solve_puzzle())
