from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600,width=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

end = False

while not end:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        if food.pencolor() == "red":
            score.increase_score_red()
        else:
            score.increase_score_blue()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        end = True
        score.game_over()


    for segments in snake.total_turtle[1:]:
        if snake.head.distance(segments) < 10:
            end = True
            score.game_over()

screen.exitonclick()