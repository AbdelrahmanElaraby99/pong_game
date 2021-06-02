from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed(0)
        self.goto(pos)

    def go_up(self):
        current_y = self.ycor()
        if current_y < 250:
            self.goto(self.xcor(), current_y+20)

    def go_down(self):
        current_y = self.ycor()
        if current_y > -240:
            self.goto(self.xcor(), current_y-20)
