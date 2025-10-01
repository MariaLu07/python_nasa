instrumentos = []

while True:
    print("\n=== Sistema de Registro de Instrumentos de Missões ===")
    print("1. Registrar instrumento")
    print("2. Consultar instrumentos registrados")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        nome = input("Digite o nome do instrumento: ")
        missao = input("Digite a missão em que o instrumento foi utilizado: ")
        tipo = input("Digite o tipo do instrumento: ")
        data_uso = input("Digite a data de uso do instrumento (ex: 15/08/2025): ")

        registro = {
            'nome': nome,
            'missao': missao,
            'tipo': tipo,
            'data_uso': data_uso
        }

        instrumentos.append(registro)
        print("\nInstrumento registrado com sucesso!")

    elif escolha == '2':
        if instrumentos:
            print("\n=== Instrumentos Registrados ===")
            for i, inst in enumerate(instrumentos, 1):
                print(f"\nInstrumento {i}:")
                print(f" Nome: {inst['nome']}")
                print(f" Missão: {inst['missao']}")
                print(f" Tipo: {inst['tipo']}")
                print(f" Data de uso: {inst['data_uso']}")
        else:
            print("\nNenhum instrumento registrado até o momento.")

    elif escolha == '3':
        print("\nSaindo do sistema. Até a próxima!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
