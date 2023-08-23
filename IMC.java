def calcular_imc(peso, altura):
        imc = peso / (altura ** 2)
        return imc

        peso = float(input("Ingresa tu peso en kg: "))
        altura = float(input("Ingresa tu altura en metros: "))

        imc = calcular_imc(peso, altura)
        print(f"Tu IMC es: {imc:.2f}")
