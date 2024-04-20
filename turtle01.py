import turtle

turtle.hideturtle() # Kaplumbağa simgesini gizler.
turtle.pensize(4) # Kalem boyutu
turtle.pencolor("red") # Kalem rengi 
turtle.bgcolor("yellow") # Arkaplan rengini ayarlar.
turtle.setup(640,600) # Ekranın genişlik ve yüksekliğini ayarlar.
turtle.speed(1) # 0-10 arasında. 0 olursa hareketleri anında yapar.

#Kaplumbağanın ilk yönü doğudur.(0. derece)
turtle.forward(100) # 100 birim ilerler

turtle.left(90) # 90 derece sola döner.
turtle.forward(100)
turtle.right(90) # 90 derece sağa döner.
turtle.forward(100)

turtle.setheading(90) # Açıyı direkt koordinatlara göre belirler. 90 derece yukarı 180 sol gibi...
turtle.forward(100)

turtle.clear()
turtle.setheading(180)

# Kesikli çizgi olur.
turtle.penup() # Kalemi kaldırır.
turtle.forward(20)
turtle.pendown() # Kalemi indirir.
turtle.forward(20)

turtle.clear()

# Daire çizer.
turtle.circle(50)

turtle.clear()

# Noktalı çizgi çizer.
turtle.forward(20)
turtle.dot() # Nokta çizer.
turtle.forward(20)
turtle.dot()
turtle.forward(20)

turtle.clear()

# Turtle kartezyen koordinatları kullanır.
turtle.goto(45,45) # (x=45,y=45) koordinatlarına gider.
turtle.write("Bu öğretici bir çizimdir.") # x ve y koordinatları yazının sol alt köşesidir.

turtle.clear()

#Şekli bir renkle doldurmak için
turtle.fillcolor("pink") #Şeklin rengini belirlerken
turtle.begin_fill() #Şekli çizmeden önce
turtle.circle(25)
turtle.end_fill() #Şekli çizdikten sonra

#Girdiler
age = turtle.numinput('Input', 'Your Age: ', default =10, minval = 0, maxval = 100) # min değeri 0, max değeri 100
name = turtle.textinput('Input', 'Your Name: ') 

# Çizimi sıfırlar. Arkaplan rengini sıfırlamaz.
#turtle.reset()

# Çizim ayarları sabit kalır sadece ekrandakiler silinir.
#turtle.clear()

# Çizimi sıfırlar. Arkaplan dahil.
#turtle.clearscreen()
turtle.done()