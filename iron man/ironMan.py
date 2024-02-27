# ibra-heeeem 
# a python turtle application, 
# drawing iron-man mask


import turtle

faceI = [
  [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),(-40, -20), (0, -20)],

  [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),(40, 120), (0, 120)]
]

faceII = [
  [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),(-80, -230), (-64, -210), (0, -210)],
  
  [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),(100, -46), (50, -40), (40, -30), (0, -30)]
]

faceIII = [
  [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),(0, -250)],
  
  [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),(0,-220)]
]


def draw(list, start):
    turtle.begin_fill()
    turtle.color("gold")
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()

    for i in range(len(list[0])):
        x, y = list [0][i]
        turtle.goto(x,y)

    for i in range(len(list[1])):
        x, y = list [1][i]
        turtle.goto(x,y)

    turtle.end_fill()


def main():
    turtle.hideturtle()
    turtle.bgcolor("red")
    turtle.setup(500,700)
    turtle.speed(5)


    faceI_Start = (0,120)
    faceII_Start = (0,-30)
    faceIII_Start = (0,-220)

    

    draw(faceI, faceI_Start)
    draw(faceII, faceII_Start)
    draw(faceIII, faceIII_Start)

    turtle.exitonclick()
main()
