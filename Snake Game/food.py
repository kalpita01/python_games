from turtle import Turtle
import random

COLOR = ["red","blue"]

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        self.color(random.choice(COLOR))
        if self.pencolor() == "red":
            self.shapesize(1,1)
        else:
            self.shapesize(0.5,0.5)
        x_cor = random.randint(-270,270)
        y_cor = random.randint(-270,270)
        self.goto(x_cor,y_cor)

    

