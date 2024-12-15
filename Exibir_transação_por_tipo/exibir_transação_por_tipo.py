from datetime import datetime

# Função que gera a data e horas
def relogio():
    data_de_hoje = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    return data_de_hoje

i = 0
y = 0

# O ditionário que estoca as informações
operacao = {"saldo": 0, "numero_saques": 0, "limite_saques": 10, "inicio": 0, "reloginho": ""}

filtragem = dict()

titulo = "EXTRATO"
hora_limite_de_operacao = " "
iteracao = 0



while 1 == 1:
    
    # Construir o menu
    print(35 * "-")
    print("Bem-vindo! O que deseja fazer hoje? \n")
    print(" [d] Depositar\n [s] Sacar \n [e] Extrato \n [a] Alterar data \n [t] Exibir o BD \n [q] Sair")

    # Entrada de dados do usuário
    opcao = input("=> ")
    
    # Operação de depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            operacao["saldo"] += valor
            
            operacao[f"extrato{i}"] = {"tipo": "Depósito", "valor": f"{valor}", "data": f"{relogio()}"}            
            i += 1
            print(f'{"Deposito realizado com succeso!":=^50}') # Centralizar o texto
            pe_pagina = f"{relogio()}: DEPOSITAR"
            print(f"{pe_pagina:^50}") # Centralizar o texto

        else:
            print("Operação falhou! O valor informado é inválido.")

    # Operação de saque
    elif opcao == "s":
        
        if operacao["inicio"] == 1:
            if relogio() > operacao["reloginho"]:  # Se já é um outro dia, reiniciar a variável numero_saques
                operacao["numero_saques"] = 0
                    
        if operacao["numero_saques"] >= operacao["limite_saques"]:  # Nem deixar entrar um valor se o número máximo de saques foi excedido
            print("Operação falhou! O número máximo de saques diário já foi excedido.")
                    
        elif operacao["saldo"] == 0:
            print("Operação falhou! Você precisa fazer um depósito primeiro para poder sacar.")
            
        else:
            valor = float(input("Informe o valor do saque: "))

            if valor > operacao["saldo"]:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif valor > 500:
                print("Operação falhou! O valor do saque excede o limite.")

            elif valor > 0:
                                
                if operacao["inicio"] == 0:   
                    hora_limite_de_operacao = f"{relogio()}"                    
                    operacao["reloginho"] = hora_limite_de_operacao.replace(f'{hora_limite_de_operacao[9:]}','24:00:00')   # Definir a hora limite de operação diária            
                    operacao["inicio"] = 1
                    
                operacao["saldo"] -= valor
                
                operacao[f"extrato{i}"] = {"tipo": "Saque", "valor": f"{valor}", "data": f"{relogio()}"}
                i += 1
                operacao["numero_saques"] += 1
                print(f'{"Saque realizado com succeso!":=^50}') # Centralizar o texto
                pe_pagina = f"{relogio()}: SACAR"
                print(f"{pe_pagina:^50}") # Centralizar o texto
                
            else:
                print("Operação falhou! O valor informado é inválido.")
                
    # Operação de exibir o extrato  
    elif opcao == "e":
        
        if operacao["saldo"] == 0:
            print("Operação falhou! Você precisa fazer um depósito primeiro para poder exibir um extrato.")
        
        else:
            
            # Organizar as transações por tipo
            
            # Iterar o dicionário operacao, toda vez que encontrar uma transação de tipo "Depósito" coloque-a no dicionário "filtragem"
            for chave, valor in operacao.items():
                if chave.startswith('extrato'):  
                    
                    if valor['tipo'] == "Depósito":
                                            
                       # print(f"{valor['tipo']}:\n{valor['valor']:>15} {11 * '-'} {valor['data']:>17}") 
                        filtragem[f"extrato{y}"] = {"tipo": f"{valor['tipo']}", "valor": f"{valor['valor']}", "data": f"{valor['data']}"} 
                        y += 1
        
        # Iterar o dicionário operacao novamente, toda vez que encontrar uma transação de tipo "Saque" adicione-a no dicionário "filtragem"
        for chave, valor in operacao.items():
                if chave.startswith('extrato'):  
                    
                    if valor['tipo'] == "Saque":
                                            
                       # print(f"{valor['tipo']}:\n{valor['valor']:>15} {11 * '-'} {valor['data']:>17}") 
                        filtragem[f"extrato{y}"] = {"tipo": f"{valor['tipo']}", "valor": f"{valor['valor']}", "data": f"{valor['data']}"} 
                        y += 1
            
        print(f"\n {titulo:=^50}") # Centralizar o texto 
        
        # Exibir o dicionário filtragem
        for chave, valor in filtragem.items():
                if chave.startswith('extrato'):  
                                    
                    if iteracao == 0:
                        print(f"{valor['tipo']}:\n{valor['valor']:>15} {11 * '-'} {valor['data']:>17}") # Alinhar o texto a direita
                        iteracao = 1  
                    else:
                        if valor['tipo'].strip().lower() == "depósito":
                            print(f"{valor['valor']:>15} {11 * '-'} {valor['data']:>17}") # Alinhar o texto a direita
                                                    
                        elif valor['tipo'].strip().lower() == "saque" and iteracao == 1:
                            print(f"{valor['tipo']}: \n {valor['valor']:>10} {15 * '-'} {valor['data']:>17}") # Alinhar o texto a direita
                            iteracao = 2
                        else:
                            print(f" {valor['valor']:>10} {15 * '-'} {valor['data']:>17}")  # Alinhar o texto a direita
                                                    
            
        print(f"\nSaldo: R$ {operacao["saldo"]:.2f}")
        print("=" * 50)
        pe_pagina = f"{relogio()}: EXIBIR EXTRATO"
        iteracao = 0
        filtragem.clear()
        print(f"{pe_pagina:>50}") # Alinhar o texto a direita
            
    # Sair do aplicativo
    elif opcao == "q":
        print("Até logo!")
        break
    
    # Alterar a data da operação    
    elif opcao == "a":
        print("Forma da data: dd/mm/aaaa")
        print("Ela deve ser inferior que a data de hoje para poder fazer esse teste")
        operacao["reloginho"] = valor = str(input("Informe a data: "))
    
    # Exibir o BD do sistema
    elif opcao == "t":
        print("O BD do sistema está vazio." if not operacao else operacao)
        
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.\n")
