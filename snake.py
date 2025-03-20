from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, snake_length):
        self.snake_segments = []
        self.snake_length = snake_length
        self.create_snake(self.snake_length)
        self.head = self.snake_segments[0]


    def create_snake(self, snake_length):
        for i in range(snake_length):
            self.add_segment(i)


    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.color("white")
        if isinstance(position, int):  # If called in create_snake
            x, y = position * -MOVE_DISTANCE, 0
        else:  # If called in extend_snake
            x, y = position

        snake_segment.goto(x, y)
        self.snake_segments.append(snake_segment)

    def extend_snake(self):
        self.add_segment(self.snake_segments[-1].position())



    def move(self):
        for segment_number in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_number - 1].xcor()
            new_y = self.snake_segments[segment_number - 1].ycor()
            self.snake_segments[segment_number].goto(new_x, new_y)

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


