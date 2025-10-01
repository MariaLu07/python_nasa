astros = []

while True:
    print("\n=== Sistema de Registro de Astros ===")
    print("1. Registrar novo astro")
    print("2. Consultar astros registrados")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        nome = input("Digite o nome do astro: ")
        descricao = input("Digite uma breve descrição: ")
        data_descoberta = input("Digite a data da descoberta (ex: 29/09/2025): ")

        print("\nEscolha o status do astro:")
        print("1. Ativo")
        print("2. Inativo")
        print("3. Em estudo")
        status_opcao = input("Digite 1, 2 ou 3: ")

        status = ""
        if status_opcao == '1':
            status = "Ativo"
        elif status_opcao == '2':
            status = "Inativo"
        elif status_opcao == '3':
            status = "Em estudo"
        else:
            status = "Indefinido"

        galaxia = input("Digite a galáxia em que o astro está localizado: ")

        registro = {
            'nome': nome,
            'descricao': descricao,
            'data_descoberta': data_descoberta,
            'status': status,
            'galaxia': galaxia
        }

        astros.append(registro)
        print("\nAstro registrado com sucesso!")

    elif escolha == '2':
        if astros:
            print("\n=== Astros Registrados ===")
            for i, astro in enumerate(astros, 1):
                print(f"\nAstro {i}:")
                print(f" Nome: {astro['nome']}")
                print(f" Descrição: {astro['descricao']}")
                print(f" Data da Descoberta: {astro['data_descoberta']}")
                print(f" Status: {astro['status']}")
                print(f" Galáxia: {astro['galaxia']}")
        else:
            print("\nNenhum astro registrado até o momento.")

    elif escolha == '3':
        print("\nSaindo do sistema. Até a próxima!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
