from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LENGTH = 1
class Paddle(Turtle):


    def __init__(self, location):
        super().__init__()
        self.location = location
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.goto(location)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)