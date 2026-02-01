from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
''' color(colorstring), color((r,g,b)), color(r,g,b)
Inputs as in pencolor(), set both, fillcolor and pencolor, to the given value. '''
''' Set pencolor to colorstring, which is a Tk color specification string '''
''' GUI stands for Graphical User Interface — it's the part of an application that users see and interact with (like buttons, text fields, windows).
 Tkinter is a Python library used to create GUIs. '''
timmy_the_turtle.forward(100)






screen = Screen()
screen.exitonclick()