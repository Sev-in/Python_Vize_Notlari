import turtle

def square(x,y,width,color):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()

square(0,0,100,"pink")

turtle.clear()

def circle(x,y,radius,color):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

circle(0,0,50,"yellow")

turtle.clear()

def line(start_x,start_y,color,end_x,end_y):
    turtle.hideturtle()
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(start_x,start_y)
    turtle.pendown()
    turtle.goto(end_x,end_y)
    
#ÇİZGİ FONKSİYONU İLE ÜÇGEN ÇİZİMİ
line(0,0,"green",100,0)
line(100,0,"pink",50,100)
line(50,100,"blue",0,0)

turtle.clear()

turtle.done()
