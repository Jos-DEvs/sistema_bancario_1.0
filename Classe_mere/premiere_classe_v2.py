from datetime import datetime

def relogio():
    data_de_hoje = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    return data_de_hoje

operacao = {"saldo": 0, "numero_saques": 0, "limite_saques": 10, "extrato": "", "inicio": 0, "reloginho": ""}

saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10
titulo = "EXTRATO"

while 1 == 1:
    
    # Construir o menu
    print(35 * "-")
    print("Bem-vindo! O que deseja fazer hoje? \n")
    print(" [d] Depositar\n [s] Sacar \n [e] Extrato \n [q] Sair")

    # Entrada de dados do usuário
    opcao = input("=> ")
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} --- {relogio()}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:  # Nem deixar entrar um valor se o número máximo de saques foi  excedido
            print("Operação falhou! O número máximo de saques já foi excedido.")
                    
        elif saldo == 0:
            print("Operação falhou! Você precisa fazer um depósito primeiro para poder sacar.")
            
        else:
            valor = float(input("Informe o valor do saque: "))

            if valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif valor > 500:
                print("Operação falhou! O valor do saque excede o limite.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f} --- {relogio()}\n"
                numero_saques += 1
                

            else:
                print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "e":
        
        if saldo == 0:
            print("Operação falhou! Você precisa fazer um depósito primeiro para poder exibir um extrato.")
        
        else:
            print(f"\n {titulo:=^40}")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=" * 40)
        
    elif opcao == "q":
        print("Até logo!")
        break
        
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.\n")
