while True:
    entrada = input()
    if entrada == "0 0":
        break
    [target, tamanho] = [int(info) for info in entrada.split(" ")]
    bolas = [int(info) for info in input().split(" ")]
    bolas.sort()

    if 0 not in bolas or target not in bolas:
        print("N")
        continue

    possibilidades = []
    for i in range(tamanho):
        for j in range(i+1, tamanho):
            possibilidades.append(abs(bolas[i]-bolas[j]))

    if sum(set(possibilidades)) == (target+1)*target/2:
        print("Y")
    else:
        print("N")

# while True:
#     entrada = input()
#     if entrada == "0 0":
#         break
#     [target, tamanho] = [int(info) for info in entrada.split(" ")]
#
#     bolas = [int(bola) for bola in input().split(" ")]
#     bolas.sort()
#
#     objetivos = [False for i in range(target+1)]
#     objetivos[0] = True
#
#     flag = False
#     for i in range(tamanho):
#         for j in range(i+1, tamanho):
#             # print(f"{bolas[i]} - {bolas[j]} = {abs(bolas[i]-bolas[j])}")
#             diferenca = abs(bolas[i]-bolas[j])
#
#             if not objetivos[diferenca]:
#                 objetivos[diferenca] = True
#         if all(objetivos):
#             print("Y")
#             flag = True
#             break
#     if not flag:
#         print("N")
#
