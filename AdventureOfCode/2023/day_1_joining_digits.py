from utils import read_file


def check_digits_letters_presence(text: str):
    base = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return [number for number in base if number in text]

def get_digits(text: str) -> int:
    # digits_writtens = check_digits_letters_presence(text)

    # if not digits_writtens:
        first_digit = [digit for digit in text if digit.isdigit()][0]
        last_digit = [digit for digit in reversed(text) if digit.isdigit()][0]
        return first_digit + last_digit

    

    # for letter in text:




def solve_puzzle():
    # data = read_file(f'AdventureOfCode/2023/inputs/day1.txt')
    data = read_file(f'AdventureOfCode/2023/inputs/day1-test.txt')
    total = 0
    for line in data:
        line_copy = line
        total+= int(get_digits(line))
    return total

print(solve_puzzle())
