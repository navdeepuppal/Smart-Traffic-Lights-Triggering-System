from turtle import Turtle
import turtle
from turtle import Screen


def HeadText():
    turtle.color('black')
    style = ('Courier', 14,)
    turtle.speed(1000)
    turtle.penup()
    turtle.setposition(-198, 285)
    turtle.write('Side 1', font=style, align='center')
    turtle.penup()
    turtle.setposition(-48, 285)
    turtle.write('Side 2', font=style, align='center')
    turtle.penup()
    turtle.setposition(102, 285)
    turtle.write('Side 3', font=style, align='center')
    turtle.penup()
    turtle.setposition(252, 285)
    turtle.write('Side 4', font=style, align='center')
    turtle.setposition(-245, 140)
    turtle.write('Left ', font=style, align='center')
    turtle.penup()
    turtle.setposition(-260, 90)
    turtle.write('Straight ', font=style, align='center')
    turtle.penup()
    turtle.setposition(-250, 40)
    turtle.write('Right ', font=style, align='center')
    turtle.penup()
    turtle.hideturtle()


def Back():
    for i in range(0,4):
        pen9 = Turtle(shape='square')
        pen9.color('white')
        pen9.shapesize(12.65, 2.5)
        pen9.speed(100)
        pen9.color('grey')
        pen9.penup()
        pen9.sety(150)
        pen9.setx(-200+(i*150))

def Pole():
    for i in range(0, 4):
        pen9 = Turtle(shape='square')
        pen9.shapesize(9, 1)
        pen9.color('white')
        pen9.speed(100)
        pen9.penup()
        pen9.sety(-65)
        pen9.setx(-200+(i*150))
        pen9.color('grey')

def Base():
    for i in range(0, 4):
        pen9 = Turtle(shape='square')
        pen9.color('white')
        pen9.penup()
        pen9.speed(100)
        pen9.sety(-150)
        pen9.setx(-200+(i*150))
        pen9.shapesize(1, 2)
        pen9.color('grey')

    turtle.color('black')
    style = ('Courier', 14,)
    turtle.speed(1000)
    turtle.penup()
    turtle.setposition(-320, -207)
    turtle.write('Total Cars :', font=style, align='center')
    turtle.penup()
    turtle.setposition(-329, -227)
    turtle.write('Passing Cars :', font=style, align='center')
    turtle.penup()
    turtle.setposition(-297, -247)
    turtle.write('Time :', font=style, align='center')
    turtle.penup()

    turtle.hideturtle()

def Red(Num):
    i=Num-1
    pen1 = Turtle(shape='circle')
    pen1.color('white')
    pen1.speed(100)
    pen1.shapesize(2)
    pen1.color('red')
    pen1.penup()
    pen1.sety(250)
    pen1.setx(-200 + (i * 150))

    pen2 = Turtle(shape='circle')
    pen2.color('white')
    pen2.speed(100)
    pen2.shapesize(2)
    pen2.color('white')
    pen2.penup()
    pen2.sety(200)
    pen2.setx(-200 + (i * 150))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(165)
    pen3.shapesize(2)
    pen3.color('white')
    pen3.penup()
    pen3.sety(150)
    pen3.setx(-200 + (i * 150))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(165)
    pen3.shapesize(2)
    pen3.color('white')
    pen3.penup()
    pen3.sety(100)
    pen3.setx(-200 + (i * 150))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(165)
    pen3.shapesize(2)
    pen3.color('white')
    pen3.penup()
    pen3.sety(50)
    pen3.setx(-200 + (i * 150))

def Yellow(Num):
    i=Num-1
    pen1 = Turtle(shape='circle')
    pen1.color('white')
    pen1.speed(100)
    pen1.shapesize(2)
    pen1.color('white')
    pen1.penup()
    pen1.sety(250)
    pen1.setx(-200 + (i * 150))

    pen2 = Turtle(shape='circle')
    pen2.color('white')
    pen2.speed(100)
    pen2.shapesize(2)
    pen2.color('yellow')
    pen2.penup()
    pen2.sety(200)
    pen2.setx(-200 + (i * 150))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(165)
    pen3.shapesize(2)
    pen3.color('white')
    pen3.penup()
    pen3.sety(150)
    pen3.setx(-200 + (i * 150))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(165)
    pen3.shapesize(2)
    pen3.color('white')
    pen3.penup()
    pen3.sety(100)
    pen3.setx(-200 + (i * 150))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(165)
    pen3.shapesize(2)
    pen3.color('white')
    pen3.penup()
    pen3.sety(50)
    pen3.setx(-200 + (i * 150))

