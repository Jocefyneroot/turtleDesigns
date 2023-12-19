import turtle
import random


def fractal_tree(branch_len, t, width):
    if branch_len > 5 and width > 0:
        # Draw the main branch
        t.pensize(width)
        t.forward(branch_len)

        # Right branch
        t.right(20)
        fractal_tree(branch_len - 15, t, width - 1)

        # Left branch
        t.left(40)
        fractal_tree(branch_len - 15, t, width - 1)

        # Retreat to the original position
        t.right(20)
        t.backward(branch_len)


def random_color():
    return random.uniform(0.4, 0.8), random.uniform(0.4, 0.8), random.uniform(0.1, 0.5)


def main():
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.color(random_color())
    turtle.width(5)
    turtle.left(90)  # Start by facing upwards

    fractal_tree(100, turtle, 5)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
