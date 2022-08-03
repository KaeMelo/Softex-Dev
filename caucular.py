def calcula(op1, op2, operacao):
  resultado = 0
  if operacao == 1:
    resultado = op1 + op2
  elif operacao == 2:
    resultado = op1 - op2
  elif operacao == 3:
    resultado = op1 * op2
  elif operacao == 4:
     resultado = op1 / op2
  return resultado 
  
print("[1] Soma")
print("[2] Subtração")
print("[3] Multiplicação")
print("[4] Divisão")
print("[5] Sair")

operacao = int(input("Operação: "))

while operacao != 0:
  if 1 <= operacao <= 4:
