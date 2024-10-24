def matriz_quadrada(matriz):
    return all(len(linha) == len(matriz) for linha in matriz)