from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):
    """Class responsible for keeping the score and printing it"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """refresh the screen writing"""
        self.clear()
        self.write(f"{self.l_score}   {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        """increments the left score"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """increments the right score"""
        self.r_score += 1
        self.update_scoreboard()
