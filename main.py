# This is a Python project on concepts:
# Turtle module, Time module, Class inheritance, Random module, OOPS, Classes and Objects, Functions, Files

from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake GAme")
screen.tracer(0)
# Creating the objects.
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# Getting the key strokes form the keyboard.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:  # Condition to eat the food.
        food.refresh()
        snake.extend()
        scoreboard.increasescore()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # Condition for hitting the wall.
        scoreboard.reset()
        snake.reset()
        # is_game_on = False
        # scoreboard.game_over()

    for segments in snake.segments[1:]:  # Condition for hitting itself.
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()
            # is_game_on = False
            # scoreboard.gameover()

screen.exitonclick()  # To keep the screen running.
# If we want to end the game without re-running undo the code in comments.
