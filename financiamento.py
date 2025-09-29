financiamentos = []

while True:
    print("\n=== Sistema de Registro de Financiamentos ===")
    print("1. Registrar novo financiamento")
    print("2. Consultar financiamentos registrados")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        orcamento = input("Digite o orçamento estimado (ex: US$ 500 milhões): ")
        custo_final = input("Digite o custo final (ex: US$ 480 milhões): ")

        print("\nEscolha a fonte do financiamento:")
        print("1. Governo")
        print("2. Agência Espacial")
        print("3. Parcerias Privadas")
        fonte_opcao = input("Digite 1, 2 ou 3: ")

        fonte = ""
        if fonte_opcao == '1':
            fonte = "Governo"
        elif fonte_opcao == '2':
            fonte = "Agência Espacial"
        elif fonte_opcao == '3':
            fonte = "Parcerias Privadas"
        else:
            fonte = "Indefinido"

        registro = {
            'orcamento_estimado': orcamento,
            'custo_final': custo_final,
            'fonte': fonte
        }

        financiamentos.append(registro)
        print("\nFinanciamento registrado com sucesso!")

    elif escolha == '2':
        if financiamentos:
            print("\n=== Financiamentos Registrados ===")
            for i, f in enumerate(financiamentos, 1):
                print(f"\nFinanciamento {i}:")
                print(f" Orçamento Estimado: {f['orcamento_estimado']}")
                print(f" Custo Final: {f['custo_final']}")
                print(f" Fonte: {f['fonte']}")
        else:
            print("\nNenhum financiamento registrado até o momento.")

    elif escolha == '3':
        print("\nSaindo do sistema. Até a próxima!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
