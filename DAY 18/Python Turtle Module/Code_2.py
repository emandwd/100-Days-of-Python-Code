''' Draw a Square '''
from turtle import Turtle, Screen
''' 
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
timmy_the_turtle.forward(100)
timmy_the_turtle.setheading(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.setheading(180)
timmy_the_turtle.forward(100)
timmy_the_turtle.setheading(270)
timmy_the_turtle.forward(100)
'''
# or

''' 
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
'''

timmy_the_turtle = Turtle()  # if you want to change the name of the object at once --> Refactor --> Rename 
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()