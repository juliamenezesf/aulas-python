valor1 = float(input("digite o primeiro valor: "))
valor2 = float(input("digite o segundo valor: "))

if valor1 == valor2 :
    print("Os valores devem ser divergentes.")

elif valor1 > valor2 :
    print(f"O maior valor é {valor1}")

else :
    print(f"O maior valor é {valor2}")