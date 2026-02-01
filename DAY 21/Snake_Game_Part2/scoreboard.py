from turtle import Turtle
Alignment = "center"
Font = ("Courier", 24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
           self.high_score = int(data.read())# It should be converted to an integer because input always returns a string.
        self.color("white")
        self.penup()
        self.goto(0, 260)
        # https://docs.python.org/3/library/turtle.html#turtle.write
        self.hideturtle()
        self.uptade_scoreboard()

    def uptade_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align=Alignment, font=Font)

    def increase_score(self):
        self.score +=1
        self.uptade_scoreboard()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode ="w") as data :
                data.write(f"{self.high_score}")
        self.score = 0
        self.uptade_scoreboard()

    # def game_over(self):
        # self.goto(0, 0)
        # self.write("GAME OVER", align = Alignment, font = Font )