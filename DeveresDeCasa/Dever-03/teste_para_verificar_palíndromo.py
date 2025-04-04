# -*- coding: utf-8 -*-
"""Teste_para_verificar_palíndromo

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bfdU7ncZhzJtGi-3FTke-eilBhdIDUJt
"""

def eh_palindromo(arr, esquerda=0, direita=None):
    """
    Função recursiva para verificar se um array é um palíndromo.
    :param arr: Lista de elementos a serem verificados.
    :param esquerda: Índice inicial (padrão: 0).
    :param direita: Índice final (padrão: None, ajustado para o último índice).
    :return: True se for palíndromo, False caso contrário.
    """
    if direita is None:
        direita = len(arr) - 1  # Inicializa o índice da direita como o último índice do array

    if esquerda >= direita:
        return True  # Condição de parada: quando os índices se cruzam ou se igualam, significa que é um palíndromo

    if arr[esquerda] != arr[direita]:
        return False  # Se os elementos nas extremidades não forem iguais, não é um palíndromo

    return eh_palindromo(arr, esquerda + 1, direita - 1)  # Chamada recursiva reduzindo os índices

# Testes
testes = [
    ([0, 1, 2, 3, 2, 1, 0], "É palíndromo"),
    (["a", "b", "b", "a"], "É palíndromo"),
    (["a", "b", "c", "b", "a"], "É palíndromo"),
    (["a", "b", "c", "f", "b", "a"], "Não é palíndromo")
]

for arr, esperado in testes:
    resultado = "É palíndromo" if eh_palindromo(arr) else "Não é palíndromo"
    print(f"{arr} -> {resultado}")