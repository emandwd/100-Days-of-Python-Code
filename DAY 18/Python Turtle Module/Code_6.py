import turtle as t
import random

tim = t.Turtle()

t.colormode(255)

def random_color():
    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,225)
    return (r,g,b)

'''colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]'''
directions = [0, 90, 180, 270]
tim.pensize(15) # make the pen size much thicker
tim.speed("fastest") # make it much faster

for _ in range(200):
    tim.color(random_color())  # change the color for each line
    tim.forward(39)
    tim.setheading(random.choice(directions))

''' RGB color that is represented by a tuple 
Python Tuples = (1, 3, 8) which is somehow like a list
my_tuple = (1, 3, 8)
my_tuple[2] = 8
The difference between tuple and a list is that tuple can't be changed ever. It is constant.
rgb(117, 61, 163) --> RGB color 
https://www.w3schools.com/colors/colors_rgb.asp
'''

