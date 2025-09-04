from turtle import Turtle

class Snake():

    def __init__(self):
        self.positions=[(-40,0),(-20,0),(0,0),(20,0),(40,0)]
        self.turtles=[]
        self.create_turtle()
        self.head=self.turtles[-1]

    def create_turtle(self):
        
        for i in range(len(self.positions)):
            sam=Turtle('square')
            sam.color('white')
            sam.penup()
            sam.goto(self.positions[i])
            self.turtles.append(sam)

    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20)

    def extend(self):
        new_turtle=Turtle()
        new_turtle.shape('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(self.positions[0])
        self.turtles.insert(0,new_turtle)

    def right(self):
        self.head.setheading(0)

    def up(self):
        self.head.setheading(90)

    def left(self):
        self.head.setheading(180)

    def down(self):
        self.head.setheading(270)

