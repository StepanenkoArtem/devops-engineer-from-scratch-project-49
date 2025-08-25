import random

DESCRIPTION = "What is the result of the expression?"

MIN = 0
MAX = 10
OPERATIONS = ["-", "+", "*"]


def get_question():
    first_operand = get_operand()
    second_operand = get_operand()
    operator = get_operator()
    return f"{first_operand} {operator} {second_operand}"


def get_correct_answer(question):
    first_operand, operator, second_operand = question.split(" ")
    first_operand = int(first_operand)
    second_operand = int(second_operand)

    match operator:
        case "-":
            return first_operand - second_operand
        case "+":
            return first_operand + second_operand
        case "*":
            return first_operand * second_operand


def get_operand():
    return random.randint(MIN, MAX)


def get_operator():
    index = random.randint(0, len(OPERATIONS) - 1)
    return OPERATIONS[index]
