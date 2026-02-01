from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_one= True
while game_is_one:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280: # bouncing if the ball touches the y_surface up/down
        ball.bounce_y() # moving to the opposite direction along the vertical
    # Detect the collision with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0:  # The distance() method in Turtle calculates the Euclidean distance between two turtle objects (or between a turtle and a point). we are checking how far the ball is from the r_paddle.  "Is the ball close enough to the paddle to count as a hit?"
        # ball.x_move > 0 avoids multiple bounces
        # If x_move > 0 → the ball is moving right
        # If x_move < 0 → the ball is moving left
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330  and ball.x_move < 0:  # The distance() method in Turtle calculates the Euclidean distance between two turtle objects (or between a turtle and a point). we are checking how far the ball is from the r_paddle.  "Is the ball close enough to the paddle to count as a hit?"
        # ball.x_move > 0 avoids multiple bounces
        # If x_move > 0 → the ball is moving right
        # If x_move < 0 → the ball is moving left
        ball.bounce_x()


    # Detect when R paddle misses
    if  ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
    if  ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()