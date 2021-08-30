from turtle import Turtle,Screen

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def tilt_left():
    tim.left(10)

def tilt_right():
    tim.right(10)

def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

tim = Turtle()

screen = Screen()

screen.listen()

screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=tilt_left, key="a")
screen.onkey(fun=tilt_right, key="d")
screen.onkey(fun=clear, key="space")

screen.exitonclick()