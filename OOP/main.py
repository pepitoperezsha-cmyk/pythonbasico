from Enemigo import *
from Zombie import *
from Ogro import *

zombie = Zombie(10, 1)
Ogro = ogro(20, 3) 

print(f"{zombie.get_tipo_enemigo()} tiene {zombie.punto_energia} de energia y puede hacer ataque de {zombie.ataque}")
print(f"{zombie.habla()}")
print(f"{Ogro.get_tipo_enemigo()} tiene {Ogro.punto_energia} de energia y puede hacer ataque de {Ogro.ataque}")
print(f"{Ogro.habla()}")