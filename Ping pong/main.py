import turtle 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = turtle.Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

player_right = Paddle((350,0))
player_left = Paddle((-350,0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(player_right.move_up,"Up")
screen.onkey(player_right.move_down,"Down")
screen.onkey(player_left.move_up,"w")
screen.onkey(player_left.move_down,"s")

while True:
    time.sleep(ball.ball_speed)
    screen.update()
    
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.xcor() > 332 and ball.xcor() < 360 and player_right.distance(ball) < 70 or ball.xcor() < -332 and ball.xcor() > -360 and player_left.distance(ball) < 70:
        ball.speed("fastest")
        ball.bounce_x()
    
    # Right Paddle misses the ball
    if ball.xcor() > 390:
        ball.refresh()
        score.left_score()
    
    # Left Paddle misses the ball
    if ball.xcor() < -390:
        ball.refresh()
        score.right_score()
    




screen.exitonclick()