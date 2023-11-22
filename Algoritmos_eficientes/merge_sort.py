
def mergesort(lista, inicio=0, fim=None):
    #seta o fim da lista com o tamanho, caso não seja passado o parametro
    if fim is None:
        fim = len(lista)
    #começa a dividir a lista se for que 1
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        #faz a chamada recursivamente para o inicio até o meio
        mergesort(lista, inicio, meio)
        #faz a chamada recursivamente para o meio até o fim
        mergesort(lista, meio, fim)
        #combina as duas listas anteriores
        merge(lista, inicio, meio, fim)
        return lista

def merge(lista, inicio, meio, fim):
    #cria duas sublistas
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    #realiza a combinação das duas sublistas
    for k in range(inicio, fim):
        #caso todos os elementos da esquerda tenham sido utilizados
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        #caso todos os elementos da direita tenham sido utilizados    
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        #caso o topo da esquerda seha menor que da direita, é o elemento da esquerda que 
        #entra na lista
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        #se não, é o elemento da direita que entra na lista
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1

