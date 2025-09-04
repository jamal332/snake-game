from turtle import Screen
from snake import Snake
from food import Food
from scoerbard import Scoer_
import time

Window=Screen()
Window.setup(width=700,height=700)
Window.bgcolor('black')
Window.title('Snake Game')
Window.tracer(0)

food=Food()
sam=Snake()
scoer=Scoer_()

game_on=True

while game_on:

    sam.move()
    
#moveing:   
    Window.listen()

    Window.onkey(fun=sam.up,key="Up")
    Window.onkey(fun=sam.down,key="Down")
    Window.onkey(fun=sam.right,key="Right")
    Window.onkey(fun=sam.left,key="Left")

    Window.update()
    time.sleep(0.1)

    if sam.head.distance(food) < 15 :
        food.new_position()
        sam.extend()
        scoer.increase_scoer()

    for piece in sam.turtles[:-1]:
        if sam.head.distance(piece) < 10:
            
            scoer.game_over()
            Window.update()
            game_on=False

    if sam.head.xcor() > 330 or sam.head.xcor() < -330 or sam.  head.ycor() > 330 or sam.head.ycor() < -330 :

        scoer.game_over()
        Window.update()
        game_on=False

Window.exitonclick()  