import random
import time
from metodo_ordenamiento import MetodosOrdenamiento
class benchmarking: 

    # public Benchmarking() {
    def __init__(self):
        print('Bechmarking instaciado')

        self.mO = MetodosOrdenamiento()
        arreglo = self.build_arreglo(10000)

        tarea = lambda: self.mO.sort_bubble(arreglo)
        tarea2 = lambda: self.mO.sort_seleccion(arreglo)
        tarea3 = lambda: self.mO.sort_burbuja_mejorado_optimizado(arreglo)
        tarea4 = lambda: self.mO.sort_shells(arreglo)

        #tiempomilles = self.contar_con_current_time_milles(tarea)

        tiemponano = self.contar_con_nano_time(tarea)
        tiemponano2 = self.contar_con_nano_time(tarea2)
        tiemponano3 = self.contar_con_nano_time(tarea3)
        tiemponano4 = self.contar_con_nano_time(tarea4)

        print("Este es el metodo de ordenamiento burbuja")
        print(f"Tiempo con nanoTime: {tiemponano} ")
        print(" ")

        print("Este es el metodo de ordenamiento burbuja mejorado optimizado")
        print(f"Tiempo con nanoTime: {tiemponano3} ")
        print(" ")

        print("Este es el metodo de ordenamiento seleccion")
        print(f"Tiempo con nanoTime: {tiemponano2} ")
        print(" ")

        print("Este es el metodo de ordenamiento shell")
        print(f"Tiempo con nanoTime: {tiemponano4} ")
        print(" ")


    def build_arreglo(self, tamano):
        arreglo = [tamano]
        for _ in range(tamano):
            numero = random.randint(0, 99999)
            arreglo.append(numero)
        return arreglo
        
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time() 
        tarea()
        fin = time.time()
        return (fin - inicio) 

    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000.0