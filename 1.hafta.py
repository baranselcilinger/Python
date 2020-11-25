print("Hello world")
#Ekran çıktısı almak için kullanılır

#Farklı örnekler ile ekran çıktıları
ad = "Baransel Çilinger"
print(ad)
sayi=35
Sayi=45
print(sayi)


#type değerin hangi türden olduğunu yazdırmak için kullanılır.
print("ad değişkenin türü:",type(ad))
print("sayi değişkenin türü:",type(sayi))

#upper yazdırılıcak olan harflerin büyük yazılmasını sağlar.
harfler="abcdef" #string
print(harfler.upper())
print("abcdef".upper())

#Kullanıcıdan alıcağımız ad-soyad bilgisi ile ekrana yazdırma işlemi yaptık.
Ad=input("Lütfen Adınızı Giriniz:")
Soyad=input("Soyadınızı Giriniz:")
print("Merhaba",Ad, Soyad)
print("Merhaba {} {}".format(Ad,Soyad))


#input değerini str olarak girsek bile int'e dönüştürme işlemi yaptığımız
#için programımız hata vericektir
sayi1=int(input("Sayı giriniz:"))#str 20
sayi2=int(input("Sayı giriniz:"))#str 10

toplam=sayi1+sayi2
print(toplam)