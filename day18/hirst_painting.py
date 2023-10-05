import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")

colors = [
  (142, 27, 72), (239, 71, 36), (218, 162, 57), (13, 144, 91), (182, 165, 43), (30, 125, 190), (50, 190, 232), (244, 221, 49), (177, 41, 95), (77, 25, 77), (127, 191, 94), (34, 173, 116), (150, 29, 26), (27, 192, 218), (237, 160, 190), (10, 108, 54), (164, 211, 174), (90, 7, 7), (13, 82, 35)
]



"""
def draw_circle():
  tim.color(random.choice(colors))
  tim.fillcolor(random.choice(colors))  
  tim.begin_fill()
  tim.circle(10)
  tim.end_fill()
  
x = 0
y = 0
for _ in range(8):
  for _ in range(4):
    tim.setposition(x, y) 
    draw_circle()
    tim.penup()
    x += 50
    tim.setposition(x, y)
    tim.pendown()
    draw_circle()
    tim.penup()
    x += 50
  x = 0
  y += 50
  tim.setposition(x, y)

screen = t.Screen()
screen.exitonclick()"""



## Answer Key

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
  tim.dot(20, random.choice(colors))
  tim.forward(50)

  if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()