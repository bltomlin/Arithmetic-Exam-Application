# -*- coding: utf-8 -*-
"""
This file contains the main entry point for the program that
dictates all logical flow.
"""
from src import io_functions, business_logic


def arith_expert():
    """
    Entry point for program.

    :return: void
    """
    difficulty_level = business_logic.difficulty()
    correct_answer_count = 0

    if difficulty_level == 1:
        correct_answer_count = business_logic.simple_ops()
    elif difficulty_level == 2:
        correct_answer_count = business_logic.int_squares()
    else:
        print('Something is wrong')
        exit()
    io_functions.save_score_to_file(correct_answer_count, difficulty_level)


if __name__ == '__main__':
    arith_expert()
