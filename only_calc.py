#!/usr/bin/python3

# pip install numpy
import numpy as np
import math

# formula para Dx scripteada

def desviacion_absoluta_media(Xi, media, fi):
    n = 0
    for Xii, Fii in zip(Xi,fi):
        n += abs(Xii-media)*Fii
    return n/len(Xi)

# formula para varianza scripteada

def varianza(Xi, media, fi):
    n = 0
    for Xii, Fii in zip(Xi,fi):
        n += ((Xii-media)**2)*Fii
    return n/len(Xi)

# esta funcion busca cuantas veces aparece un elemento en una lista, está copiada de stack overflow


def buscar_n_elemento(lista, e):
    contador=0
    for i in lista:
        if i == e:
            contador+=1
    return contador

def main():


    # definir los resultados de la población del estudio. Deben ser solo números y estar en el formato en el que estan aquí

    poblacion = [38, 38, 38, 40, 35, 39, 37, 37, 40, 37, 36, 35, 36, 40, 40, 42, 41, 42, 39, 41, 38, 39, 35, 36, 42, 42]


    # crear una lista de la poblacion sin resultados repetidos

    Xi = set(poblacion)

    # declarar variables
    Mo = 0      # moda
    Me = 0      # mediana
    media = 0   # la media
    Pii = []    # porcentaje acumulado
    Fii = []    # frecuencia absoluta acumulado
    Hii = []    # frecuencia relativa acumulada 
    Pi = 0      # Porcentajes acumulado total
    Hi = 0      # frecuencia relativa acumulada
    Fi = 0      # frecuencia absoluta acumulada total
    pi = []     # porcentaje
    hi = []     # frecuencia relativa
    fi = []     # frecuencia absoluta
    Dx = 0      # desviacion absoluta media
    s2 = 0      # varianza
    s = 0       # desviacion tipica
    CV = 0      # coeficiente de variacion


    # calcular frecuencia absoluta

    for x in Xi:
        fi.append(buscar_n_elemento(poblacion, x))

    # calcular frecuencia absoluta acumulada

    for x in fi:
        Fi += x
        Fii.append(Fi)

    # calcular sumatorio de fi, frecuencia absoluta acumulada total

    Fi = len(poblacion) 

    # frecuencia relativa

    for x in  fi:
        x = x/len(poblacion) 

        hi.append(x)

    # calcular frecuencia relativa acumulada

    for x in hi:
        Hi += x # resultado final
        Hii.append(Hi)

    # calcular porcentaje

    for x in hi:
        pi.append(x*100)

    # calcular porcentaje acumulado

    for x in pi:
        Pi += x # resultado final
        Pii.append(Pi)

    # calcular media

    for x, y in zip(Xi, fi):
        media += x*y
    media = media / Fi

    # calcular mediana usando numpy 

    Me = np.median(poblacion)

    # calcular moda 

    for x in fi:
        if (Mo is None or x > Mo):
            Mo = x

    
    # calcular Dx

    Dx = desviacion_absoluta_media(Xi, media, fi)

    # calcular varianza 

    s2 = varianza(Xi, media, fi)

    # calcular desviacion tipica

    s = math.sqrt(s2)

    # calcular coeficiente de variacion 

    CV = s / abs(media)


if __name__ == "__main__":
    main()
