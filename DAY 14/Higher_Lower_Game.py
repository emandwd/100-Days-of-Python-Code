from art import logo, vs
from data import data
import random
import os
import platform
answer = True
score = 0
print(logo)
def clear(): # os.system('cls' if platform.system() == 'Windows' else 'clear') #only clears the real terminal/console window, not PyCharm's built-in output window.
    print("\n" * 100)
while answer:
    compareA = random.randint(0, 49)
    compareB = random.randint(0, 49)
    while compareB == compareA:
        compareB = random.randint(0, 49)
    print(f"Compare A: {data[compareA]['name']}, {data[compareA]['description']}, {data[compareA]['country']}")
    print(vs)
    print(f"Compare B: {data[compareB]['name']}, {data[compareB]['description']}, {data[compareB]['country']}")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if data[compareA]['follower_count'] > data[compareB]['follower_count']:
        correct_answer = 'A'
    else:
        correct_answer = 'B'
    if user_answer == correct_answer:
        score=score+1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}")
        answer = True
    else:
        answer = False
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score} ")





