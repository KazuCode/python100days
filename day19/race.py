from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_positions = [-80, -50, -20, 10, 40, 70]
turtles = []

for _ in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[_])
    tim.penup()
    tim.goto(-230, starting_positions[_])
    turtles.append(tim)

game_is_running = True

while game_is_running:
    random_turtle = random.choice(turtles)
    random_turtle.forward(10)
    if random_turtle.xcor() == 240:
        game_is_running = False
        winner_turtle = random_turtle.fillcolor()
        screen.bye()

if winner_turtle == user_bet.lower():
    print(f"You won! The {winner_turtle} turtle won the race!")
else:
    print(f"You lose... The {winner_turtle} turtle won the race...")

screen.exitonclick()