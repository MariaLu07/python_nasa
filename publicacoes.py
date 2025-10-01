publicacoes = []

while True:
    print("\n=== Sistema de Registro de Publicações ===")
    print("1. Registrar nova publicação")
    print("2. Consultar publicações registradas")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        titulo = input("Digite o título da publicação: ")
        autor = input("Digite o autor da publicação: ")
        data = input("Digite a data da publicação (ex: 29/09/2025): ")
        texto = input("Digite o texto da publicação: ")

        registro = {
            'titulo': titulo,
            'autor': autor,
            'data': data,
            'texto': texto
        }

        publicacoes.append(registro)
        print("\nPublicação registrada com sucesso!")

    elif escolha == '2':
        if publicacoes:
            print("\n=== Publicações Registradas ===")
            for i, pub in enumerate(publicacoes, 1):
                print(f"\nPublicação {i}:")
                print(f" Título: {pub['titulo']}")
                print(f" Autor: {pub['autor']}")
                print(f" Data: {pub['data']}")
                print(f" Texto: {pub['texto']}")
        else:
            print("\nNenhuma publicação registrada até o momento.")

    elif escolha == '3':
        print("\nSaindo do sistema. Até a próxima!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
