import turtle

# #KAPLUMBAĞANIN DURUMUNUN BELİRLENMESİ

# if turtle.ycor() <0: # y koordinatlarını verir = turtle.ycor()
#     turtle.goto(0,0)
# if turtle.xcor()>100 and turtle.xcor()<200: # x koordinatlarını verir = turtle.xcor()
#     turtle.goto(0,0)

# if turtle.heading()>90 and turtle.heading<270: # turtle.heading() kaplumbağanın yönünü(derecesini) verir.
#     turtle.setheading(180)

# if turtle.isdown(): # Kalem aşağıda mı? diye sorar aşağıdaysa true değilse false döndürür.
#     turtle.penup()

# if not(turtle.isdown()):
#     turtle.pendown()

# if turtle.isvisible(): # Kaplumbağa görünürse true görünmezse false döndürür.
#     turtle.hideturtle()

# if turtle.pencolor()=="red":
#     turtle.pencolor("pink")

# if turtle.fillcolor()=="yellow":
#     turtle.fillcolor("green")

# if turtle.bgcolor()=="white":
#     turtle.bgcolor("yellow")

# if turtle.pensize()<3:
#     turtle.pensize(3)

# if turtle.speed()>0:
#     turtle.speed(0)


#HEDEF OYUNU VUR
#adlandırılmış sabitler
EKRAN_GENISLIGI=600
EKRAN_YUKSEKLIGI=600
Hedef_sol_alt_X=100
Hedef_sol_alt_Y=250
HEDEF_GENISLIGI=25

KUVVET_FAKTORU=30
MERMI_ANIMASYON_HIZI=1
KUZEY=90
GUNEY=270
DOGU=0
BATI=180

#pencereyi kurun
turtle.setup(EKRAN_GENISLIGI,EKRAN_YUKSEKLIGI)

#hedefi çizin
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(Hedef_sol_alt_X,Hedef_sol_alt_Y)
turtle.pendown()
turtle.setheading(DOGU)
turtle.forward(HEDEF_GENISLIGI)
turtle.setheading(KUZEY)
turtle.forward(HEDEF_GENISLIGI)
turtle.setheading(BATI)
turtle.forward(HEDEF_GENISLIGI)
turtle.setheading(GUNEY)
turtle.forward(HEDEF_GENISLIGI)
turtle.penup()

#kaplumbağayı ortala
turtle.goto(0,0)
turtle.setheading(DOGU)

turtle.speed(MERMI_ANIMASYON_HIZI)

#kullanıcıdan açıyı ve kuvveti alın
# aci= float(input("Merminin açısını giriniz: "))
aci= turtle.numinput("Açı","Merminin açısını giriniz: ")
# kuvvet= float(input("Fırlatma kuvvetini giriniz(1-10):"))
kuvvet= turtle.numinput("Kuvvet","Fırlatma kuvvetini giriniz(1-10):")

#mesafeyi hesaplayın
mesafe= kuvvet*KUVVET_FAKTORU

#başlığı ayarlayın
turtle.setheading(aci)

#mermiyi fırlat
turtle.pendown()
turtle.forward(mesafe)

#hedefi vurdu mu?
if (turtle.xcor()>=Hedef_sol_alt_X and turtle.xcor()<=(Hedef_sol_alt_X+HEDEF_GENISLIGI) and turtle.ycor()>=Hedef_sol_alt_Y and turtle.ycor()<=(Hedef_sol_alt_Y+HEDEF_GENISLIGI)):
    print("Atış başarılı!")
else:
    print("Tekrar deneyiniz!")

#açı=66, kuvvet=10, atış başarılı!



turtle.done()
