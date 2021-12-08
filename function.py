from databasee import veritabani 

vt = veritabani("Deneme.db")
vt.tabloOlustur("ogrenci","Isim","Soyisim")
vt.tabloyaVeriGir("ogrenci","Baransel","Cilinger")
a = vt.verileriListele("ogrenci")
print(a)
