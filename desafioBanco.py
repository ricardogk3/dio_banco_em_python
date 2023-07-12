menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        print('Deposito')
        valor_deposito = float(input('Valor do deposito:'))
        if(valor_deposito > 0):
            saldo += valor_deposito
            extrato.append(f'Deposito: R$ {valor_deposito:.2f}\n')
        else:
            print('Valor inválido')
    elif opcao == 's':
        print('Saque')
        valor_saque = float(input('Valor do saque:'))
        if(valor_saque <= saldo and valor_saque <= limite and numero_saques <= LIMITE_SAQUES ):
            saldo -= valor_saque
            numero_saques += 1
            extrato.append(f'Deposito: R$ {valor_deposito:.2f}\n')
        else:
            print('Saque não efetuado')
    elif opcao == 'e':
        print('Extrato')
        for e in extrato:
            print(e)
        print(f'Saldo na conta: R$ {saldo:.2f}\n')
    elif opcao == 'q':
        break
    else:
        print('Opção inválidada. Por favor selecione novamente a operação desejada. ')