Nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura(em metros): "))

meses = idade * 12
altura_cm = altura * 100

print(f"\nOlá, {Nome}!")
print(f"Você tem {idade} anos, ou seja, aproximadamente {meses} meses de vida")
print(f"Sua altura em Cm é de {altura_cm}cm.")
