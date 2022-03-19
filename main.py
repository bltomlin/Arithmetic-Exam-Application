import random

user_answer = 0
answer_count = 0

#adds two numbers
def add(x, y):
    return x + y

#subtracts two numbers
def sub(x, y):
    return x - y
    
#multiplys two numbers
def multiply(x, y):
    return x * y

#user selects difficulty
def difficulty():
    global user_answer
    print('Which level do you want? Enter a number:')
    print('1 - simple operations with numbers 2-9')
    print('2 - integral squares of 11-29')
    try:
        user_answer = int(input())
    except ValueError:
        while (user_answer != 1) or (user_answer != 2):    #checks for answer, possible incorrect input
            print('Incorrect format.')
            try:
                user_answer = int(input())
                if (user_answer == 1) or (user_answer == 2):
                    return
            except ValueError:
                continue
    else:
        if (user_answer == 1) or (user_answer == 2):
            return
        else:
            while (user_answer != 1) or (user_answer != 2):
                print('Incorrect format.')
                try:
                    user_answer = int(input())
                    if (user_answer == 1) or (user_answer == 2):
                        return
                except ValueError:
                    continue

#5 pseudo-random questions on math sum, difference and multiplcation.
def simple_ops():
    global answer_count
    for question_count in range(5):             #asks 5 questions
        user_answer = 0
        x = random.randint(2,9)                 #sets variables used in question
        y = random.randint(2,9)
        operator = ['+', '*', '-']      
        operator = random.choice(operator)      #sets a pseudo-random operator
        equation = str(x) + operator + str(y)   #sets string for question


        #checks answer to problem based on operator
        if equation[1] == '+':
            answer = add(x, y)
        elif equation[1] == '-':
            answer = sub(x, y)
        else:
            answer = multiply(x, y)
        print(' '.join(equation))

        
        #user inputs the answer
        try:
            user_answer = int(input())
        except ValueError:
            while not int(user_answer):         #checks for answer, possible incorrect input
                print('Incorrect format.')
                try:
                    user_answer = int(input())
                except ValueError:
                    continue
            if user_answer == answer:
                print('Right!')
                answer_count += 1
            else:
                print('Wrong')
        else:
            #Output of program
            if user_answer == answer:
                print('Right!')
                answer_count += 1
            else:
                print('Wrong!')
    print('Your mark is ' + str(answer_count) + '/5. Would you like to save your result to the file? Enter yes or no.')

#5 pseudo_random questions on squaring numbers
def int_squares():
    global answer_count
    for question_count in range(5):             #asks 5 questions
        user_answer = 0
        x = random.randint(11,29) 
        equation = str(x)

        answer = multiply(x, x)
        print(equation)

        try:
            user_answer = int(input())
        except ValueError:
            while not int(user_answer):         #checks for answer, possible incorrect input
                print('Incorrect format.')
                try:
                    user_answer = int(input())
                except ValueError:
                    continue
            if user_answer == answer:
                print('Right!')
                answer_count += 1
            else:
                print('Wrong')
        else:
            #Output of program
            if user_answer == answer:
                print('Right!')
                answer_count += 1
            else:
                print('Wrong!')
    print('Your mark is ' + str(answer_count) + '/5. Would you like to save your result to the file? Enter yes or no.')
    return answer_count


#asking user if they want to save the final score
def save_score(answer_count, user_answer):
    level_desc = ''
    if user_answer == 1:
        level_desc = 'simple operations with numbers 2-9'
    elif user_answer == 2:
        level_desc = 'integral squares 11-29'
    else:
        print('Program is broken')
        quit()
    user_input = str(input())
    if user_input.lower() == 'yes' or user_input == 'y':
        print('What is your name?')
        user_name = str(input())
        results = open('results.txt', 'w', encoding="utf-8")
        results.write(f'{user_name}: {answer_count}/5 in level {user_answer} ({level_desc}).')
        results.close()
        print('The results are saved in "results.txt".')
    else:
        exit()


def main():
    global answer_count
    global user_answer
    difficulty()
    if user_answer == 1:
        simple_ops()
    elif user_answer == 2:
        int_squares()
    else:
        print('Something is wrong')
        exit()
    save_score(answer_count, user_answer)

main()
