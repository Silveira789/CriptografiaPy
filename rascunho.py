"""
Polialfabética --> uma cifra de cezar para cada letra do alfabeto
    - a chave seleciona qual alfabeto é utilizado para cada letra da mensagem
    - um alfabeto por vez
    - Recomeçar depois que o fim da chave é atingido

CIFRA DE VIGENERE


https://www.youtube.com/watch?v=rIjLR3OYpCo


"""

# Base de dados
alfabeto = []
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letra in b:
    alfabeto.append(letra)

print(alfabeto)

a = 2

print("Anotação:"
      "\nCifra de Vigenere"
      "\nTipo de cifra polialfabética"
      "\nOBS: Chave tem que ser menor que a sua mensagem!!!!!!!!")

while a != 0:
    texto_final = ""
    print('Escolha uma opção: ')
    print("1_ Criptografar \n2_Descriptografar")
    opcao = int(input("Opção escolhida: "))
    texto = ''.join(str(input('Digite o texto: ')).upper().split())
    key = str(input('Digite a chave: ')).upper()
    final_key = ""
    if (len(key)) > len(texto):
        print("A chave é maior que sua frase")
    else:
        i = int(0)
        while len(final_key) < len(texto):
            final_key += key[i]
            i += 1
            if i == len(key):
                i = 0
        print(key)
        print(final_key)
        print(texto)
        for i in range(len(texto)):
            if (texto[i]) != " ":
                posicao_letra_frase = int(alfabeto.index(texto[i]))
                posicao_letra_chave = int(alfabeto.index(final_key[i]))
                if opcao == 1:
                    texto_final += str(alfabeto[(posicao_letra_frase + posicao_letra_chave) % len(alfabeto)])
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
