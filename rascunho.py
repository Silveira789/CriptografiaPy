"""
Polialfabética --> uma cifra de cezar para cada letra do alfabeto
    - a chave seleciona qual alfabeto é utilizado para cada letra da mensagem
    - um alfabeto por vez
    - Recomeçar depois que o fim da chave é atingido

CIFRA DE VIGENERE





"""

# Base de dados
alfabeto = []
caracteres_especiais = []
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ"
c = "!@#$%¨&*()_+|<>:;?°//*'-'"

for i in c:
    caracteres_especiais.append(i)

for letra in b:
    alfabeto.append(letra)

# print(alfabeto)
# print(caracteres_especiais)

a = 2

# print("Anotação:"
#       "\nCifra de Vigenere"
#       "\nTipo de cifra polialfabética"
#       "\nOBS: Chave tem que ser menor que a sua mensagem!!!!!!!!")

print()

while a != 0:
    texto_final = ""
    print('Escolha uma opção: ')
    print("1_Criptografar \n2_Descriptografar \n3_Sair")
    opcao = int(input("Opção escolhida: "))
    if opcao == 3:
        exit()
    texto = ''.join(str(input('Digite o texto: ')).upper().split())
    key = str(input('Digite a chave: ')).upper()
    final_key = ""
    for i in texto:
        if i in caracteres_especiais:
            print("Não é permitido caracteres epeciais")
            print("Tente Novamente")
            exit()
    if len(key) <= 2:
        print("chave muito pequena digitar mais de 2 carcteres")
    elif (len(key)) > len(texto):
        print("A chave é maior que sua frase")
    else:
        i = int(0)
        while len(final_key) < len(texto):
            final_key += key[i]
            i += 1
            if i == len(key):
                i = 0
        # print(key)
        # print(final_key)
        # print(texto)
        for i in range(len(texto)):
            if (texto[i]) != " ":
                posicao_letra_frase = int(alfabeto.index(texto[i]))
                posicao_letra_chave = int(alfabeto.index(final_key[i]))
                # print(posicao_letra_frase)
                # print(posicao_letra_chave)
                if opcao == 1:
                    texto_final += str(alfabeto[(posicao_letra_frase + posicao_letra_chave) % len(alfabeto)])
                    # print(texto_final)
                elif opcao == 2:
                    texto_final += str(alfabeto[posicao_letra_frase - posicao_letra_chave % len(alfabeto)])
                else:
                    print("Opção incorreta")
            else:
                texto_final += " "
        print(f"Frase final: {texto_final}")
        print("\n")

pass

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# texto = ''.join(str(input('Digite o texto: ')).upper().split())
# texto2 = str(input('Digite o texto: ')).upper().split()
# texto3 = str(input('Digite o texto: ')).upper()
# texto4 = ''.join(str(input('Digite o texto: ')).upper())
#
# print(texto)
# print(type(texto))
# print(texto2)
# print(type(texto2))
# print(texto3)
# print(type(texto3))
# print(texto4)
# print(type(texto4))
