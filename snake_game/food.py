from turtle import Turtle
import random

class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(0.5,0.5)
        self.penup()
        self.new_position()

    def new_position(self):
        position_x=random.randint(-320,320)
        position_y=random.randint(-320,320)
        self.goto(position_x,position_y)


        
        
