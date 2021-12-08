import sqlite3 as sql

    def __init__(self,name):
        self.name = name
        self.vt = sql.connect(self.name)            
        self.imlec = self.vt.cursor()
    
    def tabloOlustur(self,tableName,kAd,kAd2):
        self.imlec.execute(f"Create table {tableName} ({kAd},{kAd2})")
        self.vt.commit()
    
    def tabloyaVeriGir(self,tableName,name,lastName):
                
        sorgu = f"""  insert into {tableName} values(?,?) """
        self.imlec.execute(sorgu,(name,lastName))
        self.vt.commit()    
    
    def verileriListele(self,tableName):
        self.imlec.execute(f"Select * from {tableName}")
        veriler = self.imlec.fetchall()
        print("Başarılı")
        return veriler