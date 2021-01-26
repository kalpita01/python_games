from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
names = ["kalpita","arnav","prerna","papa","mummy","unknown"]

x_cor = -230
y_cor = [-100,-60,-20,20,60,100]
end = False
turtle_collection = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x_cor,y_cor[turtle_index])
    turtle_collection.append(new_turtle)

while not end:
    for turtle in turtle_collection:
        if turtle.xcor() > 230:
            end = True
            winner = turtle.pencolor()
            if user_bet.lower() == winner.lower():
                print("You Won")
            else:
                print("You lost")
            print(f"The {winner} won the race")
        num = random.randint(0,10)
        turtle.forward(num)

# A turtle is 40px wide in length and breath

screen.exitonclick()