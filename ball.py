from turtle import Turtle


class Ball(Turtle):
    """_summary_

    Args:
        Turtle (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.color("purple")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Function that makes the ball bounce when it hits the wall
        """
        
        self.y_move = self.y_move * -1

    def bounce_x(self):
        """Function that makes the ball bounce when it hits the paddle
        """
        self.x_move = self.x_move * -1
        self.move_speed = self.move_speed * 0.9
    def reset_position(self):
        """Function that resets the position of the ball
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

