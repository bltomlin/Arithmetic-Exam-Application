# -*- coding: utf-8 -*-
"""
This module contains all general functions that contain
code that is more reusable throughout the project.
"""


def validate_user_answer(answer):
    """
    Validate the user's input is an integer and that it is equivalent to
    the defined answer for the current question.

    :param answer: the programmatically calculated answer (not user answer)
    :return: 1 if user answers correctly, 0 if user answers incorrectly
    """
    user_answer = ""

    try:
        user_answer = int(input())
    except ValueError:
        while not int(user_answer):
            print('Incorrect format.')
            try:
                user_answer = int(input())
            except ValueError:
                continue
        if user_answer == answer:
            print('Right!')
            return 1
        else:
            print('Wrong')
            return 0
    else:
        # Output of program
        if user_answer == answer:
            print('Right!')
            return 1
        else:
            print('Wrong!')
            return 0
