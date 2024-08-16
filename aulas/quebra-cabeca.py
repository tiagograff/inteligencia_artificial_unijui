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
    quantidade_estados = 0
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
                quantidade_estados += 1
                nova_folha = {"estado": estado,
                              "caminho": folha["caminho"]+[op]}
                novas_folhas.append(nova_folha)
                if verifica_solucao(nova_folha["estado"]) == True:
                    return {'estado': nova_folha["estado"], 'caminho': nova_folha["caminho"], 'quantidade de estados': quantidade_estados}
        folhas = novas_folhas
    return None


qc = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
ops = ['d', 'b', 'd', 'c', 'e', 'e', 'b', 'd', 'c', 'e', 'b']
for op in ops:
    qc = aplica_operacao(qc, op)

qc = aplica_operacao(qc, "d")
qc = aplica_operacao(qc, "b")
print("estado inicial:")
mostra_qc(qc)
operacoes = ["b", "c", "d", "e"]
max_niveis = 100
res = busca_amplitude(qc, operacoes, max_niveis)
if res != None:
    for k in res:
        print(k, res[k])
        print("estado inicial:")
        mostra_qc(qc)
        for op in res["caminho"]:
            qc = aplica_operacao(qc, op)
            print(op)
            mostra_qc(qc)
else:
    print('não encontrou a solução')
