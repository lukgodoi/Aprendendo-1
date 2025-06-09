# introduçao do programa
print("Bem-vindo a calculadora básica 2000!")
print("")
# escolha dos numeros e operadores
valor1 = float(input("Digite um número: "))
valor2 = float(input("Digite outro número: "))
print("")
print(f"Com isso escolha um operador para calcular {valor1} e {valor2}")
print("[1] Adição")
print("[2] Subtração")
print("[3] Multiplicação")
print("[4] Divisão")
# confirmação do calculo dos numeros e operadores
operador = int(input("Escolha seu operador: "))
print("")

if operador == 1:
    print(f"Então você quer fazer {valor1}  +  {valor2} ")
if operador == 2:
    print(f"Então você quer fazer {valor1}  - {valor2} ")
if operador == 3:
    print(f"Então você quer fazer {valor1}  x  {valor2} ")
if operador == 4:
    print(f"Então você quer fazer {valor1}  / {valor2} ")
print("")
resposta = int(input("Confirme com 1: "))
print("")
# calculo dos numeros solicitados
if resposta == 1:
    if operador == 1:
        adicao = valor1 + valor2
        print(f"O resultado da adição é de {adicao}")
    if operador == 2:
        subtracao = valor1 - valor2
        print(f"O resultado da subtração é de {subtracao}")
    if operador == 3:
        multiplicado = valor1 * valor2
        print(f"O resultado da multiplicação é de {multiplicado}")
    if operador == 4:
        dividido = valor1 / valor2
        print(f"O resultado da divisão é de {dividido}")
else:
    print("fim do programa")
