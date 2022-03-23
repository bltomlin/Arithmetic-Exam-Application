# -*- coding: utf-8 -*-
"""
This module contains all input/output functions. For example
saving results to an external text file.
"""


def save_score_to_file(correct_answer_count, difficulty_level):
    """
    Asks the user if they want to save their final score to a txt file.

    :param correct_answer_count: amount of questions the user answered correctly
    :param difficulty_level: the user selected difficultly level
    :return: void
    """
    level_desc = ''
    if difficulty_level == 1:
        level_desc = 'simple operations with numbers 2-9'
    elif difficulty_level == 2:
        level_desc = 'integral squares 11-29'
    else:
        print('Program is broken')
        quit()
    user_input = str(input())
    if user_input.lower() == 'yes' or user_input == 'y':
        print('What is your name?')
        user_name = str(input())
        results = open('results.txt', 'w', encoding="utf-8")
        results.write(
            f'{user_name}: {correct_answer_count}/5 in level {difficulty_level} ({level_desc}).')
        results.close()
        print('The results are saved in "results.txt".')
    else:
        exit()
