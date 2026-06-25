#Faça um projeto que leia algo pelo teclado e mostre na tela o seu tipo primitivo
nome = input("Olá, seja bem vindo ao meu Github, como você se chama ? ")
idade = int(input(f"É um prazer {nome}, e você tem quantos anos? "))

print("O timpo primitivo de nome é:", type(nome))
print("\nO timpo primitivo de idade é: ", type(idade))