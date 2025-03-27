
import sympy as sp

# 1. Complexidade do Merge Sort: O(n log n)

def merge_sort(arr):
    """
    Implementação do Merge Sort com análise de complexidade.
    :param arr: Lista de elementos a serem ordenados.
    :return: Lista ordenada.
    """
    if len(arr) <= 1:
        return arr  # Caso base: listas de tamanho 1 já estão ordenadas

    mid = len(arr) // 2  # Divide a lista ao meio
    left = merge_sort(arr[:mid])  # Recursão na metade esquerda
    right = merge_sort(arr[mid:])  # Recursão na metade direita

    return merge(left, right)  # Junta as duas metades ordenadas

def merge(left, right):
    """
    Função auxiliar que combina duas listas ordenadas.
    :param left: Lista ordenada da esquerda.
    :param right: Lista ordenada da direita.
    :return: Lista ordenada combinada.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):  # Percorre as listas e ordena
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])  # Adiciona elementos restantes da esquerda
    result.extend(right[j:])  # Adiciona elementos restantes da direita

    return result

# Testando Merge Sort
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(f"Array ordenado pelo Merge Sort: {sorted_arr}")
print("Complexidade do Merge Sort: O(n log n)\n")


# 2. Complexidade da Multiplicação de Matrizes: O(n^3)

import numpy as np

def matrix_multiplication(A, B):
    """
    Multiplicação tradicional de matrizes O(n^3).
    :param A: Matriz A de tamanho n x n.
    :param B: Matriz B de tamanho n x n.
    :return: Matriz resultante AxB.
    """
    n = len(A)
    C = [[0] * n for _ in range(n)]  # Inicializa matriz resultado com zeros

    for i in range(n):  # Percorre as linhas da matriz A
        for j in range(n):  # Percorre as colunas da matriz B
            for k in range(n):  # Soma os produtos das entradas correspondentes
                C[i][j] += A[i][k] * B[k][j]

    return C

# Testando Multiplicação de Matrizes
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = matrix_multiplication(A, B)
print("Matriz resultante da multiplicação AxB:")
for row in C:
    print(row)
print("Complexidade da multiplicação de matrizes: O(n^3)\n")


# 3. Resolvendo Recorrências com o Teorema Mestre

import sympy as sp

def solve_recurrence(a, b, f_n):
    """
    Resolve a complexidade de recorrências na forma T(n) = aT(n/b) + f(n)
    utilizando o Teorema Mestre.
    :param a: Número de subproblemas.
    :param b: Fator de divisão do tamanho do problema.
    :param f_n: Função de crescimento adicional.
    :return: Complexidade assintótica da recorrência.
    """
    n = sp.Symbol('n')  # Define a variável simbólica n
    f_n = sp.simplify(f_n)  # Simplifica f(n)

    # Calculando log_b(a)
    log_b_a = (sp.log(a) / sp.log(b)).evalf()  # Avalia numericamente log_b(a)

    # Comparando f(n) com O(n^(log_b(a)))
    complexity = f"O(n^{log_b_a})"

    if f_n.is_polynomial(n):
        degree = sp.degree(f_n, n)

        # Converte grau para valor numérico antes da comparação
        if float(degree) > float(log_b_a):  
            complexity = f"O({f_n})"
        elif float(degree) == float(log_b_a):
            complexity = f"O({f_n} log n)"

    return complexity

# Recorrência 1: T(n) = 2T(n/4) + sqrt(n)
print("Resolvendo T(n) = 2T(n/4) + sqrt(n):")
print("Complexidade:", solve_recurrence(2, 4, sp.sqrt(sp.Symbol('n'))))

# Recorrência 2: T(n) = 2T(n/4) + n
print("\nResolvendo T(n) = 2T(n/4) + n:")
print("Complexidade:", solve_recurrence(2, 4, sp.Symbol('n')))

# Recorrência 3: T(n) = 16T(n/4) + n^2
print("\nResolvendo T(n) = 16T(n/4) + n^2:")
print("Complexidade:", solve_recurrence(16, 4, sp.Symbol('n')**2))
