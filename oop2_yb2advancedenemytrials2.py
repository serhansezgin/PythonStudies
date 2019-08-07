import random
class Oyun:

    def __init__(self,isim="Bas Komutan",can=100,mermi=100):

        self.isim=isim
        self.can=can
        self.mermi=mermi


    def atak(self):
        print(self.isim + " Ataturk konusuyor: Ordular ilk hedefiniz Akdeniz ileri!!!")
        harcanan_mermi=random.randrange(0,50)
        print(str(harcanan_mermi)+" kadar mermi harcandi.")
        mermi=self.mermi-harcanan_mermi
        print(mermi)
        print("Merminiz kaldi.")

    def savunma(self):
        print(self.isim + " Konusuyor: Baskin yiyoruz, askerler kacmak Turk'e yakismaz, direnin!!!")
        print(self.isim + " Ataturk Konusuyor: Geldikleri gibi gidecekler...")
        isabetli_mermi=random.randrange(0,100)
        can = self.can - isabetli_mermi
        print(can)
        print("Caniniz Kaldi.")



    def sarjor_durumu(self):
        if self.mermi == 0:
            print("Sarjorum tukendi, takviye istiyorum, cepenin kuzey batisindayim...")
        else:
            print("ilerliyorum...")


    def iyi_durum_raporu(self):
        print(self.isim + " Konusuyor, kuzey cephesinde durumlar nasil?")
        print("Dusman ussune dogru ilerliyoruz, asayis belkemal komutanim....")
        print(self.isim + " Konusuyor: Bravo askerler temizleyin onlari.... ")


    def kotu_durum_raporu(self):
        print(self.isim + " Konusuyor, orada durumlar nasil?")
        print("Guvende degiliz komunatim, dogu cephesine yardim istiyoruz....")
        print(self.isim + " Konusuyor: Yardim yolluyorum, kipirdamayin!!!.... ")

    def hayatta_mi(self):
        if self.can<=0:
            print("Oldu.")
        else:
            print("Ben iyiyim, ilerliyorum.")
    def esir_askerlerimiz(self):
        print("Dusman konusuyor: Komutan, askerlerin elimizde, ya yenilgiyi kabul edersin, yada olurler. ")

    def baskomutan_cevabi(self):
        print(" Komutan konusuyor: Turk askeri yigittir cesurdur.")
        print(" Onlarin kilina zarar gelsin, sana aci cektiririm.")

    def savasin_sonu(self):

        Adet1=int(input("Asker sayinizi giriniz:"))
        Adet2=int(input("Asker sayinizi giriniz:"))
        if Adet1 > Adet2:
            print("Turkler Kazandi!!!")
        elif Adet1==Adet2:
            print("Savas berabere bitmistir")
        else:
            print("Dusman kazandi.")

    def giris(self):
        print("isim:",self.isim,"Can:",self.can,"Mermi:",self.mermi)


Start = Oyun()


Start.savunma()
Start.kotu_durum_raporu()
Start.iyi_durum_raporu()
Start.hayatta_mi()
Start.esir_askerlerimiz()
Start.baskomutan_cevabi()
Start.atak()
Start.sarjor_durumu()
Start.savasin_sonu()




























































