class Dusman:
    kalan_can = 3
    def saldir(self):
        print("Hucummmmm")
        self.kalan_can -=1
    def hayatta_mi(self):
        if (self.kalan_can <= 0):
            print("Oldu")
        else:
            print(str(self.kalan_can) + " canim kaldi")

dusman1 = Dusman()
dusman2 = Dusman()


dusman1.saldir()
dusman1.saldir()
dusman1.hayatta_mi()


dusman2.saldir()
dusman2.saldir()
dusman2.saldir()
dusman2.hayatta_mi()
