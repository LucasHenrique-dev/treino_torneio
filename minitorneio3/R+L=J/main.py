while True:
    try:
        equacao = input().replace("+", " ").replace("=", " ")
        [r, l, j] = equacao.split(" ")

        if not r.isdigit():
            print(int(j)-int(l))
        elif not l.isdigit():
            print(int(j)-int(r))
        else:
            print(int(r)+int(l))
    except EOFError:
        break
