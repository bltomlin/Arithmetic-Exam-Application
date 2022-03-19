import random

#global variables are declared
answer = 0                                  #initializes a number to keep track of number  
                                            #of questions answered corectly

answer_count = 0                            #initializes a count to keep track of 
                                            #questions asked
user_answer = 0

#methods that will be used

#adds two numbers
def add(x, y):
    return x + y

#subtracts two numbers
def sub(x, y):
    return x - y
    
#multiplys two numbers
def multiply(x, y):
    return x * y

def difficulty():
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
                    return user_answer
            except ValueError:
                continue
    else:
        if (user_answer == 1) or (user_answer == 2):
            return user_answer
        else:
            while (user_answer != 1) or (user_answer != 2):
                print('Incorrect format.')
                try:
                    user_answer = int(input())
                    if (user_answer == 1) or (user_answer == 2):
                        return user_answer
                except ValueError:
                    continue

def simple_ops(user_answer):
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
    print('Your mark is ' + str(answer_count) + '/5')


    


