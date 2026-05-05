
def lista_somas(n:int) -> list:
    """
    Calcula os somatórios de 0 até n:
        lista_somas[i] = somatório de 0 até i, i >= 0
        ou
        lista_somas[0] = 0
        lista_somas[i] = lista_somas[i-1] + i, i > 0
    :param n: int
    :return: list[int]
    :raises ValueError: se n for negativo
    """
    if n >= 0:
        lista_sms = [0]
        for i in range(1,n+1):
            soma = lista_sms[i-1] + i
            lista_sms.append(soma)
        return lista_sms
    else:
        raise ValueError("Erro: número deve ser não negativo (>= 0)!")
