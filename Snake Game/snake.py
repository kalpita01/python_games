from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.total_turtle = []
        self.create_snake()
        self.head = self.total_turtle[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)
    
    def add_segment(self,position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.total_turtle.append(tim)

    def extend(self):
        self.add_segment(self.total_turtle[-1].position())

    def move(self):
        for segment in range(len(self.total_turtle)-1,0,-1):
            new_x = self.total_turtle[segment-1].xcor()
            new_y = self.total_turtle[segment-1].ycor()
            self.total_turtle[segment].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)
    
