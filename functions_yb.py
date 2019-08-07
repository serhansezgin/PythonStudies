'''
def factoriel(numara):
    faktoriyel = 1
    for i in range(1,numara+1):
        faktoriyel *=i
    print("Faktoriyel:",faktoriyel)


sayi = int(input("Sayiyi Giriniz:"))



factoriel(sayi)
factoriel(7)
factoriel(10)
'''

'''
def factoriel(numara):
    faktoriyel = 1
    for i in range(1,numara+1):
        faktoriyel *=i
    print("Faktoriyel:",faktoriyel)
    return faktoriyel

sayi = int(input("Sayiyi Giriniz:"))


a=factoriel(sayi)
print(a)
'''
'''
#ax^2 + bx + c
def kokbul (a,b,c):
    delta = (b*b - 4*a*c)
    if (delta < 0):
        print("Reel Kok Bulunamadi")
        return


    x1=(-b - delta**0.5)/2*a
    x2=(-b + delta**0.5)/(2*a)

    return (x1,x2)



a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

sonuc = kokbul(a,b,c)

print(sonuc)
'''

'''
def kayit_ekle(ad = "bilgi yok", soyad = "bilgi yok", yas = "bilgi yok", meslek="bilgi yok"):
    print ("Kayit Ekleniyor.")
    print("Ad:{}\nSoyad:{}\nYas:{}\nMeslek:{}\n".format(ad,soyad,yas,meslek))
    print("Kayit Basariyla Eklendi")

kayit_ekle(ad = "Mustafa Murat",yas=23)
'''

'''
def geometri(sekil):
    if len(sekil) == 3:
        a=sekil[0]
        b=sekil[1]
        c=sekil[2]

        if (a+b) > c and (a+c) > b and (b+c) > a:
            if (a==b) and (a==c) and (b==c):
                print("Eskenar Ucgen")
            elif (a==b) and (a==c):
                print("Ikizkenar Ucgen")
            else:
                print("Cesitkenar Ucgen")

        else:
            print ("Ucgen Belirtmiyor")


    elif len(sekil)==4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]
        if (a==b) and (a==c) and (a==d):
            print("Kare")
        elif (a==c) and (b==d):
            print("Dikdortgen")
        else:
            print("Normal Dortgen")


    else:
        print("Herhangi bir sekil degil")    


while (True):
    eleman_sayisi = int (input("Eleman Sayisini Giriniz:"))
    if (eleman_sayisi ==3):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        geometri([a,b,c])

    elif (eleman_sayisi ==4):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        d=int(input("d:"))
        geometri([a,b,c,d])

    else:
        print("Lutfen Tekrar Giriniz")    
'''



#func recursion

'''
def topla(liste):
    toplam=0

    for i in liste:
        toplam += i
    return toplam

print (topla([1,2,3,4]))
'''


def topla(liste):
    if (len(liste)) == 0:
        return 0
    else:
        return liste[0] + (topla(liste[1:]))


print(topla([1,2,3,4])) 























