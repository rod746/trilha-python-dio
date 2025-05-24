def menu():
    menu = """
    ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    ESCOLHA UMA FUNÇÃO
    ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    

[d]Depositar
[s]Sacar
[e]Extrato
[nc]Nova Conta
[l]Listar Contas
[nu]Novo Usúario
[q]Sair

=> """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print('\nDepósito Realizado !!!')
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente")
    elif excedeu_limite:
        print("Operação falhou! Você não tem limite suficiente")
    elif excedeu_saques:
        print("Operação falhou! Você excedeu o limite de saques!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nJá existe usuario com este CPF!!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Data de nascimento dd-mm-aaaa: ")
    endereco = input("Endereço: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, 'cpf': cpf, "endereco": endereco})
    print("Usuario registrado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('\nConta criada!')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuario não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print('¬'*20)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    agencia = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    # opcao = ''

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,                       
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) +1
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "q":
            break

        else:   
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()