entradas = int(input())

for entrada in range(entradas):
    result = ""

    [inicio, fim] = [int(info) for info in input().split(" ")]
    for i in range(inicio, fim+1):
        result += str(i)
    print(result+result[-1::-1])
