from turtle import Turtle

ALIGNMENT = "center"
FONT = ("cOURIER", 24, "normal")


# Class inheritance. This score board class has all functionalities of turtle.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:  # Opening of file in read mode.
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=265)
        self.updatescore()
        self.hideturtle()

    def updatescore(self):  # Updates the score board.
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as highscore:  # Opening of file in write mode.
                highscore.write(str(self.score))
        self.score = 0
        self.updatescore()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def increasescore(self):
        self.score += 1
        self.updatescore()
