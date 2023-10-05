import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color
  
tim.speed("fastest")


# How to draw circle
# Tilt after every circle
def draw_spirograph(size_of_gap):
  for _ in range(round(360 / size_of_gap)):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
  
screen = t.Screen()
screen.exitonclick()
