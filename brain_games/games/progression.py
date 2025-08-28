import random

MIN_LENGTH = 5
MAX_LENGTH = 15

MIN_STEP = 1
MAX_STEP = 10

DESCRIPTION = "What number is missing in the progression?"


def get_question():
    progression = build_progression()

    hidden_item_index = random.randint(0, len(progression) - 1)
    answer = str(progression[hidden_item_index])
    progression[hidden_item_index] = ".."
    question = " ".join(list(map(lambda number: str(number), progression)))
    return question, answer


def build_progression():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(1, 100)  # Starting with a positive integer
    step = random.randint(MIN_STEP, MAX_STEP)

    progression = []
    for i in range(length):
        progression.append(start + i * step)

    return progression
