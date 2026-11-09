from turtle import *
import time
bgcolor('black')
pencolor('red')
for i in range(6):
    begin_fill()
    end_fill()
    for i in range(4):        
        forward(100)
        left(90)
    right(60)
hideturtle()
time.sleep(5)  