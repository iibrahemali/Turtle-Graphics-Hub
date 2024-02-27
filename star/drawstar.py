import sys
import turtle
import time

def drawStar(t, num_sides, side_length):
    for _ in range(num_sides):
        t.forward(side_length)
        t.left(120)
        t.forward(side_length)
        t.right(180-(60+(360/num_sides)))
  

def main():
    window = turtle.Screen()
    window.setup(600, 600)
    t = turtle.Turtle()
    t.speed(3)
    
    num_sides=int(sys.argv[1])
    side_length=int(sys.argv[2])
    
    drawStar(t,num_sides,side_length)
    time.sleep(1)
    turtle.exitonclick()
main()