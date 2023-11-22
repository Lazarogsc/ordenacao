import time
from .bubble_sort import bubble_sort
from .gerador_lista import generate_almost_ordered_sequence, generate_ordered_sequence, generate_random_sequence, generate_reverse_ordered_sequence
from .insertion_sort import insertion_sort
from .selection_sort import selection_sort

#tamanho das listas
swap_probability = 0.7

def algoritmos_nao_eficientes(size=100):
    #listas geradas que não serão ordenadas
    lista_ordenada = generate_ordered_sequence(size)
    lista_inversamente_ordenada = generate_reverse_ordered_sequence(size)
    lista_quase_ordenada = generate_almost_ordered_sequence(size, swap_probability)
    lista_aleatoria = generate_random_sequence(size)

    print(f"lista_ordenada: {lista_ordenada}")
    print(f"lista_inversamente_ordenada: {lista_inversamente_ordenada}")
    print(f"lista_quase_ordenada: {lista_quase_ordenada}")
    print(f"lista_aleatoria: {lista_aleatoria}")
    
    #listas para o algoritmo bubble sort
    lista_ordenada_bubble = lista_ordenada.copy()
    lista_inversamente_ordenada_bubble = lista_inversamente_ordenada.copy()
    lista_quase_ordenada_bubble = lista_quase_ordenada.copy()
    lista_aleatoria_bubble = lista_aleatoria.copy()
    listas_bubble = [lista_ordenada_bubble, lista_inversamente_ordenada_bubble, lista_quase_ordenada_bubble, lista_aleatoria_bubble]
    
    #listas para o algoritmo insertion sort
    lista_ordenada_insertion = lista_ordenada.copy()
    lista_inversamente_ordenada_insertion = lista_inversamente_ordenada.copy()
    lista_quase_ordenada_insertion = lista_quase_ordenada.copy()
    lista_aleatoria_insertion = lista_aleatoria.copy()
    listas_insertion = [lista_ordenada_insertion, lista_inversamente_ordenada_insertion, lista_quase_ordenada_insertion, lista_aleatoria_insertion]
    
    #listas para o algoritmo selection sort
    lista_ordenada_selection = lista_ordenada.copy()
    lista_inversamente_ordenada_selection = lista_inversamente_ordenada.copy()
    lista_quase_ordenada_selection= lista_quase_ordenada.copy()
    lista_aleatoria_selection = lista_aleatoria.copy()
    listas_selection = [lista_ordenada_selection, lista_inversamente_ordenada_selection, lista_quase_ordenada_selection, lista_aleatoria_selection]
    
    
    lista_tempo_bubble = []
    lista_tempo_insertion = []
    lista_tempo_selection = []
    
    #tempo de execução do bubble sort
    for lista in listas_bubble:
        inicio = time.time()
        bubble_sort(lista)
        fim = time.time()
        tempo_execucao = fim - inicio
        lista_tempo_bubble.append(tempo_execucao)
    
    #tempo de execução do insertion sort
    for lista in listas_insertion:
        inicio = time.time()
        insertion_sort(lista)
        fim = time.time()
        tempo_execucao = fim - inicio
        lista_tempo_insertion.append(tempo_execucao)
    
    #tempo de execução do selection sort
    for lista in listas_selection:
        inicio = time.time()
        selection_sort(lista)
        fim = time.time()
        tempo_execucao = fim - inicio
        lista_tempo_selection.append(tempo_execucao)
    
    print(f'teste para a lista ordenada')
    print(f'\nTempo de execução lista ja ordenada bubble: {lista_tempo_bubble[0]}')
    print(f'\nTempo de execução lista ja ordenada insertion: {lista_tempo_insertion[0]}')
    print(f'\nTempo de execução lista ja ordenada selection: {lista_tempo_selection[0]}')
    
    print(f'\nteste para a lista inversamente ordenada')
    print(f'\nTempo de execução lista inversamente ordenada bubble: {lista_tempo_bubble[1]}')
    print(f'\nTempo de execução lista inversamente ordenada insertion: {lista_tempo_insertion[1]}')
    print(f'\nTempo de execução lista inversamente ordenada selection: {lista_tempo_selection[1]}')
    
    print(f'\nteste para a lista quase ordenada')
    print(f'\nTempo de execução lista quase ordenada bubble: {lista_tempo_bubble[2]}')
    print(f'\nTempo de execução lista quase ordenada insertion: {lista_tempo_insertion[2]}')
    print(f'\nTempo de execução lista quase ordenada selection: {lista_tempo_selection[2]}')
    
    print(f'\nteste para a lista aleatoria')
    print(f'\nTempo de execução lista aleatoria bubble: {lista_tempo_bubble[3]}')
    print(f'\nTempo de execução lista aleatoria insertion: {lista_tempo_insertion[3]}')
    print(f'\nTempo de execução lista aleatoria selection: {lista_tempo_selection[3]}')
    
    return {
        'lista ja ordenada bubble': lista_tempo_bubble[0] if lista_tempo_bubble[0] > 0.0001 else 0.0001,
        'lista ja ordenada insertion': lista_tempo_insertion[0] if lista_tempo_insertion[0] > 0.0001 else 0.0001,
        'lista ja ordenada selection': lista_tempo_selection[0] if lista_tempo_selection[0] > 0.0001 else 0.0001,
        'lista inversamente ordenada bubble': lista_tempo_bubble[1] if lista_tempo_bubble[1] > 0.0001 else 0.0001,
        'lista inversamente ordenada insertion': lista_tempo_insertion[1] if lista_tempo_insertion[1] > 0.0001 else 0.0001,
        'lista inversamente ordenada selection': lista_tempo_selection[1] if lista_tempo_selection[1] > 0.0001 else 0.0001,
        'lista quase ordenada bubble': lista_tempo_bubble[2] if lista_tempo_bubble[2] > 0.0001 else 0.0001,
        'lista quase ordenada insertion': lista_tempo_insertion[2] if lista_tempo_insertion[2] > 0.0001 else 0.0001,
        'lista quase ordenada selection': lista_tempo_selection[2] if lista_tempo_selection[2] > 0.0001 else 0.0001,
        'lista aleatoria bubble': lista_tempo_bubble[3] if lista_tempo_bubble[3] > 0.0001 else 0.0001,
        'lista aleatoria insertion': lista_tempo_insertion[3] if lista_tempo_insertion[3] > 0.0001 else 0.0001,
        'lista aleatoria selection': lista_tempo_selection[3] if lista_tempo_selection[3] > 0.0001 else 0.0001,
    }