def sum(num1,num2):
   return print("The sumation of two number is: ", num1 + num2)
def sub (num1,num2):
    return print("The substraction of two number is: ", num1 - num2)
def mul (num1,num2):
    return print("The multiplication of two number is: ",num1*num2)
def div (num1,num2):
    return print("The division of two number is: ", num1/num2)

operation = int(input('Please enter the type of operation: '))
number1 = int(input('The first number: '))
number2 = int(input('The second number: '))

if operation == 1:
    sum(number1,number2)

elif operation == 2:
    sub(number1,number2)

elif operation == 3:
    mul(number1,number2)

elif operation == 4:
    div(number1, number2)

