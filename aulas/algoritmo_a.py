import copy
from mapa_a_estrela import mostra_mapa, mapa


def aplica_operacao(estado, op):
    ncolunas = estado["mapa"]["terreno"].shape[1]
    nlinhas = estado["mapa"]["terreno"].shape[0]
    pos = estado["caminho"][-1]
    passo = (pos[0], pos[1])
    if op == "N":
        if pos[0] > 0:
            if estado["mapa"]["terreno"][pos[0]-1, pos[1]] < 1:
                passo = (pos[0]-1, pos[1])
    if op == "S":
        if pos[0] < nlinhas-1:
            if estado["mapa"]["terreno"][pos[0]+1, pos[1]] < 1:
                passo = (pos[0]+1, pos[1])
    if op == "L":
        if pos[1] < ncolunas-1:
            if estado["mapa"]["terreno"][pos[0], pos[1]+1] < 1:
                passo = (pos[0], pos[1]+1)
    if op == "O":
        if pos[1] > 0:
            if estado["mapa"]["terreno"][pos[0], pos[1]-1] < 1:
                passo = (pos[0], pos[1]-1)
    novo_caminho = copy.deepcopy(estado["caminho"])+[passo]
    novo_estado = {"mapa": mapa, "caminho": novo_caminho}
    return novo_estado
# ---------------------------------------------------


estado_ini = {"mapa": mapa, "caminho": [(3, 1)]}
mostra_mapa(estado_ini["mapa"], estado_ini["caminho"])
estado = aplica_operacao(estado_ini, "L")
estado = aplica_operacao(estado, "L")
estado = aplica_operacao(estado, "N")
estado = aplica_operacao(estado, "N")
mostra_mapa(estado["mapa"], estado["caminho"])
