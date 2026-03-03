from Enemigo import *
import random


class ogro(Enemigo):
    def __init__(self, punto_energia=20, ataque=3):
        super().__init__(tipo_enemigo='Ogro', punto_energia=punto_energia, ataque=ataque)

    def habla(self):
        print("Ogro aplasta todo!!!")

    def ataque_especial(self):
        print("ogro ataque especial o no")
        funciona_ataque_especial = random.random() <0.20
        if funciona_ataque_especial:
            self.ataque += 4
            print('Ogro enojado y incremento su ataque por 4!!!!')