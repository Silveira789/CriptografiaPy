"""


"""


def cripto(frase):
    tradutor = ""

    for letra in frase:
        if letra in "Aa":
            tradutor = tradutor + "@"
        elif letra in "Ee":
            tradutor = tradutor + "#"
        else:
            tradutor = tradutor + letra
    return f"{tradutor}, {letra}"


print(cripto("paralelepipedo"))