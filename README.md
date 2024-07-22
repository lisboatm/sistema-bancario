## README

### Descrição

Este script Python simula um sistema bancário simples com funcionalidades de depósito, saque e extrato. Os usuários podem fazer depósitos e saques, visualizar seu saldo atual e ver um histórico das transações realizadas.

### Funcionalidades

- **Depósito:** Permite ao usuário adicionar fundos à conta.
- **Saque:** Permite ao usuário retirar fundos da conta, com um limite diário de três saques e um valor máximo de R$ 500 por saque.
- **Extrato:** Exibe o histórico de depósitos e saques, bem como o saldo atual da conta.
- **Menu:** Interface de menu simples para navegar entre as funcionalidades.

### Requisitos

- Python 3.6 ou superior.

### Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Salve o código em um arquivo, por exemplo, `banco_simples.py`.
3. Execute o script usando o comando:

```bash
python banco_simples.py
```

4. Siga as instruções no terminal para interagir com o sistema bancário.

### Funcionalidades Detalhadas

#### Depósito

Permite ao usuário fazer um depósito na conta. O valor do depósito deve ser positivo.

#### Saque

Permite ao usuário fazer um saque da conta. O saque tem as seguintes restrições:
- Máximo de três saques por dia.
- Valor máximo de R$ 500 por saque.
- O valor do saque deve ser positivo e não pode exceder o saldo disponível.

#### Extrato

Exibe o histórico de depósitos e saques, além do saldo atual da conta.

#### Menu

O menu principal permite ao usuário selecionar a operação desejada:
1. **Depósito**
2. **Saque**
3. **Extrato**
4. **Sair**

### Exemplo de Execução

```plaintext
Menu:
1 - Depósito
2 - Saque
3 - Extrato
4 - Sair
Escolha uma opção: 1
Digite o valor do depósito: 100
Menu:
1 - Depósito
2 - Saque
3 - Extrato
4 - Sair
Escolha uma opção: 2
Digite o valor do saque: 50
Menu:
1 - Depósito
2 - Saque
3 - Extrato
4 - Sair
Escolha uma opção: 3

Extrato:
Depósitos:
R$ 100.00

Saques:
R$ 50.00

Saldo atual: R$ 50.00

Menu:
1 - Depósito
2 - Saque
3 - Extrato
4 - Sair
Escolha uma opção: 4
Saindo do programa.
```

### Explicação do Código

1. **Inicialização das Variáveis:**
    ```python
    depositos = []
    saques = []
    saldo = 0  # Inicializa a variável saldo
    ```

2. **Função `deposito`:**
    Solicita um valor de depósito, valida se o valor é positivo e atualiza o saldo e a lista de depósitos.
    ```python
    def deposito():
        global saldo
        while True:
            valor = float(input("Digite o valor do depósito: "))
            if valor > 0:
                saldo += valor
                depositos.append(valor)
                break
            else:
                print("Valor inválido. Por favor, digite um valor válido.")
                print()
    ```

3. **Função `saque`:**
    Solicita um valor de saque, valida se o valor é positivo, não excede R$ 500, não excede o saldo disponível e se o limite de três saques diários não foi atingido. Atualiza o saldo e a lista de saques.
    ```python
    def saque():
        global saldo
        if len(saques) < 3:
            while True:
                valor = float(input("Digite o valor do saque: "))
                if valor > 0 and valor <= 500 and valor <= saldo:
                    saldo -= valor
                    saques.append(valor)
                    break
                else:
                    print("Valor inválido. Por favor, digite um valor válido.")
                    print()
        else:
            print("Limite diário de saques atingido.")
            print()
    ```

4. **Função `extrato`:**
    Exibe o histórico de depósitos, saques e o saldo atual.
    ```python
    def extrato():
        print("\nExtrato:")
        print("Depósitos:")
        for dep in depositos:
            print(f"R$ {dep:.2f}")
        print("\nSaques:")
        for saq in saques:
            print(f"R$ {saq:.2f}")
        print("\nSaldo atual: R$ {:.2f}\n".format(saldo))
    ```

5. **Menu Principal:**
    Um loop que exibe o menu, solicita uma opção do usuário e chama a função correspondente.
    ```python
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
            print()
    ```

### Contribuição

Sinta-se à vontade para contribuir com melhorias no código ou na documentação, abrindo issues ou pull requests no repositório correspondente.
