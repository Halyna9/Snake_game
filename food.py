"""This module generate and manage 
the food behavior.
"""

from turtle import Turtle
import random

class Food(Turtle):
    """Creating subclass Food from super class Turtle,
    which will inherit behavior of Turtle class and will get extra 
    functionality.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5 ,stretch_wid = 0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """This function will refresh a new location of food on 
        the screen.
        """
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
