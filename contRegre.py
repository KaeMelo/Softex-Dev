from time import sleep
import time

print("iniciando contagem regressiva! ")

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)

print("BUM!")
