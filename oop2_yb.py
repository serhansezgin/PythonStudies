import random
class Dusman:
    
    def __init__(self,isim = "Dusman",kalan_can = 500,saldiri_gucu = 10,mermi_sayisi = 5):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):
        print(self.isim + " Saldiriliyor.")
        harcanan_mermi = random.randrange(0,10)
        print(str(harcanan_mermi) + " kadar harcandi")
        self.mermi_sayisi -= harcanan_mermi

        return(harcanan_mermi,self.saldiri_gucu)
    def saldiriyaugra(self,harcanan_mermi,saldiri_gucu):
        print("Vuruldum")
        self.kalan_can -= (harcanan_mermi + saldiri_gucu)
    def mermi_bitti_mi(self):
        if (self.mermi_sayisi <= 0):
            print(self.isim + "Konusuyor : Mermim bitti.Oyundan cikiyorum")    
            return True
        return False
    def hayatta_mi(self):
        if (self.kalan_can <=0):
            print("Oluyorum....")

    def print(self):
        print("Basiliyor...........")
        print("isim:",self.isim,"Kalan Can:",self.kalan_can,"Saldiri Gucu:",self.saldiri_gucu,"Mermi Sayisi: ",self.mermi_sayisi)

dusmanlar = []

i=0
while (i<10):
    rastgelecan = random.randrange(100,200)
    rastgelesaldirigucu = random.randrange(10,20)
    rastgelemermi = random.randrange(20,30)
    yenidusman = Dusman("Dusman" + str(i+1),rastgelecan,rastgelesaldirigucu,rastgelemermi)
    dusmanlar.append(yenidusman)

    i += 1


"""
for dusman in dusmanlar:
    dusman.print()
"""

i = 0
while (i<3):
    randomdusman1 = random.randrange(0,10)
    randomdusman2 = random.randrange(0,10)
    
    donendeger = dusmanlar[randomdusman1].saldir()  # (15,5)


    dusmanlar[randomdusman2].saldiriyaugra(donendeger[0],donendeger[1])


    print("Round Bitti....")


    i +=1

    







