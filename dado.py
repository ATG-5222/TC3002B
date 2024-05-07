import random
import matplotlib.pyplot as plt

def lanzamientos_dado(lanzamientos):
    resultados = []
    suma_resultados = 0
    for _ in range(lanzamientos):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
        suma_resultados += resultado
    promedio = suma_resultados / lanzamientos
    return resultados, promedio

def histograma(resultados,promedio):
    plt.suptitle("Histograma de lanzamiento de dado")
    plt.title(f"El promedio de los resultados es: {promedio}")
    plt.xlabel("Cara del dado")
    plt.ylabel("Frecuencia")
    plt.hist(resultados, bins=range(1,8), align="left", edgecolor="black")
    plt.show()

resultados, promedio = lanzamientos_dado(1000)
histograma(resultados,promedio)