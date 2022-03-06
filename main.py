#Objectives
#Generate a math task that looks like a math operation. Use the requirements above. Print it.
#Read the answer from a user.
#Check whether the answer is correct. Print Right! or Wrong!


import random

def add(x, y):
    return x + y
    
def sub(x, y):
    return x - y
    
def multiply(x, y):
    return x * y
    
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
