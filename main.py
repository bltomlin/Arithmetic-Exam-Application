equation = input().split()
if equation[1] == '+':
    answer = int(equation[0]) + int(equation[2])
    print(answer)
if equation[1] == '-':
    answer = int(equation[0]) - int(equation[2])
    print(answer)
if equation[1] == '*':
    answer = int(equation[0]) * int(equation[2])
    print(answer)
