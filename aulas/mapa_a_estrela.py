import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def mostra_mapa(mapa, caminho):
    ncolunas = mapa["terreno"].shape[1]
    nlinhas = mapa["terreno"].shape[0]
    letras = np.array([["" for _ in range(ncolunas)] for _ in range(nlinhas)])
    for passo in caminho:
        letras[passo] = "X"
    letras[mapa["entrada"]] = 'E'
    letras[mapa["saida"]] = 'S'
    plt.figure(figsize=(2, 2))
    sns.heatmap(mapa['terreno'], annot=letras, fmt="", cbar=False, cmap="Blues",
                linewidths=0.1, linecolor='black', square=True)
    plt.show()


tam_x = 4
tam_y = 4
terreno = np.zeros((tam_y, tam_x))
entrada = (3, 1)
saida = (0, 0)
mapa = {"terreno": terreno, "entrada": entrada, "saida": saida}
# obstáculos:
terreno[3, 0] = 1
terreno[1, 0] = 1
terreno[1, 1] = 1
caminho = [(3, 1), (2, 1), (2, 2)]
mostra_mapa(mapa, caminho)
