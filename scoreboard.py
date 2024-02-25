"""This module create and manage the scoreboard behavior.
"""

from turtle import Turtle

class Scoreboard(Turtle):
    """Creating subclass Scoreboard from super class Turtle,
    which will inherit behavior of Turtle class and will get extra 
    functionality.
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, -270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """This function is rewriting the score and display it on the screen.
        """
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        """This function displays the game over
        message for the player.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """This function will keep track on the score, increasing
        it by 1 each time the Snake collided with food.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()


