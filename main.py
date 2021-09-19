#!/usr/bin/python3

# pip install xlsxwriter
import xlsxwriter
import itertools 

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

    # crear fichero excel

    workbook = xlsxwriter.Workbook('resultados.xlsx')
    worksheet = workbook.add_worksheet()
    
    # funcion para la letra negrita
    bold = workbook.add_format({'bold': True})

    # crea los titulos de las variables y los inserta en el excel

    worksheet.write('A1', 'Variable estadística (Xi)', bold)
    worksheet.write('B1', 'Frecuencia absoluta  (fi)', bold)
    worksheet.write('C1', 'Frecuencia relativa  (hi)', bold)
    worksheet.write('D1', 'Porcentaje           (pi)', bold)

    # fila y columna donde empezar

    row = 1
    col = 0

    # crea las columnas y filas con los datos previamente calculados

    for var, fii, hii, pii in zip(Xi, fi, hi, pi):
        worksheet.write(row, col,     var)
        worksheet.write(row, col + 1, fii)
        worksheet.write(row, col + 2, hii)
        worksheet.write(row, col + 3, pii)
        row += 1

    # inserta la Fi
    worksheet.write('E1', 'Frecuencia absoluta acumulada (Fi)', bold)
    worksheet.write('E2', Fi)

    # inserta la Hi
    worksheet.write('F1', 'Frecuencia relativa acumulada (Hi)', bold)
    worksheet.write('F2', Hi)

    # inserta el Pi
    worksheet.write('G1', 'Porcentaje acumulado (Pi)', bold)
    worksheet.write('G2', Fi)
    
    workbook.close()



if __name__ == "__main__":
    main()
