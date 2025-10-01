participantes = []

while True:
    print("\n=== Sistema de Registro de Participantes das Missões ===")
    print("1. Registrar participante")
    print("2. Consultar participantes registrados")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        nome = input("Digite o nome do participante: ")
        nacionalidade = input("Digite a nacionalidade: ")
        profissao = input("Digite a profissão: ")
        especialidade = input("Digite a especialidade (ex: astrofísica, engenharia aeroespacial): ")
        instituicao = input("Digite a instituição da NASA vinculada: ")

        registro = {
            'nome': nome,
            'nacionalidade': nacionalidade,
            'profissao': profissao,
            'especialidade': especialidade,
            'instituicao': instituicao
        }

        participantes.append(registro)
        print("\nParticipante registrado com sucesso!")

    elif escolha == '2':
        if participantes:
            print("\n=== Participantes Registrados ===")
            for i, p in enumerate(participantes, 1):
                print(f"\nParticipante {i}:")
                print(f" Nome: {p['nome']}")
                print(f" Nacionalidade: {p['nacionalidade']}")
                print(f" Profissão: {p['profissao']}")
                print(f" Especialidade: {p['especialidade']}")
                print(f" Instituição da NASA: {p['instituicao']}")
        else:
            print("\nNenhum participante registrado até o momento.")

    elif escolha == '3':
        print("\nSaindo do sistema. Até a próxima!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
