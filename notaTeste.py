import string

nota01 = float(input("Digite sua primeira nota: "))
nota02 = float(input("Digite sua segunda nota: "))
qdtFaltas = float(input("Digite a quantidade de faltas: "))
nomeAluno = input("Digite seu nome: ")

media = (nota01 + nota02)/2

print("Sua primeira nota é: ", nota01)
print("Sua segunda nota é:", nota02)
print("Essa é sua quantidade de faltas: ", qdtFaltas)
print("Sua média final é: ", media)

if qdtFaltas >= 3:
     print("Aluno", nomeAluno, "Reprovado")
elif media >= 7:
    print("O aluno(A)", nomeAluno, "Aprovado!") 
else:
    print("Reprovado!")
