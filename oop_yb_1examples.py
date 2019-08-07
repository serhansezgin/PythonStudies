class insan:
    yas=85
    def yaslandir(self):
        print("1 koca sene daha gecti.")
        self.yas += 1

    def yasiyor_mu(self):
        if(self.yas>=88):
            print("Olmus")
        else:
            print("Yasim olmus",self.yas, "Toprak her gecen gun bana yaklasiyor.Aaah ah.")


Rana = insan() 
Ahmet = insan()

Rana.yasiyor_mu()

Ahmet.yaslandir()
Ahmet.yaslandir()
Ahmet.yaslandir()
Ahmet.yaslandir()

Ahmet.yasiyor_mu()



Rana.yaslandir()
Rana.yaslandir()
Rana.yaslandir()
Rana.yaslandir()
Rana.yasiyor_mu()