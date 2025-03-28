time1 = input("Digite o primeiro time: ")
time2 = input("Digite o segundo time: ")

gol1 = input("Quantos gols o primeiro time fez?  ")
gol2 = input("Quantos gols o segundo time fez?  ")

if gol1 > gol2 :
    print(f"O {time1} é o vencedor!")

elif gol2 > gol1 :
    print(f"O {time2} é o vencedor!")

else :
    print("Foi um empate!")