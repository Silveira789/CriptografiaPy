class SimpleEncryptorDecryptor:
    def __init__(self):
        self.key = {
            'a': 'x', 'b': 'y', 'c': 'z', 'd': 'a', 'e': 'b',
            'f': 'c', 'g': 'd', 'h': 'e', 'i': 'f', 'j': 'g',
            'k': 'h', 'l': 'i', 'm': 'j', 'n': 'k', 'o': 'l',
            'p': 'm', 'q': 'n', 'r': 'o', 's': 'p', 't': 'q',
            'u': 'r', 'v': 's', 'w': 't', 'x': 'u', 'y': 'v',
            'z': 'w', ' ': ' ', ',': ','
        }

    def encrypt(self, plaintext):
        ciphertext = ''.join(self.key.get(char, char) for char in plaintext.lower())
        return ciphertext

    def decrypt(self, ciphertext):
        decrypted_text = ''.join(key for key, value in self.key.items() if value == ciphertext.lower())
        return decrypted_text


# Exemplo de uso
encryptor_decryptor = SimpleEncryptorDecryptor()

# Texto original
original_text = "Hello, World!"

# Encriptando o texto
encrypted_text = encryptor_decryptor.encrypt(original_text)
print("Texto encriptado:", encrypted_text)

# Decriptando o texto
decrypted_text = encryptor_decryptor.decrypt(encrypted_text)
print("Texto decriptado:", decrypted_text)
