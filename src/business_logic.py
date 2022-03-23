# -*- coding: utf-8 -*-
"""
This module contains all business logic that will be used
in this program.
"""
from src import math_operators, utility_functions
import random


def difficulty():
    """
    User to select their intended difficultly level in the terminal.

    :return: the user selected difficulty level
    """
    difficulty_level = 0
    print('Which level do you want? Enter a number:')
    print('1 - simple operations with numbers 2-9')
    print('2 - integral squares of 11-29')
    try:
        difficulty_level = int(input())
    except ValueError:
        while (difficulty_level != 1) or (difficulty_level !=
                                          2):  # checks for answer, possible incorrect input
            print('Incorrect format.')
            try:
                difficulty_level = int(input())
                if (difficulty_level == 1) or (difficulty_level == 2):
                    return difficulty_level
            except ValueError:
                continue
    else:
        if (difficulty_level == 1) or (difficulty_level == 2):
            return difficulty_level
        else:
            while (difficulty_level != 1) or (difficulty_level != 2):
                print('Incorrect format.')
                try:
                    difficulty_level = int(input())
                    if (difficulty_level == 1) or (difficulty_level == 2):
                        return difficulty_level
                except ValueError:
                    continue


def simple_ops():
    """
    5 pseudo-random questions on math sum, difference, and multiplication.

    :return: the count of questions the user answered correctly
    """
    correct_answer_count = 0
    for question_count in range(5):  # asks 5 questions
        x = random.randint(2, 9)  # sets variables used in question
        y = random.randint(2, 9)
        operator = ['+', '*', '-']
        operator = random.choice(operator)  # sets a pseudo-random operator
        equation = str(x) + operator + str(y)  # sets string for question

        # checks answer to problem based on operator
        if equation[1] == '+':
            answer = math_operators.add(x, y)
        elif equation[1] == '-':
            answer = math_operators.subtract(x, y)
        else:
            answer = math_operators.multiply(x, y)
        print(' '.join(equation))

        correct_answer_count += utility_functions.validate_user_answer(answer)
    print(
        f'Your mark is {correct_answer_count}/5. Would you like to save your result to the file? Enter yes or no (y/n).')
    return correct_answer_count


def int_squares():
    """
    5 pseudo_random questions on squaring numbers.

    :return: the count of questions the user answered correctly
    """
    correct_answer_count = 0
    for question_count in range(5):  # asks 5 questions
        x = random.randint(11, 29)
        equation = str(x)

        answer = math_operators.multiply(x, x)
        print(equation)

        correct_answer_count += utility_functions.validate_user_answer(answer)
    print(
        f'Your mark is {correct_answer_count}/5. Would you like to save your result to the file? Enter yes or no (y/n).')
    return correct_answer_count
