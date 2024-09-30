from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.bk(10)

def turn_clockwise():
    tim.setheading(tim.heading() - 10)
    
def turn_counter_clockwise():
    tim.setheading(tim.heading() + 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkeypress(fun=move_forwards, key="z")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=turn_clockwise, key="d")
screen.onkeypress(fun=turn_counter_clockwise, key="q")
screen.onkeypress(fun=clear, key="c")
screen.listen()
screen.exitonclick()
