import turtle


def draw_flower():
    turtle.color("red")
    turtle.begin_fill()

    for _ in range(36):
        turtle.forward(50)
        turtle.right(45)
        turtle.forward(50)
        turtle.right(135)
        turtle.forward(50)
        turtle.right(45)
        turtle.forward(50)
        turtle.right(135)

        turtle.right(10)

    turtle.end_fill()


def draw_flower_field(num_flowers):
    for _ in range(num_flowers):
        draw_flower()
        turtle.penup()
        turtle.goto(turtle.xcor() + 120, turtle.ycor())
        turtle.pendown()


def main():
    turtle.speed(2)
    turtle.hideturtle()
    draw_flower_field(3)  # You can adjust the number of flowers

    turtle.done()


if __name__ == "__main__":
    main()
