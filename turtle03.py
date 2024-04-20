import turtle

#Kare oluşturur.
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.clear()

# Bir çokgenin iç açıları toplamı = (n-2)*180
for x in range(8):
    turtle.forward(25)
    turtle.right(45)

turtle.clear()

# dairelerin sayısı * açı = 360 olmalı kı desen tamamlanabilsin.
NUM_CIRCLES=12
RADIUS=100
ANGLE=30

for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.right(ANGLE)

turtle.clear()

# YILDIZ PATLAMASI

START_X= -200
START_Y= 0
NUM_LINES= 36
LINE_LENGTH= 400 
ANGLE= 170

turtle.hideturtle()
turtle.penup()
turtle.goto(START_X,START_Y)
turtle.pendown()

for x in range(NUM_LINES):
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)


turtle.done()