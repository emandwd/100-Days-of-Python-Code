""" https://github.com/hermitdave/FrequencyWords/tree/master/content/2018 """
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else :
    to_learn = data.to_dict(orient="records")
"""  
.to_dict(orient="records") converts that DataFrame into a list of dictionaries.
What does orient="records" mean?
It tells pandas to convert each row of the DataFrame into a dictionary, where:
The keys are the column names.
The values are the values in that row.
"""

current_card={}

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer) # This cancels the previously scheduled flip_card(). This ensures only one timer is active at any time.
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(card_word, text=current_card["French"], fill = "black")  # canvas.itemconfig(word_already_there, word=new_word)
    canvas.itemconfig(card_background, image= card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill= "white")
    canvas.itemconfig(card_background, image=card_back_img)  # canvas.itemconfig(image_already_there, image=new_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

"""
🔁 The Problem:
What happens if the user clicks the "Next" button quickly before the 3 seconds are up?
Case without flip_timer and after_cancel()
Imagine this simplified version of next_card():
def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(... show French ...)
    window.after(3000, flip_card)
1.User clicks the "Next" button at time t = 0s.
→ flip_card is scheduled to run at t = 3s.
2.User clicks "Next" again at t = 1s.
→ Another flip_card is scheduled at t = 4s.
3.Again at t = 2s.
→ Third flip_card scheduled at t = 5s.
So the app now has three separate flip timers running:
One will flip the first card.
One will flip the second card.
One will flip the third card.

🔒 Why is this safe?
Because you're:
1.Always canceling the old timer.
2.Always creating a new timer for the current card.
3.So flip_card() will only run once per card, after 3 seconds, and always for the correct card.
"""
window = Tk()
window.title("Flashy")
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Create a canvas with width 800 pixels and height 526 pixels
canvas = Canvas(width= 800, height = 526)

# Load the front image of the card
card_front_img = PhotoImage(file="images/card_front.png")

# Place the image at the center of the canvas (400 = 800/2, 263 = 526/2)
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image= card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image= cross_image, highlightthickness= 0, command= next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image= check_image, highlightthickness= 0, command= is_known)
known_button.grid(row=1, column=1)

next_card()



window.mainloop()
