import copy


def aplica_operacao(qc, op):
    res = copy.deepcopy(qc)
    i = 0
    j = 0
    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j] == 0:
                break
        if res[i][j] == 0:
            break
    if op == "c" and i > 0:
        res[i][j] = res[i-1][j]
        res[i-1][j] = 0
    if op == "b" and i < 2:
        res[i][j] = res[i+1][j]
        res[i+1][j] = 0
    if op == "e" and j > 0:
        res[i][j] = res[i][j-1]
        res[i][j-1] = 0
    if op == "d" and j < 2:
        res[i][j] = res[i][j+1]
        res[i][j+1] = 0

    return res


def mostra_qc(qc):
    texto = ""
    for i in range(len(qc)):
        for j in range(len(qc[i])):
            texto = texto+str(qc[i][j])
        texto = texto+"\n"
    print(texto)


def verifica_solucao(estado):
    return estado == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


def busca_amplitude(estado_ini, operacoes, max_niveis):
    quant_estados = 0
    folhas = []
    novas_folhas = []
    raiz = {"estado": estado_ini, "caminho": []}
    folhas.append(raiz)
    niveis = 0
    while (niveis < max_niveis):
        niveis = niveis+1
        novas_folhas = []
        for folha in folhas:
            for op in operacoes:
                estado = aplica_operacao(folha["estado"], op)
                quant_estados += 1
                nova_folha = {"estado": estado,
                              "caminho": folha["caminho"]+[op]}
                novas_folhas.append(nova_folha)
                if verifica_solucao(nova_folha["estado"]) == True:
                    return {"estado": nova_folha["estado"],
                            "caminho": nova_folha["caminho"],
                            "quant_estados": quant_estados}
        folhas = novas_folhas
    return None


def calc_c(folha):
    return len(folha["caminho"])


def calc_h(folha):
    h = 0
    i = 0
    for linha in folha["estado"]:
        for elemento in linha:
            if elemento != i and i != 0:
                h = h+1
            i = i+1
    return h


def busca_a_estrela(estado_ini, operacoes, max_niveis):
    quant_estados = 0
    folhas = []
    novas_folhas = []
    raiz = {"estado": estado_ini, "caminho": [], "f": 0}
    folhas.append(raiz)
    niveis = 0
    while (niveis < max_niveis):
        niveis = niveis+1
        melhor_folha = folhas[0]
        # ----escolhe a melhor folha
        for folha in folhas:
            if folha["f"] < melhor_folha["f"]:
                melhor_folha = folha
        # ---------------------------
        folhas.remove(melhor_folha)
        for op in operacoes:
            estado = aplica_operacao(melhor_folha["estado"], op)
            quant_estados += 1
            nova_folha = {"estado": estado,
                          "caminho": melhor_folha["caminho"]+[op], "f": 0}
            f = calc_c(nova_folha)+calc_h(nova_folha)
            nova_folha["f"] = f
            folhas.append(nova_folha)
            if verifica_solucao(nova_folha["estado"]) == True:
                return {"estado": nova_folha["estado"],
                        "caminho": nova_folha["caminho"],
                        "quant_estados": quant_estados}
    return None


qc = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
ops = ["d", "d", "b"]
for op in ops:
    qc = aplica_operacao(qc, op)
print("estado inicial:")
mostra_qc(qc)
operacoes = ["b", "c", "d", "e"]
max_niveis = 100000
res = busca_a_estrela(qc, operacoes, max_niveis)

if res != None:
    for k in res:
        print(k, res[k])
    print("\n")
    print("estado inicial:")
    mostra_qc(qc)
    for op in res["caminho"]:
        qc = aplica_operacao(qc, op)
        print(op)
        mostra_qc(qc)
else:
    print("Não encontrou a solução")
