import math_functions

number1 = int(input('Tell me the first number: '))
number2 = int(input('Tell me the second number: '))
number3 = int(input('Tell me the third number: '))

maximum = math_functions.max_of_three(number1, number2, number3)
minimum = math_functions.min_of_three(number1, number2, number3)

print(f'The maximum number is {maximum}')
print(f'The minimum number is {minimum}')