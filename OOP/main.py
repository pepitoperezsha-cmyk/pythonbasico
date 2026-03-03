from Enemigo import *
from Zombie import *
from Ogro import *

zombie = Zombie(10, 1)
Ogro = ogro(20, 3) 

def batalla(e1: Enemigo, e2: Enemigo):
    e1.habla()
    e2.habla()

    while e1.punto_energia > 0 and e2.punto_energia > 0:
        print("**************")
        e1.atque_especial()
        e2.atque_especial()
        print(f"{e1.get_tipo_enemigo()}: quedan {e1.punto_energia} puntos de energia!!!!")
        print(f"{e2.get_tipo_enemigo()}: quedan {e2.punto_energia} puntos de energia!!!!")
        print(f"ataque: {e2.ataque}")
        e1.punto_energia -= e2.ataque
        print("/////////")
        print(f"ataque: {e1.ataque}")
        e2.punto_energia -= e1.ataque

    print("*****************************")
    if e1.punto_energia > 0:
        print(f"{e1.get_tipo_enemigo} gano!!!!!")
    else:
        print(f"{e2.get_tipo_enemigo()} gano!!!!!")


print("===============BATALLA==============")

batalla(zombie, Ogro)

print("===========FIN DE LA BATALLA=================")


#print(f"{zombie.get_tipo_enemigo()} tiene {zombie.punto_energia} de energia y puede hacer ataque de {zombie.ataque}")
#print(f"{zombie.habla()}")
#print(f"{Ogro.get_tipo_enemigo()} tiene {Ogro.punto_energia} de energia y puede hacer ataque de {Ogro.ataque}")
#print(f"{Ogro.habla()}")