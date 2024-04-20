import random
import math

#HİYERARŞİK FONKSİYON
#Yani bir fonksiyon içerisinde tanımlanmış bir fonksiyonu çağırabiliyorsun.
#Boş fonksiyonlar oluşturabilmek için pass anahtar sözcüğünü kullanabiliriz.
def main():
    get_input()
    calc_guess_pay()
    calc_overtime()
    calc_with_holdings()
    son_fonk()
def get_input():
    get_hours_worked()
    get_hours_rate()
def get_hours_worked():
    pass
def get_hours_rate():
    pass
def calc_guess_pay():
    pass
def calc_overtime():
    pass
def calc_with_holdings():
    calc_texas()
    calc_benefits()
def calc_texas():
    pass
def calc_benefits():
    pass
def son_fonk():
    pass

def main():
    sayi=5
    show_double(sayi)
    show_sum(6,7)
    change_me(sayi) # "0" oldu.
    print(sayi) # (5 )sayi değişkeninin normal hali değişmedi sadece fonksiyon içerisinde yazıldığında değişmiş oldu.

    toplami_goster(a=5,b=4,c=7,d=4) #fonksiyonda parametlerin başına "*" koyduğumuz için parametreye değişkenlerini tanımlayarak yazmalıyız.
    carpmayi_goster(5,6,c=7,d=2) #fonksiyonu tanımlarken yıldızı c'nin önüne koyduğumuz için sadece c ve d değişkenlerini tanımlayarak yazmak durumunda kaldık.
    toplami_goster2(4,5,6,7) # fonksiyon parametresinin sonuna "/" koyduğumuz için tanımlamadık.
    carpmayi_goster2(7,8,c=5,d=2) #c den önce "/" koyduğumuz için eğer c ya da d'yi tanımlarsak ikisini birden tanımlamak zorundayız.
    carpmayi_goster2(7,8,5,2) #bu şekilde de çalışır.

    show_tax(4,0.08)
    show_tax(4) #istersem ikinci parametreyi vermeyebilirim çünkü o zaten tanımlanmış.

    #1 ve 100 dahil
    number=random.randint(1,100) #random kütüphanesiyle yazdık. 1 ile 100 arasında int değerinde rastgele bir sayı döndürür.
    print(number)

    #1 dahil 100 değil
    number=random.randrange(1,100) #random tam sayı döndürür.
    print(number)

    number=random.random() # 1 ile 0 arasında rastgele float değerinde bir sayı döndürür.
    print(number)

    number= random.uniform(1,10) # random ile aynı sadece aralık belirtme imkanı sunar.
    print(number)

    # Rastgele bir sayı ürettikten sonra hep o sayı devam eder.
    random.seed(20)
    number=random.randint(1,100)
    print(number)

    print(get_name()) #return ile yazıldığı için printle yazdırabiliriz.

    print(divide(10,0))

    print(math.acos(0.5)) # ark kosinüsü radyan cinsinden verir.
    print(math.asin(0.5))
    print(math.atan(0.5))
    print(math.cos(0.5))
    print(math.sin(0.5))
    print(math.tan(0.5))

    print(math.degrees(math.sin(0.5))) #radyan cinsinden açıyı dereceye çevirir.
    print(math.radians(math.degrees(math.sin(0.5)))) #derece cinsinden açıyı radyana çevirir.

    print(math.exp(1)) # e**1 döndürür. 
    print(math.sqrt(25)) # Karekökünü alır.

    print(math.ceil(10.1)) # x ten büyük veya eşit olan en küçük tam sayıyı döndürür. (11)
    print(math.floor(10.1)) # x ten küçük veya eşit olan en büçük tam sayıyı döndürür. (10)

    print(math.hypot(3,4)) # hipotenüsü verir. (5)

    print(math.log(100)) #doğal logaritmayı verir.
    print(math.log2(16)) #tabanlı logaritmayı verir.

    print(daire_alanı:= math.pi * (radius:=3 **2))




#IPO(input-processing-output) grafiği fonksiyon oluşturmayı kolaylaştırabilir.

def show_double(value):
    sonuc = value * 2
    print(sonuc)

def show_sum(sayi1,sayi2):
    sonuc= sayi1+sayi2
    print(sonuc)

def change_me(arg):
    print("I'm changing!")
    arg=0
    print(f"Yeni hali: {arg}")

def toplami_goster(*,a,b,c,d):
    print(a+b+c+d)

def carpmayi_goster(a,b,*,c,d):
    print(a*b*c*d)

def toplami_goster2(a,b,c,d,/):
    print(a+b+c+d)

def carpmayi_goster2(a,b,/,c,d):
    print(a*b*c*d)

def show_tax(price,tax_rice=0.07):
    tax = tax_rice * price
    print(f"The tax is {tax}")

def get_name():
    name= input("Lütfen isminizi giriniz: ")
    return name

def divide(sayi1,sayi2):
    if sayi2==0:
        sonuc= None #Hiçbir değer döndürmesini istemiyorsak None yazabiliriz.
    else:
        sonuc=sayi1/sayi2
    return sonuc



main()




# A MARKA KURUTMA MAKİNESİ MİNİ PROJE

def main0():
    startup_message()
    input("1.adımı görmek için Enter tuşuna basınız: ")
    adim_1()
    input("2.adımı görmek için Enter tuşuna basınız: ")
    adim_2()
    input("3.adımı görmek için Enter tuşuna basınız: ")
    adim_3()
    input("Son adımı görmek için Enter tuşuna basınız: ")
    adim_4()

def startup_message():
    print("İşlem 4 aşamadan oluşur.")
def adim_1():
    print("...")
def adim_2():
    print("...")
def adim_3():
    print("...")
def adim_4():
    print("...")

main0()



def sayilari_goster():
    print(f"Girdiğiniz sayı: {sayi5}'dır.")

def main1():
    global sayi5  #bir fonksiyon içinde tanımlanan bir değişkenin global kapsamda olduğunu belirtmek için kullanılır.
    sayi5= input("Bir sayı giriniz: ")
    sayilari_goster()

main1()