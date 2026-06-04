# ● Creare una classe coin che ha come attributo il valore della faccia
# ● E ha due metodi:
# ○ uno che simula il lancio della moneta e che salva il valore sull'attributo faccia.
# ○ uno che ritorna il valore dell'attributo faccia

import random

class Coin() :

    def __init__(self, faccia = 'Rovescio'):
        
        self.faccia = faccia
    
    
    def lancia(self):

        if random.randint(0,1) == 0 :
            self.faccia = 'Dritto'
        else:
            self.faccia = 'Rovescio'


    def stamba(self):
        return self.faccia
    
coin = Coin()
print(coin.stamba())
coin.lancia()
print(coin.stamba())
