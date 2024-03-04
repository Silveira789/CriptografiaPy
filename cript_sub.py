# Função para criptografar uma mensagem
def encrypt(message, key):
    # Substituição: mapeia cada caractere da mensagem para um caractere criptografado com base na chave
    encrypted_message = ''.join(chr((ord(char) + key) % 256) for char in message)

    # Transposição: inverte a mensagem criptografada
    encrypted_message = encrypted_message[::-1]

    return encrypted_message


# Função para descriptografar uma mensagem
def decrypt(encrypted_message, key):
    # Transposição: inverte a mensagem criptografada de volta para sua forma original
    encrypted_message = encrypted_message[::-1]

    # Substituição: mapeia cada caractere da mensagem criptografada de volta para seu caractere original com base na chave
    decrypted_message = ''.join(chr((ord(char) - key) % 256) for char in encrypted_message)

    return decrypted_message


# Mensagem original
original_message = input("DIGITE: ")

# Chave de criptografia
encryption_key = 3

# Criptografar a mensagem original
encrypted_message = encrypt(original_message, encryption_key)
print("Mensagem criptografada:", encrypted_message)

# Descriptografar a mensagem criptografada
decrypted_message = decrypt(encrypted_message, encryption_key)
print("Mensagem descriptografada:", decrypted_message)
