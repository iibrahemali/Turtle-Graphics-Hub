from turtle import * 

def backFrame():
    COLOR = (0.60156, 0, 0.99218)  # (154, 0, 254)
    TARGET = (0.86328, 0.47656, 0.31250)  # (221, 122, 80)

    screen = Screen()
    screen.tracer(False)

    WIDTH, HEIGHT = screen.window_width(), screen.window_height()
    deltas = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]

    turtle = Turtle()
    turtle.color(COLOR)

    turtle.penup()
    turtle.goto(-WIDTH/2, HEIGHT/2)
    turtle.pendown()

    direction = 1

    for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):

        turtle.forward(WIDTH * direction)
        turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
        turtle.sety(y)

        direction *= -1

    screen.tracer(True)

def main():
    pen_color = 'white'
    width_val = 23
    round_coordA, round_coordB = 34, 90
    circleAx, circleAy = 80, 360
    circleBx, circleBy = 7, 360
    gotoAx, gotoAy = 85, 30
    gotoBx, gotoBy = 160, -100

    pencolor(pen_color) 
    width(width_val) 
    penup() 
    goto(gotoBx, gotoBy) 
    pendown() 

    left(90) 
    for i in range(4):
        forward(250)
        circle(round_coordA, round_coordB) 

    penup() 
    goto(gotoAx, gotoAy) 
    pendown() 
    circle(circleAx, circleAy) 

    penup()
    goto(110,130) 
    pendown()
    circle(circleBx, circleBy)
    hideturtle() 
    exitonclick()

if __name__ == "__main__":
    backFrame()
    main()