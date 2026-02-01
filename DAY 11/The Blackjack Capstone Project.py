''' Blackjack is a card game where the goal is to get as close to 21
as possible without going over.
You’re playing against the computer (dealer), and both of you are dealt cards.
1.Each player starts with 2 cards.
2.Cards 2–10 = their value.
Face cards (J, Q, K) = 10
Ace (A) = either 11 or 1, depending on IF YOU ARE OVER 21 OR BELLOW 21.
3.You can choose to:
Hit (draw another card)
Stand (stop drawing)
4.If your score goes over 21, you bust and lose AND if you and the computer have equal number then it is called draw.
5.The dealer will draw until they reach at least 17.
6.The one with the highest score ≤ 21 wins.'''
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards): # Takes a list of cards and returns the score.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare_scores(user_answer, computer_answer):
    if user_answer == computer_answer:
        return "Draw "
    elif user_answer > 21:
        return "You lose "
    elif computer_answer > 21:
        return "You win"
    elif computer_answer == 0:
        return "You lose "
    elif computer_answer == 0:
        return "You win "
    elif user_answer > computer_answer:
        return "You win "

user_cards = []
computer_cards = []
game_over = False
computer_score = -1
user_score = -1

for _ in range(2) : # for _ in range(2) means: "Repeat this block 2 times, I don't care about the counter.
    # new_card = deal_card()
    # user_cards.append(new_card)
    # computer_cards.append(new_card)
    # that mean the computer and the user will take the same card ; however, we want each one of them takes different card so this is wrong
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while game_over == False:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score > 21 or computer_score == 0 or user_score == 0:
        game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            game_over = True

while computer_score !=0 and computer_score < 17 :
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"   Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
print(f"   Dealer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
print(compare_scores(calculate_score(user_cards), calculate_score(computer_cards)))
