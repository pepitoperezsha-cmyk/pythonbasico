from enemigo import *

class ogro(enemigo):
    def _int_(self, puntos_energia=20, ataque=2):
        super().__init__(tipo_enemigo='ogro', puntos_energia=puntos_energia, ataque=ataque)

        def habla(self):
            print("ogro aplasta todo!!!")
            