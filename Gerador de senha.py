import random
import string

print("=== Gerador de Senhas ===")

tamanho = int(input("Digite o tamanho da senha desejada: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha =""

for i in range(tamanho):
    senha += random.choice(caracteres)

    print("\nSenha gerada")
    print(senha)
    print(f"Tamanho da senha: {len(senha)} caracteres")