# -*- coding: utf-8 -*-
"""quick_sort_com tempo_de_execucao_adaptado

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FDKUgUpqHxka2zmlz-Nxar9yhQ1WWEsw
"""

# Funções de tempo adaptadas pelo Brayan

import time
from random import randint


def quick_sort(arr):
    """
    Implementação do algoritmo Quick Sort para ordenar uma lista em ordem crescente.

    O Quick Sort é um algoritmo de ordenação baseado no conceito de "dividir e conquistar".
    Ele seleciona um pivô, particiona a lista em duas partes (menores e maiores que o pivô)
    e depois aplica recursivamente o mesmo processo a cada sublista.

    Complexidade média: O(n log n)
    Complexidade no pior caso: O(n²) (quando o pivô escolhido é o menor ou maior elemento)
    """

    # Caso base: Se a lista tem 0 ou 1 elemento, já está ordenada
    if len(arr) <= 1:
        return arr

    # Escolhe um pivô (aqui, usamos o último elemento da lista)
    pivot = arr[-1]

    # Particiona a lista em duas: elementos menores e maiores que o pivô
    menores = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    maiores = [x for x in arr[:-1] if x > pivot]   # Elementos maiores que o pivô

    # Chama recursivamente para ordenar as sublistas e junta o resultado

    return quick_sort(menores) + [pivot] + quick_sort(maiores)

print("teste do algoritmo")

lista = [34, 7, 23, 32, 5, 62, 32, 12, 90, 3]
print("Lista original:", lista)
print("Lista ordenada:", quick_sort(lista))

arr_100 = [randint(1, 100) for _ in range(100)]
arr_1000 = [randint(1, 1000) for _ in range(1000)]
arr_10000 = [randint(1, 10000) for _ in range(10000)]
arr_100000 = [randint(1, 100000) for _ in range(100000)]



print("calculando tempo")


tempoInicial = time.time()
quick_sort(arr_100)
tempoFinal = time.time()
print(f"tempo decorrido {tempoFinal-tempoInicial}")
tempoInicial = time.time()
quick_sort(arr_1000)
tempoFinal = time.time()
print(f"tempo decorrido {tempoFinal-tempoInicial}")
tempoInicial = time.time()
quick_sort(arr_10000)
tempoFinal = time.time()
print(f"tempo decorrido {tempoFinal-tempoInicial}")
tempoInicial = time.time()
quick_sort(arr_100000)
tempoFinal = time.time()
print(f"tempo decorrido {tempoFinal-tempoInicial}")