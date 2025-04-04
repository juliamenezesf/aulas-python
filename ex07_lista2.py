
nomeNadador = input("Qual é o nome do nadador(a)?")
idadeNadador = float(input("Informe a idade do nadador: "))

if idadeNadador <= 7:
  print(f"O/A {nomeNadador} está na categoria infantil!")

elif idadeNadador <= 10 :
  print(f"O/A {nomeNadador} está na categoria adolescente!")

elif idadeNadador <= 30 :
  print(f"O/A {nomeNadador} está na categoria adulto!")

else :
  print(f"O/A {nomeNadador} está na categoria senior!")