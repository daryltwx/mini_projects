import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

colors = ["cyan", "purple", "honeydew", "blue", "orange", "pink", "burlywood", "green", "black", "violet"]

# Step 1. Set pen related codes thickness & colors
# Step 2. random direction (left, right, up, down)
# Step 3. while true


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color
  
direction = [0, 90, 180, 270]
tim.speed("fastest")
tim.pensize(10)

while True:
  tim.pencolor(random_color())
  tim.forward(30)
  tim.setheading(random.choice(direction))
  



screen = Screen()
screen.exitonclick()


"""
def draw_shape(num_sides):
  angle = 360 / num_sides
  for _ in range(num_sides):
    tim.forward(100)
    tim.right(angle)

for shape_side_n in range(3, 11):
  tim.color(random.choice(colors))
  draw_shape(shape_side_n)


"""