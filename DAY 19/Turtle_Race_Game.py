import turtle
from turtle import Turtle, Screen
import random

all_turtles = []
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "cyan", "magenta"]
y_pos = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You Win! The {winning_color} turtle is the winner!")
            else:
                print(f"You Lose! The {winning_color} turtle is the winner!")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()