import math
import turtle

def pythagoras_tree(t: turtle, depth: int, length: float):
    if depth == 0:
        return
    else:
        t.pendown()

        t.left(45)
        child_length = length * math.cos(math.radians(45))
        t.forward(child_length)

        # draw left
        pythagoras_tree(t, depth - 1, child_length)

        t.penup()
        t.backward(child_length)

        t.left(-90)
        t.pendown()
        t.forward(child_length)

        # draw right
        pythagoras_tree(t, depth - 1, child_length)

        t.penup()
        t.backward(child_length)
        t.left(45)



def draw_pythagoras_tree(depth = 6, length = 100.0):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    t.forward(length)

    pythagoras_tree(t, depth, length)

    t.hideturtle()
    window.mainloop()


draw_pythagoras_tree()