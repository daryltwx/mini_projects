from turtle import Turtle
import random


LOCATION = (random.randint(-300,300), random.randint(-200,200))
COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_WIDTH = 1
CAR_LENGTH = 3

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=CAR_WIDTH, stretch_len=CAR_LENGTH)
            new_car.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            new_car.speed("fast")
            new_car.goto((300, random.randint(-240, 240)))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
         self.car_speed += MOVE_INCREMENT
