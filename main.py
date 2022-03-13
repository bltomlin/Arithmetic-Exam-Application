import random

#methods that will be used
def add(x, y):
    return x + y
    
def sub(x, y):
    return x - y
    
def multiply(x, y):
    return x * y


#Variables are delcared
answer = 0
answer_count = 0

#main
for question_count in range(5):
    user_answer = 0
    x = random.randint(2,9)
    y = random.randint(2,9)
    operator = ['+', '*', '-']
    operator = random.choice(operator)
    equation = str(x) + operator + str(y)
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
        while not int(user_answer):
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
print('Your mark is ' + str(answer_count) + '/5')
