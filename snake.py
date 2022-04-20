from turtle import Turtle


class Snake:
    def __init__(self):
        self.start_pos = [(0, 0), (-20, 0), (-40, 0)]
        self.UP = 90
        self.DOWN = 270
        self.RIGHT = 0
        self.LEFT = 180
        self.squares = []
        self.create_snake()
        self.snake_head = self.squares[0]

    def create_snake(self):
        for pos in self.start_pos:
            self.add_square(pos)

    def move(self):
        for sq in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[sq - 1].xcor()
            new_y = self.squares[sq - 1].ycor()
            self.squares[sq].goto(new_x, new_y)
        self.snake_head.forward(20)

    def add_square(self,position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def reset(self):
        for sq in self.squares:
            sq.hideturtle()

        self.squares = []
        self.create_snake()
        self.snake_head = self.squares[0]

    def extend_snake(self):
        self.add_square(self.squares[-1].position())

    def up(self):
        if self.snake_head.heading() != self.DOWN:
            self.snake_head.setheading(self.UP)

    def left(self):
        if self.snake_head.heading() != self.RIGHT:
            self.snake_head.setheading(self.LEFT)

    def right(self):
        if self.snake_head.heading() != self.LEFT:
            self.snake_head.setheading(self.RIGHT)

    def down(self):
        if self.snake_head.heading() != self.UP:
            self.snake_head.setheading(self.DOWN)
