from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.update_board()
        
    def update_board(self):
        self.write(f"Score: {self.total_score}",False,"center",("Arial",25,"normal"))

    def increase_score_red(self):
        self.total_score += 5
        self.clear()
        self.update_board()

    def increase_score_blue(self):
        self.total_score += 1
        self.clear()
        self.update_board()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",False,"center",("Arial",25,"normal"))

        
        