
def ensinar():
    pergunta = input("Digite a pergunta: ").strip().lower()
    resposta = input("Digite a resposta: ").strip().lower()

    with open("cerebro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{pergunta}-{resposta}\n")


def conversar():
    fala = input("Você: ").strip().lower()
    encontrou = False

    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            dados = linha.strip().split("-", 1)

            if len(dados) == 2:
                pergunta_salva, resposta_salva = dados

                if fala == pergunta_salva:
                    print(f"bot: {resposta_salva}")
                    encontrou = True
                    break

        if not encontrou:
            print("bot: Desculpe, não sei a resposta. Use a opção 2 para me ensinar.")

    except FileNotFoundError:
        print("bot: Meu cérebro está vazio! Me ensine algo primeiro.")


def listar_conhecimento():
    base_dados = []

    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            dados = linha.strip().split("-", 1)

            if len(dados) == 2:
                base_dados.append((dados[0], dados[1]))

        base_dados.sort()

        print("\n--- MEMÓRIA DO PYBOT (ORDENADA) ---")

        for item in base_dados:
            print(f"Pergunta: {item[0]} -> Resposta: {item[1]}")

    except FileNotFoundError:
        print("Nenhum dado cadastrado ainda.")

while True:
    print("\n--- PYBOT ---")
    print("1 - Conversar")
    print("2 - Ensinar")
    print("3 - Listar conhecimentos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        conversar()

    elif opcao == "2":
        ensinar()

    elif opcao == "3":
        listar_conhecimento()

    elif opcao == "0":
        print("Encerrando o PyBot...")
        break

    else:
        print("Opção inválida!")
