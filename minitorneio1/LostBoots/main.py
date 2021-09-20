while True:
    try:
        lotes = int(input())

        dicionario = {"pares": 0}

        for i in range(lotes):
            [tamanho, pe] = input().split(" ")
            if tamanho not in dicionario:
                if pe == "D":
                    dicionario[tamanho] = [0, 1]
                else:
                    dicionario[tamanho] = [1, 0]
            else:
                if pe == "D":
                    if dicionario[tamanho][0] >= 1:
                        dicionario[tamanho][0] -= 1
                        dicionario["pares"] += 1
                    else:
                        dicionario[tamanho][1] += 1
                else:
                    if dicionario[tamanho][1] >= 1:
                        dicionario[tamanho][1] -= 1
                        dicionario["pares"] += 1
                    else:
                        dicionario[tamanho][0] += 1

        print(dicionario["pares"])
    except Exception:
        break
