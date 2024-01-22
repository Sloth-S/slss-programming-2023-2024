from turtle import *
def tree(deep,lenth):
    if(deep>0):
        forward(lenth)
        left(36)
        tree(deep-1,lenth/1.61)
        right(36)
        
        right(36)
        tree(deep-1,lenth/1.61)
        left(36)
        backward(lenth)
    else:
        color("green")
        dot(lenth/3)
        color("black")

left(90)
speed(10)
color("white")
backward(500)
color("black")
showturtle()
tree(6,300)
