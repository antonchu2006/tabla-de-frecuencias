#!/usr/bin/python3

# esta funcion busca cuantas veces aparece un elemento en una lista, está copiada de stack overflow

def buscar_n_elemento(lista, e):
    contador=0
    for i in lista:
        if i == e:
            contador+=1
    return contador

def main():


    # definir los resultados de la población del estudio

    poblacion = [38, 38, 38, 40, 35, 39, 37, 37, 40, 37, 36, 35, 36, 40, 40, 42, 41, 42, 39, 41, 38, 39, 35, 36, 42, 42]


    # crear una lista de la poblacion sin resultados repetidos

    Xi = set(poblacion)

    # declarar variables

    Pi = 0      # Porcentajes acumulados
    Hi = 0      # frecuencia relativa acumulada
    Fi = 0      # frecuencia absoluta acumulada
    pi = []     # porcentaje
    hi = []     # frecuencia relativa
    fi = []     # frecuencia absoluta


    # calcular frecuencia absoluta

    for x in Xi:
        fi.append(buscar_n_elemento(poblacion, x))

    # calcular sumatorio de fi, frecuencia absoluta acumulada

    Fi = len(poblacion) 

    # frecuencia relativa

    for x in  fi:
        x = x/len(poblacion) 

        hi.append(x)

    # calcular frecuencia relativa acumulada

    for x in hi:
        Hi += x

    # calcular porcentaje

    for x in hi:
        pi.append(x*100)

    # calcular porcentaje acumulado

    for x in pi:
        Pi += x


if __name__ == "__main__":
    main()
