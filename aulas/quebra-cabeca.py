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

    if op == 'c' and i > 0:
        res[i][j] = res[i - 1][j]
        res[i-1][j] = 0

    if op == 'b' and i < 2:
        res[i][j] = res[i + 1][j]
        res[i+1][j] = 0

    if op == 'e' and j > 0:
        res[i][j] = res[i][j - 1]
        res[i][j - 1] = 0

    if op == 'd' and j < 2:
        res[i][j] = res[i][j + 1]
        res[i][j + 1] = 0

    return res


def mostra_qc(qc):
    texto = ""
    for i in range(len(qc)):
        for j in range(len(qc[i])):
            texto = texto + str(qc[i][j])
        texto = texto + '\n'
    print(texto)


qc = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
mostra_qc(qc)
qc = aplica_operacao(qc, 'b')
mostra_qc(qc)
qc = aplica_operacao(qc, 'd')
mostra_qc(qc)
qc = aplica_operacao(qc, 'c')
mostra_qc(qc)
qc = aplica_operacao(qc, 'e')
mostra_qc(qc)
