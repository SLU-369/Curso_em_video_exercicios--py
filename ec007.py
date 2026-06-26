#Desenvolva um programa que leia as notas de um aluno, calcule e mostre a sua media. 
prova = float(input("Fala auluno! Quanto você tirou na prova? "))
pim = float(input("Fala auluno! Quanto você tirou no pim? "))
trabalho = float(input(f"Fala auluno! Quanto você tirou no trabalho?"))

n1 = prova * 7
n2 = pim * 2
n3 = trabalho * 1

def media():
    media = (n1 + n2 + n3) / 10
    print(f"A minha media na escola foi: {media}")

media()

