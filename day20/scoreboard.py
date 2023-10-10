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
        with open("data.txt") as file:
            data_high_score = int(file.read())
        self.high_score = data_high_score
        self.update_scoreboard()




    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)


