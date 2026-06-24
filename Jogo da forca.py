import random

def jogar_forca():
    print("================================")
    print("  Bem vindo ao jogo da Forca!   ")
    print("================================\n")

    # Lista de palavras para o jogo
    palavras = ["banana", "abacaxi", "laranja", "morango", "uva", "melancia", "kiwi", "manga", "cereja", "pessego"]

    # Escolher uma palavra aleatória da lista
    palavra_secreta = random.choice(palavras).lower()

    # Criar uma lista de letras acertadas (começa cheia de underscores)
    letras_acertadas = ["_" for _ in palavra_secreta]

    tentativas = 6
    letras_tentadas = []

# Loop principal do jogo
    while tentativas > 0 and "_" in letras_acertadas:
        print(f"\nPalavra: {' '.join(letras_acertadas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras tentadas: {', '.join(letras_tentadas)}")

        # Receber uma letra do jogador
        chute = input("Digite uma letra: ").lower().strip()
        print("\n--------------------------------")
        
        # Validação do chute
        if len(chute) != 1 or not chute.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if chute in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        # Adicionar a letra tentada à lista
        letras_tentadas.append(chute)

        # Verificar se a letra está na palavra
        if chute in palavra_secreta:
            print(f"Muito bem! A letra '{chute}' está na palavra.")
            # atualizar os undercores com a letra acertada na posição correta
            for indice, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_acertadas[indice] = chute
        else:
            tentativas -= 1
            print(f"Que pena! A letra '{chute}' não está na palavra.")

            # verificação de fim de jogo
        if "_" not in letras_acertadas:
                print(f"\nParabéns!!! Você venceu! A palavra era: {palavra_secreta.upper()}")
        else:
            print(f'\n Fim de jogo! Você perdeu! A palavra era: {palavra_secreta.upper()}')

#  Executar o jogo
if __name__ == "__main__":
    jogar_forca()