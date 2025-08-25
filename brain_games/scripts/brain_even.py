#!/usr/bin/env python3

import random

import prompt

from brain_games.cli import welcome_user

MAX_SUCCESS_COUNT = 3
MIN = 0
MAX = 100


def main():
    username = welcome_user()
    game(username)


if __name__ == "__main__":
    main()


def game(username):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    success_count = 0

    while success_count < MAX_SUCCESS_COUNT:
        question = ask()
        print(f"Question: {question}")

        answer = prompt.string("You answer: ").strip().lower()
        correct_answer = get_correct_answer(question)

        if answer == correct_answer:
            print("Correct!")
            success_count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {username}!")
            return

    if success_count == MAX_SUCCESS_COUNT:
        congrats(username)


def ask():
    return random.randint(MIN, MAX)


def get_correct_answer(question):
    return "yes" if is_even(question) else "no"


def is_even(number):
    return number % 2 == 0


def congrats(username):
    print(f"Congratulations, {username}!")
