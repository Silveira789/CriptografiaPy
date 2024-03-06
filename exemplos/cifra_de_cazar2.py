def cripto_cesar(texto, p):
    cifra = ''

    for i in range((len(texto))):
        char = texto[i]

        if (char.isupper()):
            cifra += chr((ord(char) + p - 65) % 26 + 65)
        else:
            cifra += chr((ord(char) + p - 97) % 26 + 97)
    return cifra


texto = "O rato roeu a roupa do rei de roma"
p = 3

print(f"Texto previsto: {texto}")
print(f"padrão: {str(p)}")
print(f'cifra: {cripto_cesar(texto, p)}')
