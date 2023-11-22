
def selection_sort(lista):
    n = len(lista)

    for j in range(n-1):
        #seleciona o primeiro elemento da lista como minimo
        min_index = j
        for i in range(j, n):    
            #realiza a comparação pra saber qual é o menor elemento da lista      
            if lista[i] < lista[min_index]:
                min_index = i

        #realiza a troca se o elemento da posição j for maior que o elemento da busca anterior
        #que o indice ficou armazenado na variavel min_index
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux    

    return lista