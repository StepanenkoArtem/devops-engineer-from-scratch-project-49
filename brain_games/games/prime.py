import math
import random

MIN = 0
MAX = 100


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    question = random.randint(MIN, MAX)
    answer = get_correct_answer(question)
    return question, answer


def get_correct_answer(question):
    return "yes" if is_prime(question) else "no"


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    divide_remainders = []
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        divide_remainders.append(number % i)
        if 0 in divide_remainders:
            return False
    return True
