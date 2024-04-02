from turtle import Turtle

class Scoreboard(Turtle):
    """Class that creates the scoreboard

    Args:
        Turtle (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        """Function that updates the scoreboard"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        
    def l_point(self):
        """a function that adds a point to the left side of the scoreboard
        """
        self.l_score += 1
        self.update_scoreboard()
        
    def r_point(self):
        """A function that adds a point to the right side of the scoreboard"""
        self.r_score += 1
        self.update_scoreboard()
        