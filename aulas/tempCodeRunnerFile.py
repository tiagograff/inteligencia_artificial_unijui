def mostra_mapa(mapa, caminho):
    ncolunas = mapa["terreno"].shape[1]
    nlinhas = mapa["terreno"].shape[0]
    # Matriz para anotações (letras) e posições percorridas
    letras = np.array([["" for _ in range(ncolunas)] for _ in range(nlinhas)])
    percorridos = np.zeros((nlinhas, ncolunas))

    for passo in caminho:
        letras[passo] = "X"
        # Marcar as posições percorridas com um valor intermediário
        percorridos[passo] = 0.5

    letras[mapa["entrada"]] = 'E'
    letras[mapa["saida"]] = 'S'

    # Adicionar as posições da entrada e saída com valores únicos
    percorridos[mapa["entrada"]] = 0.7
    percorridos[mapa["saida"]] = 0.7

    # Combine o terreno e os percorridos para criar o gradiente de cores
    mapa_comb = mapa["terreno"] + percorridos

    plt.figure(figsize=(6, 6))
    sns.heatmap(mapa_comb, annot=letras, fmt="", cbar=False, cmap="Blues",
                linewidths=0.1, linecolor='black', square=True)
    plt.show()