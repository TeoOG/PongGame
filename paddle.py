from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, starting_x, starting_y, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        # Original is 20x20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_x, starting_y)

    def move_up(self):
        get_x_cor = self.xcor()
        get_y_cor = self.ycor()
        self.goto(get_x_cor, get_y_cor + MOVE_DISTANCE)

    def move_down(self):
        get_x_cor = self.xcor()
        get_y_cor = self.ycor()
        self.goto(get_x_cor, get_y_cor - MOVE_DISTANCE)
