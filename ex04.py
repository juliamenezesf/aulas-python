dias_uteis = int(input("Quantos dias úteis tem o mês? "))
horas_trabalhadas = float(input("Qual foi a quantidade de horas trabalhadas? "))
salario_hora = float(input("Quanto você recebe por hora? "))

horas_normais = dias_uteis * 8
horas_extras = max(0, horas_trabalhadas - horas_normais)

valor_hora_extra = salario_hora * 1.5
salario_base = horas_normais * salario_hora 
salario_final = salario_base + (horas_extras * valor_hora_extra)

if horas_extras > 0:
    print(f"Valor de horas extras: R${horas_extras * valor_hora_extra:.2f}")
    print(f"Salário final: R${salario_final:.2f}")
else:
    print("Você não tem direito a horas extras.")
    print(f"Salário final: R${salario_base:.2f}")