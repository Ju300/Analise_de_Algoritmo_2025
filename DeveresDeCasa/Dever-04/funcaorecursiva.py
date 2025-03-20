import math

def F(n):
    """
    Função recursiva que calcula F(n) = 2F(n-1) + n^2.
    :param n: Número inteiro positivo.
    :return: Valor de F(n).
    """
    if n == 1:
        return 2  # Caso base: F(1) = 2
    return 2 * F(n - 1) + n ** 2  # Chamada recursiva conforme a definição

def F_fechada(n):
    """
    Função que calcula F(n) usando a fórmula fechada para evitar recursão.
    :param n: Número inteiro positivo.
    :return: Valor de F(n).
    """
    return (2 ** (n - 1)) * 2 + sum(2 ** (n - i) * i ** 2 for i in range(2, n + 1))

# Solicita ao usuário um valor de n
n = int(input("Digite um valor de n: "))

# Calcula F(n) recursivamente
def resultado_recursivo():
    try:
        return F(n)
    except RecursionError:
        return "Erro: n muito grande para recursão"

# Calcula F(n) usando a fórmula fechada
resultado_fechado = F_fechada(n)

# Exibe os resultados
print(f"F({n}) via recursão: {resultado_recursivo()}")
print(f"F({n}) via fórmula fechada: {resultado_fechado}")
