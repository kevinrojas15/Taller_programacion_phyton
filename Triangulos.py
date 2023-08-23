def tipo_de_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilátero"
        elif a == b or a == c or b == c:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "No es un triángulo válido"

# Ingresar las longitudes de los lados del triángulo
lado_a = float(input("Ingresa la longitud del lado a: "))
lado_b = float(input("Ingresa la longitud del lado b: "))
lado_c = float(input("Ingresa la longitud del lado c: "))

tipo = tipo_de_triangulo(lado_a, lado_b, lado_c)
print("El triángulo es de tipo {tipo}")