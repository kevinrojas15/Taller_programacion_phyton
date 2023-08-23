def division(a, b):
    if b != 0:
        cociente = a / b
        producto = a * b
        return cociente, producto
    else:
        return "No se puede dividir por cero"

num1 = float(input("Ingresa el numerador: "))
num2 = float(input("Ingresa el denominador: "))

resultado = division(num1, num2)

if isinstance(resultado, tuple):
    cociente, producto = resultado
    print(f"Cociente: {cociente:.2f}")
    print(f"Producto: {producto:.2f}")
else:
    print(resultado)