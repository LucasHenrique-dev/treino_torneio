entradas = int(input())


def cesar_cifra(frase, deslocamento):
    frase_codificada = ""
    for letra in frase:
        ascii_value = ord(letra)-deslocamento
        if ascii_value < 65:
            ascii_value = 91 - (65-ascii_value)
        frase_codificada += chr(ascii_value)
    return frase_codificada


for i in range(entradas):
    palavra = input()
    chave = int(input())
    print(cesar_cifra(palavra, chave))
