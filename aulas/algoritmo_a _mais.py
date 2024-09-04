import copy
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def aplica_operacao(estado, op):
    pos = estado["caminho"][-1]
    ops = {
        "N": (-1, 0), "S": (1, 0), "L": (0, 1), "O": (0, -1),
        "NE": (-1, 1), "NO": (-1, -1), "SE": (1, 1), "SO": (1, -1)
    }
    passo = (pos[0] + ops[op][0], pos[1] + ops[op][1])
    novo_caminho = copy.deepcopy(estado["caminho"]) + [passo]
    novo_estado = {"mapa": estado["mapa"], "caminho": novo_caminho}
    return novo_estado


def get_ops_validas(estado):
    ncolunas = estado["mapa"]["terreno"].shape[1]
    nlinhas = estado["mapa"]["terreno"].shape[0]
    pos = estado["caminho"][-1]
    ops = {
        "N": (-1, 0), "S": (1, 0), "L": (0, 1), "O": (0, -1),
        "NE": (-1, 1), "NO": (-1, -1), "SE": (1, 1), "SO": (1, -1)
    }
    ops_validas = []
    for op in ops:
        nova_pos = (pos[0] + ops[op][0], pos[1] + ops[op][1])
        if 0 <= nova_pos[0] < nlinhas and 0 <= nova_pos[1] < ncolunas:
            if estado["mapa"]["terreno"][nova_pos] < 1 and nova_pos not in estado["caminho"]:
                ops_validas.append(op)
    return ops_validas


def verifica_solucao(estado):
    return estado["caminho"][-1] == estado["mapa"]["saida"]


def calc_c(estado):
    return len(estado["caminho"])


def calc_h(estado):
    s = estado["mapa"]["saida"]
    p = estado["caminho"][-1]
    return abs(s[0] - p[0]) + abs(s[1] - p[1])


def busca_a_estrela(estado_ini, max_niveis):
    quant_estados = 0
    folhas = [{"estado": estado_ini, "ops": [], "f": 0}]
    niveis = 0
    caminhos_percorridos = []

    while niveis < max_niveis:
        niveis += 1
        melhor_folha = min(folhas, key=lambda f: f["f"])
        folhas.remove(melhor_folha)
        operacoes = get_ops_validas(melhor_folha["estado"])

        for op in operacoes:
            estado = aplica_operacao(melhor_folha["estado"], op)
            quant_estados += 1
            nova_folha = {"estado": estado,
                          "ops": melhor_folha["ops"] + [op], "f": 0}
            nova_folha["f"] = calc_c(
                nova_folha["estado"]) + calc_h(nova_folha["estado"])
            folhas.append(nova_folha)

            caminhos_percorridos.append(nova_folha["estado"]["caminho"])

            if verifica_solucao(nova_folha["estado"]):
                return nova_folha["estado"], nova_folha["ops"], quant_estados, caminhos_percorridos

    return None, None, quant_estados, caminhos_percorridos


def mostra_mapa(mapa, caminhos_percorridos, caminho_final):
    ncolunas = mapa["terreno"].shape[1]
    nlinhas = mapa["terreno"].shape[0]
    letras = np.array([["" for _ in range(ncolunas)] for _ in range(nlinhas)])
    percorridos = np.zeros((nlinhas, ncolunas))

    for caminho in caminhos_percorridos:
        for passo in caminho:
            percorridos[passo] = max(
                percorridos[passo], 0.3)

    for passo in caminho_final:
        percorridos[passo] = 0.6
        letras[passo] = "X"

    letras[mapa["entrada"]] = 'E'
    letras[mapa["saida"]] = 'S'

    percorridos[mapa["entrada"]] = 0.7
    percorridos[mapa["saida"]] = 0.7

    mapa_comb = mapa["terreno"] + percorridos

    plt.figure(figsize=(6, 6))
    sns.heatmap(mapa_comb, annot=letras, fmt="", cbar=False, cmap="Blues",
                linewidths=0.1, linecolor='black', square=True)
    plt.show()


tam_x = 15
tam_y = 15
terreno = np.zeros((tam_y, tam_x))
entrada = (14, 6)
saida = (0, 6)
mapa = {"terreno": terreno, "entrada": entrada, "saida": saida}

obstaculos = [
    (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5),
    (6, 7), (7, 7), (8, 7), (9, 7), (6, 6), (9, 4), (9, 3), (9, 2)
]
for obstaculo in obstaculos:
    terreno[obstaculo] = 1

estado_ini = {"mapa": mapa, "caminho": [entrada]}
mostra_mapa(mapa, [], [entrada])
max_niveis = 100000
resultado, _, quant_estados, caminhos_percorridos = busca_a_estrela(
    estado_ini, max_niveis)

if resultado:
    mostra_mapa(resultado["mapa"], caminhos_percorridos, resultado["caminho"])
    print("Quantidade de estados explorados:", quant_estados)
else:
    print("Não foi possível encontrar uma solução.")