def GreenL(Num,TCars,PCars,Time):
    i=Num-1
    pen1 = Turtle(shape='circle')
    pen1.color('white')
    pen1.speed(100)
    pen1.shapesize(2)
    pen1.color('white')
    pen1.penup()
    pen1.sety(250)
    pen1.setx(-200 + (i * 150))

    pen2 = Turtle(shape='circle')
    pen2.color('white')
    pen2.speed(100)
    pen2.shapesize(2)
    pen2.color('white')
    pen2.penup()
    pen2.sety(200)
    pen2.setx(-200 + (i * 150))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(165)
    pen3.shapesize(2)
    pen3.color('green')
    pen3.penup()
    pen3.sety(150)
    pen3.setx(-200 + (i * 150))


    turtle.color('black')
    style = ('Courier', 14,)
    turtle.speed(1000)
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-207)
    pen3.setx(-230 + ((i) * 150))
    turtle.setposition(-230 + (i * 150), -207)
    turtle.write(TCars, font=style, align='center')
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-227)
    pen3.setx(-230 + ((i) * 150))
    turtle.setposition(-230 + (i * 150), -227)
    turtle.write(PCars, font=style, align='center')
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-247)
    pen3.setx(-230 + ((i) * 150))
    turtle.setposition(-230 + (i * 150), -247)
    turtle.write(Time, font=style, align='center')
    turtle.hideturtle()


def GreenM(Num,TCars,PCars,Time):
    i=Num-1
    pen1 = Turtle(shape='circle')
    pen1.color('white')
    pen1.speed(100)
    pen1.shapesize(2)
    pen1.color('white')
    pen1.penup()
    pen1.sety(250)
    pen1.setx(-200 + (i * 150))

    pen2 = Turtle(shape='circle')
    pen2.color('white')
    pen2.speed(100)
    pen2.shapesize(2)
    pen2.color('white')
    pen2.penup()
    pen2.sety(200)
    pen2.setx(-200 + (i * 150))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(165)
    pen3.shapesize(2)
    pen3.color('green')
    pen3.penup()
    pen3.sety(100)
    pen3.setx(-200 + (i * 150))

    turtle.color('black')
    style = ('Courier', 14,)
    turtle.speed(1000)
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-207)
    pen3.setx(-200 + ((i) * 150))
    turtle.setposition(-200 + (i * 150), -207)
    turtle.write(TCars, font=style, align='center')
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-227)
    pen3.setx(-200 + ((i) * 150))
    turtle.setposition(-200 + (i * 150), -227)
    turtle.write(PCars, font=style, align='center')
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-247)
    pen3.setx(-200 + ((i) * 150))
    turtle.setposition(-200 + (i * 150), -247)
    turtle.write(Time, font=style, align='center')
    turtle.hideturtle()

def GreenR(Num,TCars,PCars,Time):
    i=Num-1
    pen1 = Turtle(shape='circle')
    pen1.color('white')
    pen1.speed(100)
    pen1.shapesize(2)
    pen1.color('white')
    pen1.penup()
    pen1.sety(250)
    pen1.setx(-200 + (i * 150))

    pen2 = Turtle(shape='circle')
    pen2.color('white')
    pen2.speed(100)
    pen2.shapesize(2)
    pen2.color('white')
    pen2.penup()
    pen2.sety(200)
    pen2.setx(-200 + (i * 150))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(165)
    pen3.shapesize(2)
    pen3.color('green')
    pen3.penup()
    pen3.sety(50)
    pen3.setx(-200 + (i * 150))

    turtle.color('black')
    style = ('Courier', 14,)
    turtle.speed(1000)
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-207)
    pen3.setx(-170 + ((i) * 150))
    turtle.setposition(-170 + (i * 150), -207)
    turtle.write(TCars, font=style, align='center')
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-227)
    pen3.setx(-170 + ((i) * 150))
    turtle.setposition(-170 + (i * 150), -227)
    turtle.write(PCars, font=style, align='center')
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-247)
    pen3.setx(-170 + ((i) * 150))
    turtle.setposition(-170 + (i * 150), -247)
    turtle.write(Time, font=style, align='center')
    turtle.hideturtle()

def RightOff(Num):
    i=Num-1
    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(165)
    pen3.shapesize(2)
    pen3.color('white')
    pen3.penup()
    pen3.sety(50)
    pen3.setx(-200 + (i * 150))

def Reset():
    Yellow(1)
    Yellow(2)
    Yellow(3)
    Yellow(4)
'''
screen=Screen()
screen.setup(1000,1000)
Base()
Pole()
Back()
HeadText()
GreenR(1,12,12,123)
RightOff(1)
#Reset()
screen.mainloop()

'''

