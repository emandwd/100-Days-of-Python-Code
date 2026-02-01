''' Prime numbers are numbers that can only be cleanly divided by themselves and 1.
You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.
It should return True or False.'''
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    # If a number is not prime, then it must have a factor less than or equal to its square root.
    for i in range(3, int(num ** 0.5) + 1, 2):  # 7*7 = 49 and square root 49 is equal to 7
        # range(start, stop, step) --> step is equal to 2 which means skip the even numbers because we already checked that
        if num % i == 0:
            return False
    return True

# If you want to accept decimal numbers and still process them into integer NOT rounding
user_number = int(float(input('Please enter a number: ')))
if is_prime(user_number) == True:
    print('The number is prime.')
else:
    print('The number is NOT prime.')




