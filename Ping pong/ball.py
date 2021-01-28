from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_distance = 10
        self.y_distance = 10
        self.ball_speed = 0.08

    def move(self):
        self.setx(self.xcor() + self.x_distance)
        self.sety(self.ycor() + self.y_distance)

    def bounce_y(self):
        self.y_distance *= -1
        
    def bounce_x(self):
        self.x_distance *= -1
        self.ball_speed *= 0.9
        
    def refresh(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed = 0.08

    


    
