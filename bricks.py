from turtle import Turtle

class Brick(Turtle):
    def __init__(self, color, width, height):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=width / 20)
        self.width = width
        self.height = height

    def set_position(self, x, y):
        self.goto(x, y)

    def clear(self):
        self.goto(2000, 2000)

