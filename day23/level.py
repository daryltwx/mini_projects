from turtle import Turtle

LEVEL = 1
LOCATION = (-260, 260)
class Level(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(LOCATION)
        self.write(f"Level: {LEVEL}", align="left", font=("Arial", 14, "normal"))