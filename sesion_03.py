#loops
mi_li = [1,2,3,4,5]

for i in mi_li:
    print("El numero es: ", i)

    resul = 0
    for i in mi_li:
        resul += i
print(f"El resultado de la suma de mi lista es: {resul} ")

for i in range(2,9):
            print(i)

mi_lista_2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
for i in mi_lista_2:
       if i != "Lunes":
              print(f"Feliz{i}!")

# while loop
i = 0

while i < 5 :
    i += 1
    if i ==3:
          continue
    print(i)
    if i == 4: 
          break
    else:
          print("i es ahora mayor o igual a 5")


#practica 2
#Dada la lista mi_lista_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]
#Imprimir cada elemento de la lista 3 veces y cuando sea lunes no lo incluya 
#pista. usa los dos tipos loops while y for en el mismo programa para lograrlo
#resultado 
#martes
#miercoles 
#jueves 
#viernes 
#martes
#miercoles
#jueves
#viernes
#martes
#miercoles
#jueves
#viernes
i = 0
mi_lista_2 = ["lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
while i < 3 :
    i += 1
    for d in mi_lista_2:
          if d !="lunes":
                print(f"{d}!")