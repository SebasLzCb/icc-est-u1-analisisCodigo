#import benchmarking as bm
import benchmarking as bm
from metodo_ordenamiento import MetodosOrdenamiento
# Archivo principal o main
if __name__ == "__main__":
    print("Funciona")
    bench = bm.benchmarking()
    metodosO = MetodosOrdenamiento()
    
    #tam = 10000
    tamanios = [5000, 10000, 20000]
    
    resultados = []
    
    for tam in tamanios:
        
        arreglo_base = bench.build_arreglo(tam)
    
        metodos_dic = {
            "burbuja" : metodosO.sort_bubble,
            "seleccion" : metodosO.sort_seleccion,
            "burbujamejorado" : metodosO.sort_burbuja_mejorado_optimizado,
            "shell" : metodosO.sort_shells
        }
        
        for nombre, fun_metodo in metodos_dic.items():
            
            tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)
            
    for tam, nombre, tiempo_resultado in resultados:
        print(f'Tamaño: {tam}, Nombre metodo: {nombre}, Tiempo: {tiempo_resultado:.6f} segundos')
        