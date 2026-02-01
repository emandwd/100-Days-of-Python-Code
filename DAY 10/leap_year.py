''' leap year --> 1- on every year that is divisible by 4 with no remainder
--> 2- except every year that is evenly divisible by 100 with no remainder
--> 3- unless the year is also divisible by 400 with no remainder  --> because of the word unless which mean that the
400 may change the condition of 100 if it is true we will start with the 400 in the if condition
'''

def is_leap_year(year):
    ''' If the year is divisible by 400 → Leap year
Else if the year is divisible by 100 → Not a leap year
Else if the year is divisible by 4 → Leap year
Else → Not a leap year  '''

    if year % 400 == 0:
            return True
    elif year % 100 == 0:
            return False
    elif year % 4 == 0:
            return True
    else:
            return False


choosen_year = int(input(" Enter the year: "))
if is_leap_year(choosen_year):
    print(f"{choosen_year} is a leap year")
else:
    print(f"{choosen_year} is not a leap year")



