
def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):

            if lista[i] > lista[i+1]:
                # troca de elementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]

    return lista
