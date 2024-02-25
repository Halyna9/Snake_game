"""This module creates and manage behavior of the Snake
"""

from turtle import Turtle

# constant/global values
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    """Creating a Snake class"""

    # snake attributes
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    # snake methods
    def create_snake(self):
        """Creating a starting snake"""
        for position in STARTING_POSITIONS:
            self.add_part(position)
            
    def add_part(self, position):
        """This function adds a new part to the snake body"""
        new_snake_part = Turtle("square")
        new_snake_part.penup()
        new_snake_part.color("white")   
        new_snake_part.goto(position)
        self.snake_parts.append(new_snake_part)

    def extend(self):
        """This function attach a new part to the snake."""
        self.add_part(self.snake_parts[-1].position())

    def move(self):
        """ Make sure all snake parts are moving together, following the first segment"""
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            