class CriptografiaBasica:
    def __init__(self):
        self.chave = {
            'a': 'x', 'b': 'q', 'c': 'w', 'd': 'e', 'e': 'r',
            'f': 't', 'g': 'y', 'h': 'u', 'i': 'i', 'j': 'o',
            'k': 'p', 'l': 'a', 'm': 's', 'n': 'd', 'o': 'f',
            'p': 'g', 'q': 'h', 'r': 'j', 's': 'k', 't': 'l',
            'u': 'z', 'v': 'x', 'w': 'c', 'x': 'v', 'y': 'b',
            'z': 'n', ' ': ' '
        }

    def encriptar(self, mensagem):
        mensagem_cifrada = ''
        for letra in mensagem.lower():
            if letra in self.chave:
                mensagem_cifrada += self.chave[letra]
            else:
                mensagem_cifrada += letra
        return mensagem_cifrada

    def decriptar(self, mensagem_cifrada):
        mensagem = ''
        for letra in mensagem_cifrada.lower():
            for chave, valor in self.chave.items():
                if valor == letra:
                    mensagem += chave
                    break
            else:
                mensagem += letra
        return mensagem


# Exemplo de uso
if __name__ == "__main__":
    cripto = CriptografiaBasica()

    # Encriptar mensagem
    mensagem_original = input("DIGITAR: ")
    mensagem_cifrada = cripto.encriptar(mensagem_original)
    print("Mensagem cifrada:", mensagem_cifrada)

    # Decriptar mensagem
    mensagem_decriptada = cripto.decriptar(mensagem_cifrada)
    print("Mensagem decriptada:", mensagem_decriptada)
