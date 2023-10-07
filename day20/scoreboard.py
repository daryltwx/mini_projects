from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape()
        self.hideturtle()
        self.pencolor("white")
        self.goto(x=0, y=280)
        self.pendown()
        self.score = 0
        self.update_scoreboard()



    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)


