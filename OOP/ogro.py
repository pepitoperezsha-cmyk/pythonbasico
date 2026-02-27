from Enemigo import *

class ogro(Enemigo):
    def __init__(self, punto_energia=20, ataque=3):
        super().__init__(tipo_enemigo='Ogro', punto_energia=punto_energia, ataque=ataque)

    def habla(self):
        print("Ogro aplasta todo!!!")
