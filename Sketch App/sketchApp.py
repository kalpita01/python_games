from turtle import Turtle, Screen

kalpita = Turtle()

def move_forward():
    kalpita.fd(10)

def move_backward():
    kalpita.bk(10)

def counter_clockwise():
    kalpita.lt(10)

def clockwise():
    kalpita.rt(10)

def clear_screen():
    kalpita.clear()
    kalpita.penup()
    kalpita.home()
    kalpita.pendown()
    

screen = Screen()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(counter_clockwise,"a")
screen.onkey(clockwise,"d")
screen.onkey(clear_screen,"c")

screen.exitonclick()