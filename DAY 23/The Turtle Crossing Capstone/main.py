import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)  # height is 600 which mean the y_axis in +ve side is 300 and -ve side -300
screen.tracer(0)

player1 = Player((0,-280))
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player1.go_up, "Up")

game_is_on = True
while game_is_on: # So the loop runs 10 times per second,
    time.sleep(0.1) # pauses the loop for 0.1 seconds
    screen.update()
    car_manager.create_cars() # is called ~10 times per second
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player1)< 20 :
            game_is_on = False
            scoreboard.game_over()

    if player1.is_at_finish_line():
        player1.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()