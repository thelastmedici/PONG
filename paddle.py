from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        """"Initialize the paddle class"""
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        """ Function that goes tells paddle to go up"""
        y = self.ycor()
        y = y + 20
        self.goto(self.xcor(), y)

    def go_down(self):
        """A fuunction that brings the paddle down"""
        x = self.ycor()
        x = x - 20
        self.goto(self.xcor(), x)
