while True:
    entrada = input()
    if entrada == "0 0":
        break
    target = int(entrada.split(" ")[0])
    bolas = [int(info) for info in input().split(" ")]
    bolas.sort()

    if 0 not in bolas or target not in bolas:
        print("N")
        continue

    possibilidades = []
    for i in range(int(len(bolas)/2)+1):
        for j in range(i+1, len(bolas)):
            possibilidades.append(abs(bolas[i]-bolas[j]))

    if sum(set(possibilidades)) == (target+1)*target/2:
        print("Y")
    else:
        print("N")
