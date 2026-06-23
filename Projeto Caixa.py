# Nosso saldo inicial
Saldo = 500

print("=== Bem vindo ao Banco Python ===")

#Um looping para o programam continuar rodando até que o usuário decida sair
while True:
    print("\nEscolha uma opção:")
    print("1 - Ver saldo")
    print("2 - Depositar Diheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Sair")

    #Recebendo a opção do usuário
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        print(f"Seu saldo atual é: R${Saldo:.2f}")

    elif opcao == "2":
        valor_deposito = float(input("Digite o valor que deseja depositar: R$"))
        if valor_deposito > 0:
            Saldo += valor_deposito
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido. Tente novamente.")

    elif opcao == "3":
        valor_saque = float(input("Digite o valor que deseja sacar: R$"))
        if 0 < valor_saque <= Saldo:
            Saldo -= valor_saque
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso! Seu saldo atual é: R${Saldo:.2f}")
        else:
            print("Valor de saque inválido ou saldo insuficiente. Tente novamente.")

    elif opcao == "4":
        print("Obrigado por usar o Banco Python! Até logo!")
        break # Para o looping e fecha o programa

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")