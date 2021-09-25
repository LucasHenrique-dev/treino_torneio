entradas = int(input())

for i in range(entradas):
    falantes = int(input())
    lingua = ""

    for j in range(falantes):
        lingua += input() + " "
    linguas = set(lingua.strip().split(" "))

    print("ingles") if len(linguas) > 1 else print(linguas.pop())
