import sys
import time
import turtle

def main():
    # setup the window and the turtle
    window = turtle.Screen()
    window.setup(600, 600)
    window.bgcolor("black")
    t = turtle.Turtle()

    # get input from the user
    num_squares = int(sys.argv[1])
    side_length = int(sys.argv[2])

    # draw the flower
    angle = 360 // num_squares

    for _ in range(num_squares):
        for colors in ["grey"]:
            t.color(colors)
            t.left(angle)
        for _ in range(4):
            t.forward(side_length)
            t.left(90)

    time.sleep(1)
    turtle.exitonclick()
main()