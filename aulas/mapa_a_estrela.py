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
    plt.figure(figsize=(3, 3))
    sns.heatmap(mapa['terreno'], annot=letras, fmt="", cbar=False, cmap="Blues",
                linewidths=0.1, linecolor='black', square=True)
    plt.show()


tam_x = 15
tam_y = 15
terreno = np.zeros((tam_y, tam_x))
entrada = (14, 6)
saida = (0, 6)
mapa = {"terreno": terreno, "entrada": entrada, "saida": saida}
# obstáculos:
terreno[6, 5] = 1
terreno[7, 5] = 1
terreno[8, 5] = 1
terreno[9, 5] = 1
terreno[10, 5] = 1
terreno[11, 5] = 1
terreno[12, 5] = 1
terreno[13, 5] = 1
terreno[6, 7] = 1
terreno[7, 7] = 1
terreno[8, 7] = 1
terreno[9, 7] = 1
terreno[6, 6] = 1
terreno[9, 4] = 1
terreno[9, 3] = 1
terreno[9, 2] = 1
caminho = [entrada]
mostra_mapa(mapa, caminho)
