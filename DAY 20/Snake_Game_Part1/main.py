from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
''' We will start each step in our 7 steps '''
''' Step 1: we need to create 3 squares beside ech other '''
'''' Step 2: Move the snake '''
''' Step 3: Create a class '''
screen.tracer(0) # Turns off automatic screen updates. Normally, turtle updates the screen after every movement
snake = Snake()
screen.update()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
game_is_on = True
while game_is_on:
    screen.update() # Manually refresh the screen after all segments have moved. This updates the screen once per loop
    time.sleep(0.1) # Without this, the snake moves instantly and too fast
    snake.move()

screen.exitonclick()