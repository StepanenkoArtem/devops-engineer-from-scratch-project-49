#!/usr/bin/env python3


import prompt

from brain_games.cli import welcome_user

MAX_SUCCESS_COUNT = 3


def run(game):
    username = welcome_user()
    print(game.DESCRIPTION)
    success_count = 0

    while success_count < MAX_SUCCESS_COUNT:
        question = game.get_question()
        print(f"Question: {question}")

        user_answer = get_user_answer()
        correct_answer = str(game.get_correct_answer(question))

        if user_answer == correct_answer:
            print("Correct!")
            success_count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {username}!")
            return

    if success_count == MAX_SUCCESS_COUNT:
        congrats(username)


def get_user_answer():
    return prompt.string("You answer: ").strip().lower()


def congrats(username):
    print(f"Congratulations, {username}!")
