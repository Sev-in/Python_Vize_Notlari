
n=0
while n<5:
    print(f"Sayı: {n}")
    n+=1

#Eğer while döngüsünün içerisinde sadece 1 satır komut varsa hepsini aynı satıra geçirebiliriz.
while n<10 : n+=1

for num in {1,2,3,4,5}:
    print(num)

# range[başlangıç değeri,bitiş değeri,aralık]
for i in range(1,10,2):
    print(i)

# İstenilen değer girilene kadar döner.
while (sayi:=int(input("Lütfen bir sayı giriniz:"))<0):
    print("Lütfen pozitif bir sayı giriniz!")


sayi=int(input("Lütfen bir sayı giriniz: "))
while True:
    if sayi<0:
        print("Lütfen pozitif bir sayı giriniz!")
        sayi=int(input("Lütfen bir sayı giriniz:"))
    else:
        break

while(sayi1:=input("Lütfen bir sayı giriniz: ")) and not sayi1.isdigit(): #isdigit() fonksiyonu dizenin sadece rakamlardan mı oluştuğunu kontrol eder.
    print("Geçersiz giriş. Lütfen sadece rakam giriniz!")

#break deyimi direkt döngünün sonlanmasına neden olur.
sayi2=input("Lütfen bir sayı giriniz: ")
while True:
    if not sayi2.isdigit():
        sayi2=input("Lütfen tekrar giriniz: ")
    else:
        break

#Sonsuz döngüye girdi çünkü hep sayi 0'a atandı.
# while sayi:=0<100:
#     if sayi==5:
#         break
#     else:
#         print(sayi)
#     sayi+=1

#5 sayısını ve ondan sonrakileri almaz çünkü döngüyü kırar.
sayi=0
while sayi<100:
    print(sayi)
    sayi+=1
    if sayi==5:
        break
else:
    print(f"Döngüden sonra sayi {sayi}\'dür")  #while ve for döngüleri için else kullanılabilir fakat break deyimi içeriyorsa kullanışlıdır.
#break deyimi yürütüldüğü için else yürütülmedi. Çünkü sayı hala 100den küçük kaldı.       
    
#Sadece 3'e tam bölünenleri almaz.
sayi=0
while sayi<10:
    sayi+=1
    if sayi%3==0:
        continue
    print(sayi)
else:
    print(f"Döngüden sonra sayi {sayi}\'dur") #Bu kısım çalıştı.

    