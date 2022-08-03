peso = float(input("Qual o peso do veículo? "))
qtdPessoas = int(input("Quantos passageiros cabem no veículo? "))
rodas = int(input("Quantas rodas o veículo possui? "))

if rodas >= 4 and peso > 6000:
  print("Carteira tipo E! ")
elif rodas >= 4 and qtdPessoas > 8:
  print("Carteira tipo D! ")
elif rodas >= 4 and 3500 <= peso <= 6000:
  print("Carteira tipo B! ")
elif 2 <= rodas <= 3:
  print("Carteira tipo A!  ")
else:
  print("Esse veículo não possui carteira.")
