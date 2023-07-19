def depositar(saldo, extrato):
    print('Deposito')
    valor_deposito = float(input('Valor do deposito:'))
    if(valor_deposito > 0):
        saldo += valor_deposito
        extrato.append(f'Deposito: R$ {valor_deposito:.2f}\n')
    else:
        print('Valor inválido')
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    print('Saque')
    valor_saque = float(input('Valor do saque:'))
    if(valor_saque <= saldo and valor_saque <= limite and numero_saques <= LIMITE_SAQUES ):
        saldo -= valor_saque
        numero_saques += 1
        extrato.append(f'Saque: R$ {valor_saque:.2f}\n')
    else:
        print('Saque não efetuado')
    return saldo, extrato, numero_saques

def extratoC(saldo, /, *, extrato):
    print('Extrato')
    for e in extrato:
        print(e)
    print(f'Saldo na conta: R$ {saldo:.2f}\n')

def novo_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário:')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso')
        return {'agencia':agencia, 'numero_conta': numero_conta, 'usuario':usuario}

def listar_contas(contas):
    for conta in contas:
        print('Agência:', conta['agencia'],
              'C/C:', conta['numero_conta'],
              'Titular:', conta['usuario']['nome'],
              )
        print('-------------')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def novo_usuario(usuarios):
    cpf = input('Informe o CPF do usuário:')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe o usuário com esse cpf')
        return
    nome = input('Nome')
    data = input('Data de nascimento')
    endereco = input('Endereço')

    usuarios.append({'nome':nome, 'data':data, 'endereco':endereco, 'cpf':cpf})
    print('Usuario cadastrado com sucesso')


def menu():
    menu = """\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova Conta
    [l] Listar Contas
    [u] Novo Usuário 
    [q] Sair

    =>"""
    return menu


def main():
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = []
    usuarios = []
    contas = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu())
        if opcao == 'd':
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == 's':
            saldo, extrato, numero_saques = sacar(saldo = saldo, 
                                                  extrato = extrato, 
                                                  limite = limite, 
                                                  numero_saques = numero_saques, 
                                                  LIMITE_SAQUES = LIMITE_SAQUES)
        elif opcao == 'e':
            extratoC(saldo, extrato =  extrato)
        elif opcao == 'n':
            numero_conta = len(contas) + 1
            conta = novo_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 'l':
            listar_contas(contas)
        elif opcao == 'u':
            novo_usuario(usuarios)
        elif opcao == 'q':
            break
        else:
            print('Opção inválidada. Por favor selecione novamente a operação desejada. ')


main()