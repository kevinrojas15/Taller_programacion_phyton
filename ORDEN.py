def mostrar_orden(lista):
    ordenada = sorted(lista)
    orden = {valor: index + 1 for index, valor in enumerate(ordenada)}
    return orden

numeros = []

n = int(input("Ingresa la cantidad de números: "))
for i in range(n):
    numero = float(input(f"Ingresa el número {i + 1}: "))
    numeros.append(numero)

orden = mostrar_orden(numeros)

for numero, posicion in orden.items():
    print(f"El número {numero} está en la posición {posicion}")