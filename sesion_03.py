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
       if i==3:
        continue
       print(i)
else:
      print("i es ahora mayor o igual a 5")