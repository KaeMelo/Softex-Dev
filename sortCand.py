import enum

class Candidatos(enum.Enum):
    candidato_X = 889
    candidato_y = 847
    candidato_Z = 515
    branco = 0

alist = {Candidato.candidato_Z:0, Candidato.candidato_X:0, Candidato.candidato_Y:0, Candidato.branco:0}
qtdVotos = int(input("Quantos eleitores? ")

for I in range(0, qtdVotos):
    try:
        voto = int(input("Número de candidatos: "))
    except ValueError:
        voto = int(input("Digite um número: "))
    finally:
        if Candidato.candidato_X.value == voto:
            alist[Candidato.candidato_X] += 1
        elif Candidato.candidato_Y.value == voto:
            alist[Candidato.candidato_Y] += 1
        elif Candidato.candidato_Z.value == voto:
            alist[Candidato.candidato_Z] += 1
        else:
            alist[Candidato.branco] += 1

ganhador = ["", 0]

for c, v in alist.items():
    print(f"{str(c).removeprefix("Candidatos.")}: {v}")
    if ganhador[1] < v and c != Candidatos.branco:
        ganhador = [c, v]

if ganhador[0] == Candidatos.branco:
    print("EMPATE!")
else:
    print(f"{str(ganhador[0]).removeprefix("Candidatos:")}foi o ganhador com {ganhador[1]}votos")
