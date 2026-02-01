from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
''' We will start each step in our 7 steps '''
''' Step 1: we need to create 3 squares beside ech other '''
'''' Step 2: Move the snake '''
''' Step 3: Create classes '''
screen.tracer(0) # Turns off automatic screen updates. Normally, turtle updates the screen after every movement

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15: # we can't say if snake.distance(food) < 15: because the snake is not a turtle so it does not have attribute of distance
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()





screen.exitonclick()