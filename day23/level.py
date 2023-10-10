from turtle import Turtle

LOCATION = (-260, 260)
class Level(Turtle):


    def __init__(self):
        super().__init__()
        self.level = 0
        self.create_scoreboard()
        self.goto(LOCATION)
        self.print_level()

    def create_scoreboard(self):
        self.penup()
        self.hideturtle()

    def next(self):
        self.level += 1
        self.clear()
        self.print_level()

    def print_level(self):
        self.write(f"Level: {self.level}", align="left", font=("Arial", 14, "normal"))


    def game_over(self):
        self.create_scoreboard()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 14, "normal"))