# Heap Sort in python

def heapify(arr, n, i):
    # Encontra o maior entre raiz e filhos direito e esquerdo
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    # Encontra o maior entre raiz e filhos esquerdo
    if l < n and arr[i] < arr[l]:
        largest = l
    # Encontra o maior entre raiz e filhos direito
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # caso o nó não for a maior elemento, é realizado a 
    # troca pela maior e continue a heapificar
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
  
  
def heapSort(arr):
    n = len(arr)
  
    # Criar heap máximo
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        # Troca
        arr[i], arr[0] = arr[0], arr[i]
  
        # Heapificar o elemento raiz
        heapify(arr, i, 0)
  
