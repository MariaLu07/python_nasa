equipes = []

while True:
    print("\n=== Sistema de Registro de Equipes das Missões ===")
    print("1. Registrar equipe")
    print("2. Consultar equipes registradas")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        participantes = input("Digite os participantes da equipe (separe por vírgula): ")
        funcao = input("Digite a função da equipe (ex: exploração, pesquisa científica, suporte técnico): ")
        descricao = input("Digite uma breve descrição da equipe: ")

        registro = {
            'participantes': participantes,
            'funcao': funcao,
            'descricao': descricao
        }

        equipes.append(registro)
        print("\nEquipe registrada com sucesso!")

    elif escolha == '2':
        if equipes:
            print("\n=== Equipes Registradas ===")
            for i, e in enumerate(equipes, 1):
                print(f"\nEquipe {i}:")
                print(f" Participantes: {e['participantes']}")
                print(f" Função: {e['funcao']}")
                print(f" Descrição: {e['descricao']}")
        else:
            print("\nNenhuma equipe registrada até o momento.")

    elif escolha == '3':
        print("\nSaindo do sistema. Até a próxima!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
