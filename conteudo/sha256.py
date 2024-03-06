"""
SHA256
    - Algoritmo Seguro de Hash (Security Hash Algorithm)
    - Ferramena de criptografia de texto
    - Gera um hash para a informação, encriptando-a;
    - 256 bits



* Como sites armazenam informações do ususàrio na web de maneira segura na web ?

* Transformar texto em bytes

1° b"texto" -           -> b: transforma em bytes
2° "texto".encode()     -> encode(): Transforma em bytes

"""

a = b'nome'
print(type(a))
print(a)

print()

b = "texto".encode()
print(type(b))
print(b)

from hashlib import sha256

hash_b = sha256(b)
print(hash_b)
armazenameno_senha = hash_b.digest()  # .digest() --> verifica o valor do obj sha256
print(armazenameno_senha)  # impressão de valor em byte
print(len(armazenameno_senha))  # 32 * 8  = 256    --> 1 byte == 8 bits

"""
Porque o hash hexadecimal contem 64 caracteres?

R: 1 byte = 2 dígitos p/ representar o hexadecimal

"""
