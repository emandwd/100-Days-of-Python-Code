from calculator_art import calculator_art_1
import os
def operation (num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')

def user_input(num1):
    print(" + \n - \n * \n /")
    operator = input("Pick an operation?: ")
    num2 = int(input("What's the second number?: "))
    result = int(operation (num1, num2, operator))
    print(f"{num1} {operator} {num2} = {result}")
    return result


print(calculator_art_1[0])
num1 = int(input("What's the first number?: "))

while True:
    num1 = user_input(num1)
    user_answer = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation, or 'q' to quit: ").lower()
    if user_answer == 'y':
        continue
    elif user_answer == 'n':
        print("\n" * 50)
        print(calculator_art_1[0])
        num1 = int(input("What's the first number?: "))
    elif user_answer == 'q':
        print("Goodbye")
        break



