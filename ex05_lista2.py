A = int(input("informe um número: "))
B = int(input("Informe outro número: "))

if B == 0:
    print("Não é possível dividir por zero.")
elif A % B == 0:
    print(f"{A} é divisível por {B}.")
else:
    print(f"{A} não é divisível por {B}.")