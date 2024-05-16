import math
import numpy as np
import matplotlib.pyplot as plt

# Leer los datos del archivo txt
def leer_datos(num_decimales,nombre_archivo):
    datos=[]
    with open(nombre_archivo,'r') as file:
        for line in file:
            number = round(float(line.strip()),num_decimales)
            datos.append(number)
    return datos

# Definir variables para tabla de frecuencias
def variables_tabla_frecuencias(num_decimales,nombre_archivo):
    datos = leer_datos(num_decimales,nombre_archivo)
    valor_max = max(datos)
    valor_min = min(datos)
    num_datos = len(datos)
    num_intervalos = math.ceil(1+3.3*math.log(num_datos, 10))
    ancho_intervalo = round(((valor_max-valor_min)/num_intervalos),num_decimales)
    frecuencias = [0] * num_intervalos
    for dato in datos:
        intervalo_index = min(int((dato-valor_min)//ancho_intervalo),num_intervalos-1)
        frecuencias[intervalo_index] += 1
    return valor_max, valor_min, ancho_intervalo, num_datos, num_intervalos, frecuencias

#Imprimir en consola la tabla de frecuencias
def imprimir_tabla_frecuencias(num_decimales,nombre_archivo):
    valor_max, valor_min, ancho_intervalo, num_datos, num_intervalos, frecuencias = variables_tabla_frecuencias(num_decimales,nombre_archivo)
    print(f"N: {num_datos}")
    print(f"C = {num_intervalos}")
    print(f"Max: {valor_max}, min: {valor_min}")
    print(f"W = {ancho_intervalo}")
    print("Intervals              f")
    suma_frecuencias = 0
    for i, frecuencia in enumerate(frecuencias):
        suma_frecuencias += frecuencia
        limite_superior = valor_min + i * ancho_intervalo
        limite_inferior = valor_min + (i + 1) * ancho_intervalo
        print(f"[{round(limite_superior,num_decimales)} - {round(limite_inferior,num_decimales)})      {frecuencia}")
    print(f"Sum of frequencies: {suma_frecuencias}")

# Graficar el histograma
def graficar_histograma(num_decimales,nombre_archivo):
    valor_max, valor_min, ancho_intervalo, num_datos, num_intervalos, frecuencias = variables_tabla_frecuencias(num_decimales,nombre_archivo)
    x_pos = np.arange(num_intervalos)  
    etiquetas_x = []
    for i, frecuencia in enumerate(frecuencias):
        limite_superior = valor_min + i * ancho_intervalo
        limite_inferior = valor_min + (i + 1) * ancho_intervalo
        etiqueta = f"[{round(limite_superior,num_decimales)} - {round(limite_inferior,num_decimales)})"
        etiquetas_x.append(etiqueta)  
    plt.bar(x_pos,frecuencias,align='center',alpha=0.7)
    plt.xticks(x_pos,etiquetas_x,rotation='horizontal',fontsize=5)
    plt.title('Frequencias of grouped data')
    plt.xlabel('Bins')
    plt.ylabel('Frequencies')
    plt.show()

def main():
    num_decimales = int(input("Ingrese el numero de decimales: "))
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    imprimir_tabla_frecuencias(num_decimales,nombre_archivo)
    graficar_histograma(num_decimales,nombre_archivo)

if __name__ == "__main__":
    main()