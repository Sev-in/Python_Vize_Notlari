puan = 70
odev= 82
if puan > 45 : print("Geçtin!")

if 'mary'>'mark' : print("mary ascii karakter kodlamasında daha büyük")

# and operatörü için yanlış olması daha muhtemel olan durum başta olmalı. (İşlem kolaylığı için)
if puan>65 and puan<90 : print("Başarılı!")

# or operatörü için doğru olması daha muhtemel olan durum başta olmalı. (İşlem kolaylığı için)
if puan>60 or odev>85 : print("Başarılı!")


not1 = 'Geçti' if puan > 59 else 'Kaldi'

if puan>59:
    not1='Geçti'
else:
    not1='Kaldı'


#Max değer bulma
num1=5
num2=7
max = num1 if num1>num2 else num2
print(max)

if num1>num2:
    max=num1
else:
    max=num2
print(max)


#Walrus(mors) operatörü en düşük önceliğe sahiptir.
#num:=99 yanlıştır daha büyük bir ifadenin parçası olarak yazılmalı.
print(mors:=9) #Bu ifade ":=" hem 9 ataması yapar hem de 9'u yazdırır.

genislik=20
yukseklik=6
if(alan:= genislik*yukseklik) >100:
    print("Alan çok büyük")

#ŞİFRE DOĞRULAMA
sifre=int(input("Şifrenizi giriniz:"))
if sifre== 12345:
    print('Başarıyla giriş yapıldı!')
else:
    print('Üzgünüm şifre yanlış. Lütfen tekrar deneyiniz!')

#İSİMLERİ SIRALAMA
isim1=input("Bir isim giriniz: ")
isim2=input("Bir isim daha giriniz: ")
if isim1>isim2:
    print(isim1)
    print(isim2)
else:
    print(isim2)
    print(isim1)
