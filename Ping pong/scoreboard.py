from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_score}",False,"center",("Arial",70,"normal"))
        self.goto(100,200)
        self.write(f"{self.r_score}",False,"center",("Arial",70,"normal"))

    def left_score(self):
        self.l_score += 1
        self.update_score()

    def right_score(self):
        self.r_score += 1
        self.update_score()

