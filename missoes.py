missoes = []

while True:
    print("\n=== Sistema de Registro de Missões da NASA ===")
    print("1. Registrar nova missão")
    print("2. Consultar missões registradas")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        nome = input("Digite o nome da missão: ")
        descricao = input("Digite uma breve descrição da missão: ")
        data_inicio = input("Digite a data de início (ex: 20/07/2025): ")
        data_fim = input("Digite a data de término (ou previsto, ex: 20/08/2025): ")

        print("\nEscolha o status da missão:")
        print("1. Ativa")
        print("2. Concluída")
        print("3. Cancelada")
        print("4. Planejada")
        status_opcao = input("Digite 1, 2, 3 ou 4: ")

        status = ""
        if status_opcao == '1':
            status = "Ativa"
        elif status_opcao == '2':
            status = "Concluída"
        elif status_opcao == '3':
            status = "Cancelada"
        elif status_opcao == '4':
            status = "Planejada"
        else:
            status = "Indefinido"

        registro = {
            'nome': nome,
            'descricao': descricao,
            'data_inicio': data_inicio,
            'data_fim': data_fim,
            'status': status
        }

        missoes.append(registro)
        print("\nMissão registrada com sucesso!")

    elif escolha == '2':
        if missoes:
            print("\n=== Missões Registradas ===")
            for i, missao in enumerate(missoes, 1):
                print(f"\nMissão {i}:")
                print(f" Nome: {missao['nome']}")
                print(f" Descrição: {missao['descricao']}")
                print(f" Data de Início: {missao['data_inicio']}")
                print(f" Data de Fim: {missao['data_fim']}")
                print(f" Status: {missao['status']}")
        else:
            print("\nNenhuma missão registrada até o momento.")

    elif escolha == '3':
        print("\nSaindo do sistema. Até a próxima!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
