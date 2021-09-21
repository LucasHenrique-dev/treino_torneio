partidas = int(input())

for partida in range(partidas):
    result = ""

    jogo1 = [int(info) for info in input().split(" x ")]
    jogo2 = [int(info) for info in input().split(" x ")]

    if jogo1[0] > jogo1[1] and jogo2[1] > jogo2[0]:
        result = "Time 1"
    elif jogo1[0] < jogo1[1] and jogo2[1] < jogo2[0]:
        result = "Time 2"
    else:
        time1_pontos = jogo1[0] + jogo2[1]
        time2_pontos = jogo1[1] + jogo2[0]
        if time1_pontos > time2_pontos:
            print("Time 1")
            continue
        elif time2_pontos > time1_pontos:
            print("Time 2")
            continue
        if jogo2[1] > jogo1[1]:
            result = "Time 1"
        elif jogo2[1] < jogo1[1]:
            result = "Time 2"
        else:
            result = "Penaltis"
    print(result)
