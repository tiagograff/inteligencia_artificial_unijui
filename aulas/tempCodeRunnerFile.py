    if op == 'e' and i > 0:
        res[i][j] = res[i][j - 1]
        res[i][j - 1] = 0