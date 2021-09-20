import math

numeros = int(input())


def is_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for n in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % n == 0:
            return False
    return True


for i in range(0, numeros):
    valor = int(input())
    result = is_primo(valor)
    print(f"{valor} eh primo") if result else print(f"{valor} nao eh primo")
