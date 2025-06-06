# início da simulação
print("Bem-vindo(a) ao Simulador de Viagem 2000")
print("")
print("Para começarmos vou precisar de algumas informações suas, digite 'Enter' parar continuarmos")
input("")

# coleta de dados
nome = input("Digite o seu nome: ")
distancia = int(input("Digite a distância da viagem (em Km): "))
valor_gasolina = float(input("Digite o valor da gasolina (em R$): "))
media_de_consumo = int(input("Quantos Km seu carro faz com 1L de gasolina: "))

# cálculos
# para acharmos os litros nescessario precisamos dividir a quantidade de km que o carro faz com 1l pelo km da viagem
litros_nescessarios = distancia / media_de_consumo
valor_da_viagem = litros_nescessarios * valor_gasolina

# exibição de resultados
print("")
print(f"{nome} percorrerá {distancia} Km com isso precisará de {litros_nescessarios: .2f} litros de gasolina, então, o custo da viagem será de R$", round(valor_da_viagem, 2))
print("")
print('tipo do dado do valor da viagem:', type(valor_da_viagem))
print("")
