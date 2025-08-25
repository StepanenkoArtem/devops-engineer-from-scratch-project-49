import random

MIN = 0
MAX = 100


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    return random.randint(MIN, MAX)


def get_correct_answer(question):
    return "yes" if is_even(question) else "no"


def is_even(number):
    return number % 2 == 0
