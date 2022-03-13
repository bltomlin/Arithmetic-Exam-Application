<<<<<<< HEAD
import random

#methods that will be used
=======
#Objectives
#Generate a math task that looks like a math operation. Use the requirements above. Print it.
#Read the answer from a user.
#Check whether the answer is correct. Print Right! or Wrong!


import random

>>>>>>> 9a36093b35397bd33bbdd618be90ad39f00ca89b
def add(x, y):
    return x + y
    
def sub(x, y):
    return x - y
    
def multiply(x, y):
    return x * y
<<<<<<< HEAD


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
=======
    
x = random.randint(2,9)
y = random.randint(2,9)
operator = ['+', '*', '-']
operator = random.choice(operator)
answer = 0

equation = str(x) + operator + str(y)
if equation[1] == '+':
    answer = add(x, y)
elif equation[1] == '-':
    answer = sub(x, y)
elif equation[1] == '*':
    answer = multiply(x, y)
else:
    print('Operator invalid. Please try again.')
    quit()
print(' '.join(equation))
user_answer = int(input())

if user_answer == answer:
    print('Right!')
else:
    print('Wrong!')
>>>>>>> 9a36093b35397bd33bbdd618be90ad39f00ca89b
