import re
import itertools

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i+1]
        elif op == '*':
            result *= numbers[i+1]
        elif op == '||':
            result = int(str(result) + str(numbers[i+1]))
    return result

def solve_calibration(expressions, part2=False):
    total_calibration = 0
    
    for expression in expressions:
        operators = ['+', '*', '||'] if part2 else ['+', '*']
        for ops in itertools.product(operators, repeat=len(expression['equation']) - 1):
            try:
                if evaluate_expression(expression['equation'], ops) == expression['result']:
                    total_calibration += expression['result']
                    break
            except:
                continue
    
    return total_calibration

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

raw_numbers = [[int(number) for number in re.findall(r'\d+', line)] for line in lines]

expressions = [
    {
        "result": numbers[0],
        "equation": numbers[1:]
    }
    for numbers in raw_numbers
]

# Part 1
print(f"Part 1: {solve_calibration(expressions)}")

# Part 2
print(f"Part 2: {solve_calibration(expressions, True)}")