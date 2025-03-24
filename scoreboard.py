from turtle import Turtle
FONT = "Arial"
FONT_TYPE = "normal"
FONT_SIZE = 18
FONT_ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.getHighScore()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=FONT_ALIGNMENT, font=(FONT,FONT_SIZE,FONT_TYPE))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.display_score()

    def display_game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align=FONT_ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))


    def getHighScore(self):
        try:
            with open("high_score.txt", "r") as file:
                high_score = int(file.read())
                return high_score
        except FileNotFoundError:
            high_score = 0
            with open("high_score.txt", "w") as file:
                file.write(str(high_score))
                return high_score


    def write_high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.highscore))

