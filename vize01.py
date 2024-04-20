print('Merhaba Dünya')

print('Ödevin yarına kadar "Hamlet"i okumak') #Alıntılama

para=100
print("Şevin\'in hesabında ", para ,"tl var.")

x,y,z = 1,2,3
print(x,y,z)

kullanici_girisi = int(input("Lutfen bir sayi giriniz: "))
print(kullanici_girisi)

puan = float(input("Lütfen puan giriniz:"))
print(puan)

x = 25.2 // 5 #Tam sayıyı veren bölme 
print(x)

y= 25.2 % 5 #Kalanı veren bölme
print(y)

#Alt satıra geçişi sağlar(\)
sonuc = x*2+\
        y+5
print(sonuc)

#Parantez içine alındıysa "\"" buna gerek kalmaz.
sonuc =(x*2+
        y+5)
print(sonuc)

print("Merhaba"+" Dünya") #Merhaba Dünya

my_str = 'bir ' 'iki ' 'üç'
print(my_str)  #bir iki üç

yeni_cümle= "RGB: \n kırmızı \n yeşil \n mavidir." # "\n" alt satıra geçmeyi sağlar.
print(yeni_cümle)

yeni_cümle1= "Bu özellik: \t Bir \t tab \t kadar boşluk bırakır."
print(yeni_cümle1)

ad = "Şevin"
print(f"Merhaba {ad}") 

value =5
print(f"5+2= {value + 2}")
print(f"5+2= {5+2}")


 # [hizalama] [genişlik] [,] [.hassasiyet] [tür]
num= 12546546.65445487
print(f"{num:.2f}")  #12546546.65
print(f"Sayı: {num:,.2f}") #Sayı: 12,546,546.65
print(f"Sayı: {num:20,.2f}") # 20 boşluk bırakır.
print(f"Sayı: {num:<20.2f}") #Sola hizalama
print(f"Sayı: {num:>20.2f}") #Sağa hizalama
print(f"Sayı: {num:^20.2f}") #Orta hizalama
print(f"{num:,e}") #1.254655e+07

num1=646465
print(f"{num1:,d}") #646,465
print(f"{num1:,e}") #6.464650e+05


#ZAMAN DÖNÜŞTÜRÜCÜ

toplam_saniye = float(input("Lütfen saniye değeri giriniz: "))

saat = toplam_saniye // 3600
dakika = (toplam_saniye // 60) % 60
saniye = toplam_saniye % 60 

print(int(saat), "sa" , int(dakika) , "dk", int(saniye), "sn")

#KOLONLARDA GÖSTERME
sayi1 = 4654.546
sayi2 = 54654.545
sayi3 = 5685.45
sayi4 = 7879.87
sayi5 = 8798.9861
sayi6 = 78798.867665

print(f"{sayi1:10.2f}{sayi2:10.2f}")
print(f"{sayi3:10.2f}{sayi4:10.2f}")
print(f"{sayi5:10.2f}{sayi6:10.2f}")

#    4654.55  54654.54
#    5685.45   7879.87
#    8798.99  78798.87

#ORTAYA HİZALAMA
isim1 = "Şevin"
isim2 = "Lale"
isim3 = "Ahmet"
isim4 = "Gül"

print(f"*****{isim1:^10}*****")
print(f"*****{isim2:^10}*****")
print(f"*****{isim3:^10}*****")
print(f"*****{isim4:^10}*****")

# *****  Şevin   *****
# *****   Lale   *****
# *****  Ahmet   *****
# *****   Gül    *****









