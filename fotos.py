fotos = []

while True:
    print("\n=== Sistema de Registro de Fotos ===")
    print("1. Registrar nova foto")
    print("2. Consultar fotos registradas")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        url = input("Digite a URL da imagem: ")
        data = input("Digite a data do registro (ex: 29/09/2025): ")
        fonte = input("Digite a fonte da imagem (ex: NASA, telescópio Hubble, satélite): ")
        descricao = input("Digite uma descrição para a foto: ")

        registro = {
            'url': url,
            'data': data,
            'fonte': fonte,
            'descricao': descricao
        }

        fotos.append(registro)
        print("\nFoto registrada com sucesso!")

    elif escolha == '2':
        if fotos:
            print("\n=== Fotos Registradas ===")
            for i, foto in enumerate(fotos, 1):
                print(f"\nFoto {i}:")
                print(f" URL: {foto['url']}")
                print(f" Data: {foto['data']}")
                print(f" Fonte: {foto['fonte']}")
                print(f" Descrição: {foto['descricao']}")
        else:
            print("\nNenhuma foto registrada até o momento.")

    elif escolha == '3':
        print("\nSaindo do sistema. Até a próxima!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
