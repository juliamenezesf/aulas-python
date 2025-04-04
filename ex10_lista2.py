import math

def calcular_raizes(a, b, c):
    # Calcular o discriminante
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("A equação não tem raízes reais.")
    elif delta == 0:
        # Raiz única
        x = -b / (2*a)
        print(f"A equação tem uma raiz real: x = {x}")
    else:
        # Duas raízes reais distintas
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes reais da equação são: x1 = {x1} e x2 = {x2}")

# Exemplo de uso
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

if a != 0:
    calcular_raizes(a, b, c)
else:
    print("O coeficiente 'a' deve ser diferente de zero.")
