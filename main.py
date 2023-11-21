import random
import time

# Funções de Ordenação
def bubble_sort(arr):
    comparisons, assignments = 0, 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                assignments += 3  # Contamos as atribuições feitas durante a troca
    return comparisons, assignments

def insertion_sort(arr):
    comparisons, assignments = 0, 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
        arr[j + 1] = key
        assignments += 1
    return comparisons, assignments

def selection_sort(arr):
    comparisons, assignments = 0, 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        assignments += 3  # Contamos as atribuições feitas durante a troca
    return comparisons, assignments

import random
import time


# Funções de Ordenação (Não Eficientes)
def bubble_sort(arr):
    comparisons, assignments = 0, 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                assignments += 3  # Conta o número de atribuições feitas durante a troca
    return comparisons, assignments


def insertion_sort(arr):
    comparisons, assignments = 0, 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1  # Conta o número de atribuições feitas durante o deslocamento
            j -= 1
        arr[j + 1] = key
        assignments += 1
    return comparisons, assignments


def selection_sort(arr):
    comparisons, assignments = 0, 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        assignments += 3  # Conta o número de atribuições feitas durante a troca
    return comparisons, assignments


# Funções de Ordenação Eficientes (QuickSort, HeapSort, MergeSort)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

# Função para gerar listas
def generate_list(size, order):
    if order == "sorted":
        return list(range(1, size + 1))
    elif order == "reverse":
        return list(range(size, 0, -1))
    elif order == "almost_sorted":
        arr = list(range(1, size + 1))
        random_index = random.randint(0, size - 2)
        arr[random_index], arr[random_index + 1] = arr[random_index + 1], arr[random_index]
        return arr
    elif order == "random":
        return random.sample(range(1, size + 1), size)

# Função para imprimir listas
def print_list(arr):
    print(" ".join(map(str, arr)))

# Função para ordenar a lista com o algoritmo escolhido e medir o desempenho

def heap_sort(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        left = merge_sort(arr, low, mid)
        right = merge_sort(arr, mid + 1, high)

        return merge(left, right)


def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged
def run_sorting_algorithm(algorithm, arr):
    comparisons, assignments = 0, 0

    start_time = time.time()

    if algorithm == "bubble":
        comparisons, assignments = bubble_sort(arr)
    elif algorithm == "insertion":
        comparisons, assignments = insertion_sort(arr)
    elif algorithm == "selection":
        comparisons, assignments = selection_sort(arr)
    elif algorithm == "quick":
        arr = quick_sort(arr)
    elif algorithm == "heap":
        comparisons, assignments = heap_sort(arr)
    elif algorithm == "merge":
        comparisons, assignments = merge_sort(arr)

    end_time = time.time()

    execution_time = end_time - start_time

    return {
        "execution_time": execution_time,
        "comparisons": comparisons,
        "assignments": assignments,
    }

# Função para imprimir estatísticas
def print_statistics(results):
    print("\nEstatísticas:")
    print(f"Tempo de execução: {results['execution_time']:.6f} segundos")
    print(f"Número de comparações: {results['comparisons']}")
    print(f"Número de atribuições: {results['assignments']}")

if __name__ == "__main__":
    # Pedir informações ao usuário
    algorithm = input("Escolha o algoritmo (bubble, insertion, selection, quick, heap, merge): ").lower()
    order = input("Escolha o tipo de sequência (sorted, reverse, almost_sorted, random): ").lower()
    size = int(input("Escolha o tamanho da lista: "))

    # Gerar lista
    arr = generate_list(size, order)

    # Imprimir lista antes da ordenação
    print(f"Algoritmo: {algorithm}, Ordem: {order}")
    print(f"Lista antes da ordenação: {arr[:min(size, 10)]}...")

    # Medir desempenho e ordenar lista
    results = run_sorting_algorithm(algorithm, arr)

    # Imprimir lista após ordenação
    print(f"Lista após ordenação: {arr[:min(size, 10)]}...")

    # Imprimir estatísticas

    print_statistics(results)
    print("\n" + "=" * 40)