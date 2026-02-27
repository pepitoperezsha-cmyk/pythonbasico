from Enemigo import *


class Zombie(Enemigo):
    def __init__(self, punto_energia=10, ataque=1):
        super().__init__(tipo_enemigo='Zombie', punto_energia=punto_energia, ataque=ataque)

    def habla(self):
        print("Hummmm......")

    def propagar_enfermedad(self):
        print("El xombie esta tratando de propagar la enferm3edad!!")