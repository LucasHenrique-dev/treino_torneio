while True:
    entrada = input()

    if entrada == "0 0":
        break

    [num1, num2] = [int(info) for info in entrada.split(" ")]

    print(str(num1+num2).replace("0", ""))
