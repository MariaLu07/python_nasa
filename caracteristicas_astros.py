caracteristicas_astros = []

while True:
    print("\n=== Sistema de Registro de Características dos Astros ===")
    print("1. Registrar características de um astro")
    print("2. Consultar características registradas")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        massa = input("Digite a massa do astro (em Kg): ")
        raio = input("Digite o raio do astro (em Km): ")
        temperatura = input("Digite a temperatura do astro (em °C): ")
        distancia = input("Digite a distância da Terra (em anos-luz): ")
        composicao = input("Digite a composição do astro (ex: Hidrogênio e Hélio): ")

        registro = {
            'massa': massa,
            'raio': raio,
            'temperatura': temperatura,
            'distancia': distancia,
            'composicao': composicao
        }

        caracteristicas_astros.append(registro)
        print("\nCaracterísticas registradas com sucesso!")

    elif escolha == '2':
        if caracteristicas_astros:
            print("\n=== Características Registradas ===")
            for i, c in enumerate(caracteristicas_astros, 1):
                print(f"\nAstro {i}:")
                print(f" Massa: {c['massa']} Kg")
                print(f" Raio: {c['raio']} Km")
                print(f" Temperatura: {c['temperatura']} °C")
                print(f" Distância da Terra: {c['distancia']} anos-luz")
                print(f" Composição: {c['composicao']}")
        else:
            print("\nNenhuma característica registrada até o momento.")

    elif escolha == '3':
        print("\nSaindo do sistema. Até a próxima!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
