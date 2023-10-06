from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

tim = Turtle(shape="turtle")
tim.penup()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

tim.goto(x=-230, y=-100)

# for color_p in colors:
x = -230
y = -100
# tim.color(color_p)
tim.goto(x, y)
tim.color(colors[0])
y += 50

joe = tim.clone()
joe.color(colors[1])
joe.goto(x=-230, y=-50)

moe = tim.clone()
moe.color(colors[2])
moe.goto(x=-230, y=0)

toe = tim.clone()
toe.color(colors[3])
toe.goto(x=-230, y=50)

poe = tim.clone()
poe.color(colors[4])
poe.goto(x=-230, y=100)


def race():
    while True:
        tim.forward(random.randint(0, 50))
        tim_pos_x, tim_pos_y = tim.position()
        print(tim_pos_x, tim_pos_y)
        if tim_pos_x >= 390:
            print("You win")
        joe.forward(random.randint(0, 50))
        moe.forward(random.randint(0, 50))
        toe.forward(random.randint(0, 50))
        poe.forward(random.randint(0, 50))


def finish_line():
    x = 490
    y = -100


race()

screen.exitonclick()