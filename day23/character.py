from turtle import Turtle

LOCATION = (0, -280)

class Character(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(LOCATION)


    def move_up(self):
        self.forward(20)

