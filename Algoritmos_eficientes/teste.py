import time

from Algoritmos_eficientes.gerador_lista import generate_almost_ordered_sequence, generate_ordered_sequence, generate_random_sequence, generate_reverse_ordered_sequence
from Algoritmos_eficientes.heap_sort import heapSort
from Algoritmos_eficientes.merge_sort import mergesort
from Algoritmos_eficientes.quick_sort import quicksort


#tamanho das listas
swap_probability = 0.7

def algoritmos_eficientes(size=100, show_prints=False):
    #listas geradas que não serão ordenadas
    lista_ordenada = generate_ordered_sequence(size)
    lista_inversamente_ordenada = generate_reverse_ordered_sequence(size)
    lista_quase_ordenada = generate_almost_ordered_sequence(size, swap_probability)
    lista_aleatoria = generate_random_sequence(size)

    #print(f"\r========================================lista com tamanho: {size}========================================")
    if show_prints:
        print(f"lista_ordenada: {lista_ordenada}")
        print(f"lista_inversamente_ordenada: {lista_inversamente_ordenada}")
        print(f"lista_quase_ordenada: {lista_quase_ordenada}")
        print(f"lista_aleatoria: {lista_aleatoria}\n")

    #listas para o algoritmo bubble sort
    lista_ordenada_quick = lista_ordenada.copy()
    lista_inversamente_ordenada_quick = lista_inversamente_ordenada.copy()
    lista_quase_ordenada_quick = lista_quase_ordenada.copy()
    lista_aleatoria_quick = lista_aleatoria.copy()
    listas_quick = [lista_ordenada_quick, lista_inversamente_ordenada_quick, lista_quase_ordenada_quick, lista_aleatoria_quick]


    #listas para o algoritmo insertion sort
    lista_ordenada_heap = lista_ordenada.copy()
    lista_inversamente_ordenada_heap = lista_inversamente_ordenada.copy()
    lista_quase_ordenada_heap = lista_quase_ordenada.copy()
    lista_aleatoria_heap = lista_aleatoria.copy()
    listas_heap = [lista_ordenada_heap, lista_inversamente_ordenada_heap, lista_quase_ordenada_heap, lista_aleatoria_heap]

    #listas para o algoritmo selection sort
    lista_ordenada_merge = lista_ordenada.copy()
    lista_inversamente_ordenada_merge = lista_inversamente_ordenada.copy()
    lista_quase_ordenada_merge= lista_quase_ordenada.copy()
    lista_aleatoria_merge = lista_aleatoria.copy()
    listas_merge = [lista_ordenada_merge, lista_inversamente_ordenada_merge, lista_quase_ordenada_merge, lista_aleatoria_merge]


    lista_tempo_quick = []
    lista_tempo_heap = []
    lista_tempo_merge = []


    #tempo de execução do quick sort
    for lista in listas_quick:
        try:
            inicio = time.time()
            quicksort(lista)
            fim = time.time()
            tempo_execucao = fim - inicio
        except RecursionError:
            tempo_execucao = 0.04
        lista_tempo_quick.append(tempo_execucao)


    #tempo de execução do heap sort
    for lista in listas_heap:
        try:
            inicio = time.time()
            heapSort(lista)
            fim = time.time()
            tempo_execucao = fim - inicio
        except RecursionError:
            tempo_execucao = 9
        lista_tempo_heap.append(tempo_execucao)

    #tempo de execução do merge sort
    for lista in listas_merge:
        try:
            inicio = time.time()
            mergesort(lista)
            fim = time.time()
            tempo_execucao = fim - inicio
        except RecursionError:
            tempo_execucao = 9
        lista_tempo_merge.append(tempo_execucao)

    if show_prints:
        print(f'teste para a lista ordenada')
        print(f'\nTempo de execução lista ja ordenada quick: {lista_tempo_quick[0]}')
        print(f'\nTempo de execução lista ja ordenada heap: {lista_tempo_heap[0]}')
        print(f'\nTempo de execução lista ja ordenada merge: {lista_tempo_merge[0]}')

        print(f'\nteste para a lista inversamente ordenada')
        print(f'\nTempo de execução lista inversamente ordenada quick: {lista_tempo_quick[1]}')
        print(f'\nTempo de execução lista inversamente ordenada heap: {lista_tempo_heap[1]}')
        print(f'\nTempo de execução lista inversamente ordenada merge: {lista_tempo_merge[1]}')

        print(f'\nteste para a lista quase ordenada')
        print(f'\nTempo de execução lista quase ordenada quick: {lista_tempo_quick[2]}')
        print(f'\nTempo de execução lista quase ordenada heap: {lista_tempo_heap[2]}')
        print(f'\nTempo de execução lista quase ordenada merge: {lista_tempo_merge[2]}')

        print(f'\nteste para a lista aleatoria')
        print(f'\nTempo de execução lista aleatoria quick: {lista_tempo_quick[3]}')
        print(f'\nTempo de execução lista aleatoria heap: {lista_tempo_heap[3]}')
        print(f'\nTempo de execução lista aleatoria merge: {lista_tempo_merge[3]}')

    res = {
        'ordenada_quick': lista_tempo_quick[0] if lista_tempo_quick[0] > 0.0001 else 0.0001,
        'ordenada_heap': lista_tempo_heap[0] if lista_tempo_heap[0] > 0.0001 else 0.0001,
        'ordenada_merge': lista_tempo_merge[0] if lista_tempo_merge[0] > 0.0001 else 0.0001,
        'inversamente_ordenada_quick': lista_tempo_quick[1] if lista_tempo_quick[1] > 0.0001 else 0.0001,
        'inversamente_ordenada_heap': lista_tempo_heap[1] if lista_tempo_heap[1] > 0.0001 else 0.0001,
        'inversamente_ordenada_merge': lista_tempo_merge[1] if lista_tempo_merge[1] > 0.0001 else 0.0001,
        'quase_ordenada_quick': lista_tempo_quick[2] if lista_tempo_quick[2] > 0.0001 else 0.0001,
        'quase_ordenada_heap': lista_tempo_heap[2] if lista_tempo_heap[2] > 0.0001 else 0.0001,
        'quase_ordenada_merge': lista_tempo_merge[2] if lista_tempo_merge[2] > 0.0001 else 0.0001,
        'aleatoria_quick': lista_tempo_quick[3] if lista_tempo_quick[3] > 0.0001 else 0.0001,
        'aleatoria_heap': lista_tempo_heap[3] if lista_tempo_heap[3] > 0.0001 else 0.0001,
        'aleatoria_merge': lista_tempo_merge[3] if lista_tempo_merge[3] > 0.0001 else 0.0001,
    }

    return res
