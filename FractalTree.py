import turtle 

def draw_branch(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15, t)
        t.left(40)
        draw_branch(branch_length-15, t)
        t.right(20)
        t.backward(branch_length)
        
screen = turtle.Screen()
screen.bgcolor("black")

turtle.speed(0)
turtle.color("green")
turtle.left(90)
turtle.up()
turtle.backward(200)
turtle.down()

draw_branch(100, turtle)

turtle.hideturtle()
turtle.exitonclick()