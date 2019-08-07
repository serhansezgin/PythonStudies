class Calisan():
    def __init__(self,isim,maas,departman):
        print("Calisan Sinifinin Yapici Fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman
    def bilgilerigoster(self):
        print("Calisan sinifinin bilgileri gosteriliyor.....")
        print("isim",self.isim,"Maas:",self.maas,"Calistigi Departman", self.departman)
    def maasazamyap(self,zam_miktari):
        print("Maasa Zam Yapildi")
        self.maas += zam_miktari
    def departmandegistir(self,yeni_departman):
        print("Departman degisitiriliyor....")
        self.departman = yeni_departman

"""
calisan = Calisan("Mehmet Baltaci",2500,"Insan Kaynaklari")

calisan.bilgilerigoster()
"""


class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        print("Yonetici sinifinin yapici fonksiyonlari")
        super().__init__(isim,maas,departman)
        
        self.kisi_sayisi = kisi_sayisi         # ek ozellik
        #super().bilgilerigoster()
    def bilgilerigoster(self):
        print("Yonetici sinifinin bilgileri gosteriliyor...")
        print("isim",self.isim,"Maas:",self.maas,"Calistigi Departman:",self.departman,"Kisi Sayisi:",self.kisi_sayisi)
#overwrite

    def kisisayisiartir(self,artir):
        print("Kisi Sayisi Artiriliyor...")
        self.kisi_sayisi += artir


    

yonetici = Yonetici("Mehmet Baltaci",2500,"Insan Kaynaklari",20)


yonetici.bilgilerigoster()
yonetici.kisisayisiartir(10)
yonetici.bilgilerigoster




