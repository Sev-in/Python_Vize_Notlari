list=["Şevin",4,True] #Her tipten öge tutabilir.
print(list[2]) #True

list1 = list * 2
print(list1) # ['Şevin', 4, True, 'Şevin', 4, True]

# Tek tek listedeki elemanları dolaşır ve yazdırır.
for x in list:
    print(x)

size = len(list) #listenin uzunluğunu verir.

#Listeler değişebilir!
list[1]="Ahmet"
print(list) #['Şevin', 'Ahmet', True]

my_list= [4,5,6]

#Listeler birleştirilebilir!
list_plus= my_list+list
print(list_plus)

#Liste dilimleme
#list[start:end]
#Başlangıç belirtilmezse 0 kullanılır.
#Bitiş belirtilmezse len(list) kullanılır.
print(list_plus[0:3]) #0,1,2. indexleri alır. ([4,5,6])

print("Şevin" in list_plus) #listede aradığımız öge var mı diye kontrol eder. True ya da False döndürür.

print(list.index("Şevin"))  #(0) Şevin'in kaçıncı indexte olduğunu yazar.
print(list1.count("Şevin")) #(2) listede kaç tane Şevin olduğunu yazar.

list.append("Lale") #Listenin sonuna yeni öge ekler.
print(list)  #['Şevin', 'Ahmet', True, 'Lale']
list.remove("Lale") #Listeden seçtiğimiz ögeyi siler.
print(list) #['Şevin', 'Ahmet', True]

my_list1= [5,9,6]
my_list1.sort()  #Listeyi küçükten büyüğe doğru sıralar.
print(my_list1)  # ([5,6,9])

my_list1.reverse() #Listeyi ters çevirir.
print(my_list1) #([9, 6, 5])

my_list1.insert(0,4) # istenilen indexe yeni öge ekler.
print(my_list1) #[4, 9, 6, 5]
 
delete_list = [4,8,9]
del delete_list[1] #İstenilen indexteki ögeyi siler.
print(delete_list) #([4,9])

total = sum(my_list1) # listedeki elemanları toplar.
print(total) #24

max_deger= max(my_list1)
min_deger= min(my_list1)
print(max_deger,min_deger)

#LİSTELERİ KOPYALAMA
liste0=[4,8,3,7]
liste1=[]
liste2=[]
liste6=[]

#1.yöntem
liste1+= liste0
print(liste1)

#2.yöntem
for i in liste0:
    liste2.append(i)
print(liste2)

#3.yöntem
liste3 = [item for item in liste0]
print(liste3)

liste4= [item**2 for item in liste0] #liste0'daki ögelerin karelerini alır ve liste4'e ekler.
print(liste4)

str_list = ["Şevin","Ahmet","Lale"]
len_list= [len(s) for s in str_list] #str_list'teki herbir elemanın uzunluğunu len_list'e ekler.
print(len_list) #([5,5,4])

liste5=[item for item in liste0 if item<5] #liste0'daki 5'ten küçük elemanları liste5'e ekler.
print(liste5) #([4,3])

for i in liste0:
    if i<5:
        liste6.append(i)
print(liste6) #([4,3])

liste7= [[1,2],[3,4]]
print(liste7[0][1]) #(2)




#TUPLES
#İçeriği değiştirilemez.
#Listelere kıyasla daha hızlıdır ve daha güvenlidir.
#İçeriği değiştirilebilir nesneler tuple'ın içerisinde saklanabilir.

tuples0= (1,5,7,[7,8,2])
tuples0[3].append(9)
print(tuples0) #(1, 5, 7, [7, 8, 2, 9])



