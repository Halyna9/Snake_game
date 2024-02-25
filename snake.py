from turtle import Turtle, Screen

# constant/global values
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


#creating a Snake class
class Snake:

    # snake attributes
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    # snake methods
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_snake_part = Turtle("square")
            new_snake_part.penup()
            new_snake_part.color("white")   
            new_snake_part.goto(position)
            self.snake_parts.append(new_snake_part)

    def move(self):
        # make sure all snake parts are moving together, following the first segment
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
            