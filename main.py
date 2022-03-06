import random
# write your code here
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
if equation[1] == '-':
    answer = sub(x, y)
if equation[1] == '*':
    answer = multiply(x, y)
print(' '.join(equation))
user_answer = input()

if user_answer == answer:
    print('Right!')
else:
    print('Wrong!')