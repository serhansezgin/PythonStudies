class Dusman:
    


    def __init__(self,isim = "Dusman",kalan_can = 500,saldiri_gucu = 10,mermi_sayisi = 5):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi



    def print(self):
        print("Basiliyor...........")
        print("isim:",self.isim,"Kalan Can:",self.kalan_can,"Saldiri Gucu:",self.saldiri_gucu,"Mermi Sayisi: ",self.mermi_sayisi)


dusman1 = Dusman("Ali",2000,30,50)
dusman2 = Dusman("Veli",1000,20,40)
dusman3 = Dusman()
print("Dusman1---------------------------------------")
dusman1.print()
print("Dusman2---------------------------------------")
dusman2.print()
print("Dusman3---------------------------------------")
dusman3.print()





