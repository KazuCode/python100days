import colorgram
import random
from turtle import Turtle, Screen

def extract_colors():
    colors = colorgram.extract('hirst_painting.PNG', 50)
    rgb_colors = []
    for color in colors:
        rgb = color.rgb
        red = rgb.r
        green = rgb.g
        blue = rgb.b
        rgb_colors.append((red, green, blue))
    return rgb_colors


colors = (extract_colors())

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setpos(-250.0, -250.0)
screen = Screen()
screen.colormode(255)

for counter in range(1, 101):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if (counter % 10) == 0:
        tim.seth(90)
        tim.forward(50)
        tim.seth(180)
        tim.forward(500)
        tim.seth(0)


screen.exitonclick()
