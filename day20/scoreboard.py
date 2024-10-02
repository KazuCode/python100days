from turtle import Turtle
FONT_SCORE = ('Arial', 16, 'normal')
FONT_MESSAGE = ('Arial', 22, 'normal')
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.refresh_score()

    def refresh_score(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT_SCORE)

    def score_point(self):
        self.clear()
        self.score+=1
        self.refresh_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER.", move=False, align=ALIGNMENT, font=FONT_MESSAGE)