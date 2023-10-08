from turtle import Turtle

BALL_WIDTH = 1
BALL_LENGTH = 1
class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=BALL_WIDTH, stretch_len=BALL_LENGTH)
        self.penup()


    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def bounce(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() - 20
        self.goto(new_x, new_y)