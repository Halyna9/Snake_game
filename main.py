""" This is my version of the famous Snake Game.

"""

# importing modules
from turtle import Turtle, Screen
from snake import Snake
import random
import time

# setting up the screen size, background color and title
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# creating a snake object from Snake class
snake = Snake()

# using screen methods to control snake movements
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True 

while game_is_on:
    # refreshing the screen to make sure visual moving of the snake is user friendly 
    screen.update()
    time.sleep(0.3)  

    snake.move()


screen.exitonclick()