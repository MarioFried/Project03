"""
Modulo para as Tarefas de Matematica do David
"""
from random import randint
def numeros(qtd):
    for i in range(0,qtd):
        num = randint(1000,9999)
        print(f"Numero: {num}")

def div(divisor):
    while True:
        num = randint(1000,9999)
        if ((num % divisor) == 0):
            break
    print(f"Numero DIVISIVEL por {divisor}: {num}")