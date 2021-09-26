def verificar(list3, list2, l3_size, soma):
    if soma >= l3_size:
        return False
    if l3_size <= len(list2):
        return list3 == list2
    else:
        impar = 0
        if l3_size % 2 == 1:
            impar = 1
        l4 = []
        limite = int((l3_size - soma) / 2)
        for j in range(limite):
            l4.append(list3[j] + list3[l3_size - (j + 1 + impar)])
        if impar == 1:
            l4.insert(0, l3[-1])
        if verificar(l4, list2, limite+impar, soma):
            return True
        else:
            soma += 2
            l4 = l3[:soma]
            for j in range(limite - 1):
                l4.append(list3[j + soma] + list3[l3_size - (j + 1 + impar)])
            verificar(l4, list2, limite, soma + 2)
    return False


while True:
    try:
        tamanho_l1 = int(input())
        l1 = [int(info) for info in input().split(" ")]

        tamanho_l2 = int(input())
        l2 = [int(info) for info in input().split(" ")]

        if not sum(l1) == sum(l2):
            print("N")
            continue

        if l1 == l2 or l1 == l2[-1::-1]:
            print("S")
            continue

        index = 0
        last_index = tamanho_l1

        for i in range(tamanho_l2):
            if l1[i] == l2[i]:
                index += 1
            else:
                break
        if index == 0:
            for i in range(tamanho_l2):
                if l1[tamanho_l1-(i+1)] == l2[i]:
                    last_index -= 1
                else:
                    break

        l3, l2_aux = [], []
        if not last_index == tamanho_l1:
            l3, l2_aux = l1[:last_index], l2[last_index-1:]
        else:
            l3, l2_aux = l1[index:], l2[index:]

        if verificar(l3, l2_aux, len(l3), 0):
            print("S")
        else:
            print("N")

    except EOFError:
        break
