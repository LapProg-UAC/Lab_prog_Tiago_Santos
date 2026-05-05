def funcao(n:int) -> int:
    """
    Calcula o valor da função f(n) = 2 * n + 1
    :param n: int
    :return: int
    """
    if n < 0:
        raise ValueError("Erro: número deve ser não negativo (>= 0)!")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * funcao(n-2) + funcao(n-1)