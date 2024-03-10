def inicializar_matriz():
    matriz = [['' for _ in range(4)] for _ in range(4)]
    return matriz


# Função para exibir a matriz
def exibir_matriz(matriz):
    for linha in matriz:
        print(' | '.join(linha))
        print('-' * 13)


# Função principal
def main():
    matriz = inicializar_matriz()

    while True:
        # Exibir a matriz atual
        exibir_matriz(matriz)

        # Solicitar ao usuário a linha e coluna para armazenar o valor
        linha = int(input("Digite o número da linha (1-4): ")) - 1
        coluna = int(input("Digite o número da coluna (1-4): ")) - 1

        # Verificar se a linha e coluna estão dentro dos limites da matriz
        if 0 <= linha < 4 and 0 <= coluna < 4:
            # Solicitar ao usuário o valor a ser armazenado na posição escolhida
            valor = input("Digite o valor a ser armazenado: ")

            # Armazenar o valor na posição escolhida
            matriz[linha][coluna] = valor
        else:
            print("Linha ou coluna inválida. Por favor, tente novamente.")

        # Verificar se o usuário deseja continuar
        continuar = input("Deseja continuar? (S/N): ")
        if continuar.upper() != 'S':
            break


if __name__ == "__main__":
    main()


