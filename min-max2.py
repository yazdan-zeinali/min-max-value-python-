number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

if number1 > number2 and number1 > number3:
    max_number = number1
elif number2 > number1 and number2 > number3:
    max_number = number2
else:
    max_number = number3

if number1 < number2 and number1 < number3:
    min_number = number1
elif number2 < number1 and number2 < number3:
    min_number = number2
else:
    min_number = number3

print("The maximum number is:", max_number)
print("The minimum number is:", min_number)
