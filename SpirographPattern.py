import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

turtle.speed(0)
turtle.color("magenta")

for _ in range(72):
    turtle.forward(150)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(150)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.right(5)

turtle.hideturtle()
screen.exitonclick()
