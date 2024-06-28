from turtle import Turtle, Screen, colormode
import random


timmy = Turtle()
timmy.speed("fastest")
colormode(255)
timmy.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(0, 361, 5):
    timmy.setheading(_)
    timmy.pencolor(random_color())
    timmy.circle(150)


'''def draw_dashed_line(turtle: Turtle):
    for nbr in range(0,10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def draw_shape(turtle: Turtle, x: int):
    angle = 360/x
    for _ in range(x):
        turtle.forward(100)
        turtle.right(angle)

timmy.hideturtle()
timmy.pensize(10)
timmy.speed("fastest")
for _ in range(200):
    random_color = colors[random.randint(0, len(colors)-1)]
    random_angle = 90 * random.randint(0,3)
    timmy.setheading(random_angle)
    timmy.pencolor(random_color)
    timmy.forward(50)'''











screen = Screen()
screen.exitonclick()

