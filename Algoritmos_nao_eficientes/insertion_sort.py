
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        #pega a chave, primeiro elemento da lista
        chave = lista[i]
        j = i - 1
        #faz a busca pra saber qual é elemento é maior que a chave 
        #e deslocando eles para a direita da chave
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j] 
            j = j - 1
        #no fim coloca a chave na sua posição certa
        lista[j+1] = chave

    return lista