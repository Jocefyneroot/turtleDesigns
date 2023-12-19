import turtle

screen  =  turtle.Screen()
screen.bgcolor("black")

turtle.speed(0)
turtle.color("cyan")

for i in range(100):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.right(10)
    
turtle.hideturtle()
turtle.exitonclick()