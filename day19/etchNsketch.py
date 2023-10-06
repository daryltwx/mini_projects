from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
  tim.forward(10)

def move_backwards():
  tim.backward(10)

def turn_right():
  tim.right(10)

def turn_left():
  tim.left(10)

def reset():
  tim.reset()

# Listening for keystrokes.
screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=reset, key="c")
screen.exitonclick()