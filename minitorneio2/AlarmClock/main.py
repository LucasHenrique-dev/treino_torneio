while True:
    try:
        entrada = input().strip()
        if entrada == "0 0 0 0":
            break
        [h1, m1, h2, m2] = [int(info) for info in entrada.split(" ")]

        if m1 > m2:
            min_dif = 60 - m1 + m2
            h1 += 1
        else:
            min_dif = m2 - m1

        if h1 > h2:
            hora_dif = 24 - h1 + h2
        else:
            hora_dif = h2 - h1

        print(hora_dif*60 + min_dif)
    except EOFError:
        break
