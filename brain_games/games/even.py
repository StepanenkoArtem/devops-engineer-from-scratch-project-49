import random

MIN = 0
MAX = 100


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    question = random.randint(MIN, MAX)
    answer = get_correct_answer(question)
    return question, answer


def get_correct_answer(question):
    return "yes" if is_even(question) else "no"


def is_even(number):
    return number % 2 == 0
