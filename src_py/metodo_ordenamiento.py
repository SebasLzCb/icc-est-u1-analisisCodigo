# Creen una clase MetodosOrdenamient
# Crear un metodo sort bubble que reciba un arreglo, el metodo solo imprima el mensaje
class MetodosOrdenamiento:
    def __init__(self):
        pass

    def sort_bubble(self, array):
        arreglo = array.copy();
        n = len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] =  arreglo[j], arreglo[i]
        return arreglo
    
    def sort_burbuja_mejorado_optimizado(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        while n > 0:
            nuevo_n = 0  
            for i in range(1, n):
                if arreglo[i - 1] > arreglo[i]:
                    arreglo[i - 1], arreglo[i] = arreglo[i], arreglo[i - 1]
                    nuevo_n = i  
            n = nuevo_n 
        return arreglo

    
    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arreglo[j] < arreglo[min_index]:
                    min_index = j
            arreglo[i], arreglo[min_index] = arreglo[min_index], arreglo[i]
        return arreglo
    
    def sort_shells(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo
    

    