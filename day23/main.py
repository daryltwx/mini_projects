from turtle import Turtle, Screen
from character import Character
from level import Level

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

level = Level()
character = Character()


screen.listen()
screen.onkey(character.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()




screen.exitonclick()