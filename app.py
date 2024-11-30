#fisrt number variable
first_number=float(input("Enter a number: "))

#operation sign variable
operation=input("Enter a mathimatical operation e.g +,-,/ 0r *: ")

#second number variable
second_number=float(input("Enter the second number: "))

#if statement operation to add, subtract, divide or multiply
if operation== '+':
    print(first_number + second_number)
elif operation == '-':
    print(first_number-second_number)
elif operation == '/':
    print(first_number/second_number)
elif operation == '*':
    print(first_number*second_number)
else:
    print("operation input error")