def rotacionar_90_horario(matriz):
    return [list(reversed(coluna)) for coluna in zip(*matriz)]