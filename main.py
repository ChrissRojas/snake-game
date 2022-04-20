from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def initialize_score():
    with open("hiscore.txt", mode="r") as file:
        return int(file.read())


def overwrite_file(score):
    with open("hiscore.txt", mode="w") as file:
        file.write(str(score))


snake = Snake()
food = Food()
scoreboard = Scoreboard(initialize_score())

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_head.distance(food) < 15:
        scoreboard.new_score()
        snake.extend_snake()
        food.new_position()
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        if scoreboard.check_hiscore():
            overwrite_file(scoreboard.score)
    for sq in snake.squares[1:]:
        if snake.snake_head.distance(sq) < 10:
            scoreboard.reset()
            snake.reset()
            if scoreboard.check_hiscore():
                overwrite_file(scoreboard.score)

screen.exitonclick()
