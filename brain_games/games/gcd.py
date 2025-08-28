import random

MIN = 0
MAX = 100


DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_question():
    first = get_operand()
    second = get_operand()
    question = f"{first} {second}"
    answer = str(calculate_gcd(first, second))
    return question, answer


def get_operand():
    return random.randint(MIN, MAX)


def calculate_gcd(first, second):
    if second == 0:
        return first
    else:
        first, second = second, (first % second)
        return calculate_gcd(first, second)
