from turtle import *
from random import *

X = window_width() // 2
Y = window_height() // 2
pensize(2)

while 1:
    LIM = 30
    reset()
    hideturtle()
    while LIM:
        speed(10)
        penup()
        DOT1 = (randint(-X,X+1), randint(-Y,Y+1))
        DOT2 = (randint(-X,X+1), randint(-Y,Y+1))
        DOT3 = (randint(-X,X+1), randint(-Y,Y+1))
        AREA = ((DOT1[0]-DOT3[0])*(DOT2[1]-DOT3[1]) - (DOT2[0]-DOT3[0])*(DOT1[1]-DOT3[1]))/2
        if AREA < 2000:
            continue
        else:
            goto(DOT1)
            COL = (random(), random(), random())
            color((COL), (COL))
            speed(3)
            pendown()
            begin_fill()
            goto(DOT2)
            goto(DOT3)
            goto(DOT1)
            end_fill()
        LIM -= 1
