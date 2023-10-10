from turtle import Turtle, Screen
from character import Character
from level import Level
from car import CarManager

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)
screen.colormode(255)

level = Level()
character = Character()
car_manager = CarManager()


screen.listen()
screen.onkey(character.move_up, "Up")

game_is_on = True
while game_is_on:
    car_speed = 0.1
    time.sleep(car_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision with car
    for car in car_manager.all_cars:
        if car.distance(character) < 20:
            print("Ouch")
            game_is_on = False
            level.game_over()

    # Cars reach the end

    if character.is_at_finish_line():
        character.go_to_start()
        car_manager.level_up()
        level.next()






    # More than 1 car to move.
    # Using a for loop, create a number of cars and add them to list,
    # Using that list to move the vehicles


screen.exitonclick()