#tuplas 
mi_tupla= (2,4)
print ("mi tupla: ", mi_tupla)

#lista 
mi_lista = [1, 3.1416, "angel", mi_tupla]
print("El peimwe elemento de mi lista ", mi_lista[0])
print("El cuarto elemento de mi lista ", mi_lista[3])
print("El tercer elemento de mi lista ", mi_lista[2])

#diccionario 
mi_diccionario = {
    "mi_lista": mi_lista,
    "nombre": "angel",
    "Pi": 3.1416,
    "tel": "7485858344"
}
print("llave para accesar a mi diccionario mi_lista", mi_diccionario["mi_lista"])
print("llave para accesar a mi diccionario Pi", mi_diccionario["Pi"])
print("llave para accesar a mi diccionario tel", mi_diccionario["tel"])