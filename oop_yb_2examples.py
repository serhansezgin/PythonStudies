'''
import random
import time

class Enemy:
    health_remaining=100
    def attack(self):
        print("Charge! " + str(self.health_remaining))
        self.health_remaining-=random.randint(5,50)
        print(str(self.health_remaining))
    def check(self):
        if(self.health_remaining<=0):
            print("YOU DIED")
        else:
            print(str(self.health_remaining)+" Health remaining")


Enemy1 = Enemy()

Enemy1.attack()
time.sleep(1)
Enemy1.attack()
time.sleep(1)
Enemy1.attack()
time.sleep(1)
Enemy1.check()
'''


import random

class dusman:
    kalan_can =(100)
    def saldir(self):
        print("Hücum")
        self.kalan_can -= random.randrange(1,100)
    def hayatta_mi(self):
        if (self.kalan_can <= 0):
            print("Düsman öldü")
        else:
            print(str(self.kalan_can)+" canı kaldı")


dusman1=dusman()
dusman2=dusman()


dusman1.saldir()
dusman1.saldir()
dusman1.hayatta_mi()            


dusman2.saldir()
dusman2.hayatta_mi()




