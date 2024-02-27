depositos = []
saques = []
saldo = 0  # Inicializa a variável saldo

def deposito():
    global saldo  # Declara a variável saldo como global
    while True:
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            depositos.append(valor)
            break
        else:
            print("Valor inválido. Por favor, digite um valor válido.")
            print()  # Pula uma linha após a mensagem de erro

def saque():
    global saldo  # Declara a variável saldo como global
    if len(saques) < 3:
        while True:
            valor = float(input("Digite o valor do saque: "))
            if valor > 0 and valor <= 500 and valor <= saldo:
                saldo -= valor
                saques.append(valor)
                break
            else:
                print("Valor inválido. Por favor, digite um valor válido.")
                print()  # Pula uma linha após a mensagem de erro
    else:
        print("Limite diário de saques atingido.")
        print()  # Pula uma linha após a mensagem de erro

def extrato():
    print("\nExtrato:")
    print("Depósitos:")
    for dep in depositos:
        print(f"R$ {dep:.2f}")
    print("\nSaques:")
    for saq in saques:
        print(f"R$ {saq:.2f}")
    print("\nSaldo atual: R$ {:.2f}\n".format(saldo))

while True:
    print("Menu:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        deposito()
    elif opcao == 2:
        saque()
    elif opcao == 3:
        extrato()
    elif opcao == 4:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        print()  # Pula uma linha após a mensagem de erro
