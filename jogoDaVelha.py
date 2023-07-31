def jogoDaVelha():
    print("Jogo da Velha\n")

    print("Cada jogador escolherá a posição que quer colocar sua jogada.")
    print("O jogador 1 jogará como \"X\" e o jogador 2 jogará como \"O\".")
    print("Boa sorte!")

    # Método para criar um tabuleiro nxn
    def criaTabuleiro(dimensaoTabuleiro):
        tabuleiro = []
        linhaTab = []
        colunaTab = list(range(1, (dimensaoTabuleiro*dimensaoTabuleiro)+1, 1))
        contadorAdicoes = 0
        adicionador = 1
        while (contadorAdicoes < dimensaoTabuleiro):
            linhaTab = list(
                range(adicionador, adicionador+dimensaoTabuleiro, 1))
            tabuleiro.append(linhaTab)
            adicionador += dimensaoTabuleiro
            contadorAdicoes += 1
        return tabuleiro

    # Método para exibir o tabuleiro

    def imprimeTabuleiro(tabuleiro):
        contadorLinhasSeparadoras = 0
        for linha in tabuleiro:
            for coluna in range(len(linha)):
                print(f"{linha[coluna]}", end='')
                if (coluna < len(linha)-1):
                    print(" | ", end='')
            print()

            contadorLinhasSeparadoras += 1
            if (contadorLinhasSeparadoras < len(tabuleiro)):
                print("-" * (len(tabuleiro)*len(tabuleiro)))

    # Método para que o usuário escolha sua posição de jogada
    def quemJoga(jogadorDaVez, jog1, jog2, simboloJogDaVez, simboloJog1, simboloJog2, tabuleiro):
        completou = len(tabuleiro)*len(tabuleiro)
        contagemDeJogadas = 1
        while (contagemDeJogadas <= completou):
            print("Jogador 1 (" + simboloJogDaVez + ") - Sua vez\n")
            imprimeTabuleiro(tabuleiro)
            print()
            msg = "Digite a posição em que deseja inserir:"
            posicao = int(input(msg))
            while (not (1 <= posicao <= 9)):
                print("Insira um número que pertença às posições disponíveis!")
                posicao = int(input(msg))

            for linha in range(len(tabuleiro)):
                for coluna in range(linha):
                    if (coluna == simboloJog1 or coluna == simboloJog2):
                        print(
                            "Esta posição já foi escolhida! Escolha outra posição.")
                        quemJoga(jogadorDaVez, jog1, jog2, simboloJogDaVez,
                                 simboloJog1, simboloJog2, tabuleiro)
                    elif (tabuleiro):
                        coluna = simboloJogDaVez

            contagemDeJogadas += 1
            jogadorDaVez = jog2
            simboloJogDaVez = simboloJog2

            print("Jogador 2 (" + simboloJogDaVez + ") - Sua vez\n")
            imprimeTabuleiro(tabuleiro)
            print()
            msg = "Digite a posição em que deseja inserir:"
            posicao = int(input(msg))
            while (not (1 <= posicao <= 9)):
                print("Insira um número que pertença as posições disponíveis!")
                posicao = int(input(msg))

            for linha in tabuleiro:
                for coluna in range(len(linha)):
                    if posicao == linha[coluna]:
                        if (tabuleiro[linha][coluna] == simboloJog1 or tabuleiro[linha][coluna] == simboloJog2):
                            print(
                                "Esta posição já foi escolhida! Escolha outra posição.")
                            quemJoga(jogadorDaVez, jog1, jog2, simboloJogDaVez,
                                     simboloJog1, simboloJog2, tabuleiro)
                        else:
                            tabuleiro[linha][coluna] = simboloJogDaVez
            contagemDeJogadas += 1
            jogadorDaVez = jog1
            simboloJogDaVez = simboloJog1

    # Início do jogo
    tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    jog1 = 1
    jog2 = 2
    jogadorDaVez = 0
    X = "X"
    O = "O"
    simboloJogDaVez = X
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            while (tabuleiro[linha][coluna] != X and tabuleiro[linha][coluna] != O):
                quemJoga(jogadorDaVez, jog1, jog2,
                         simboloJogDaVez, X, O, tabuleiro)

    imprimeTabuleiro(tabuleiro)
    print("Fim de Jogo!")