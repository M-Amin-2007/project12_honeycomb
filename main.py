"""write by: M. Amin"""
import turtle
pen = turtle.Pen()
screen = turtle.Screen()
def hexagon(side_length):
    """a function to draw a hexagon."""
    for side in range(6):
        pen.fd(side_length)
        pen.left(60)

screen.exitonclick()
