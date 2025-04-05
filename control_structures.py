user_number = int(input('Choose a number: '))

if user_number < 0:
    print("It's a negative number")
elif user_number > 0:
    print("It's a positive number")
else:
    print("It's zero")
    
print('Iteration challenge!!!')
for number in range(1,11):
    if number == 5:
        print("Halfway there!")
        continue
    if number == 9:
        print("Finishing earlier")
        break
    print(number)