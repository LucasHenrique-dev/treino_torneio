entradas = int(input())

numeros = {"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6}

for i in range(entradas):
    print(sum([numeros[info] for info in input()]), "leds")
