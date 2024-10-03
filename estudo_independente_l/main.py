numero_alvo = 51
intervalo_inicial = (1, 100)


def aplica_operacao(estado, operacao):
    intervalo = estado["intervalo"]
    palpite_atual = estado["palpite"]

    if operacao == "menor":
        novo_intervalo = (intervalo[0], palpite_atual - 1)
    elif operacao == "maior":
        novo_intervalo = (palpite_atual + 1, intervalo[1])

    novo_palpite = (novo_intervalo[0] + novo_intervalo[1]) // 2

    novo_estado = {
        "intervalo": novo_intervalo,
        "palpite": novo_palpite,

        "tentativas": estado["tentativas"] + [palpite_atual],

        "quantidade_tentativas": estado["quantidade_tentativas"] + 1,

        "operacoes": estado["operacoes"] + [(palpite_atual, operacao)]
    }
    return novo_estado


def get_ops_validas(estado):
    ops_validas = []
    intervalo = estado["intervalo"]
    palpite = estado["palpite"]

    if palpite > intervalo[0]:
        ops_validas.append("menor")
    if palpite < intervalo[1]:
        ops_validas.append("maior")

    return ops_validas


def verifica_solucao(estado):
    return estado["palpite"] == numero_alvo


def busca_a_estrela(estado_ini, max_niveis):
    folhas = []
    raiz = {
        "estado": estado_ini,
        "ops": [],
        "f": 0
    }

    folhas.append(raiz)
    niveis = 0

    while niveis < max_niveis:
        niveis += 1
        melhor_folha = folhas[0]

        for folha in folhas:
            if folha["f"] < melhor_folha["f"]:
                melhor_folha = folha

        folhas.remove(melhor_folha)
        operacoes = get_ops_validas(melhor_folha["estado"])

        for op in operacoes:
            estado = aplica_operacao(melhor_folha["estado"], op)

            nova_folha = {
                "estado": estado,
                "ops": melhor_folha["ops"] + [op],
                "f": 0
            }
            f = estado["quantidade_tentativas"]
            nova_folha["f"] = f
            folhas.append(nova_folha)

            if verifica_solucao(nova_folha["estado"]):
                return nova_folha["estado"], nova_folha["ops"]

    return None


estado_ini = {
    "intervalo": intervalo_inicial,
    "palpite": (intervalo_inicial[0] + intervalo_inicial[1]) // 2,
    "tentativas": [],
    "quantidade_tentativas": 0,
    "operacoes": []  #
}

max_niveis = 100
estado, ops = busca_a_estrela(estado_ini, max_niveis)

print(f'\npalpite final: {estado["palpite"]}')
print(f'\noperações: {ops}')
print(f'\nquantidade de tentativas: {estado["quantidade_tentativas"]}')
print('\n-- palpites e operações registradas --\n')
for palpite, operacao in estado["operacoes"]:
    print(f'palpite: {palpite}, operação: {operacao}')
