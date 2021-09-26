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


    # definir los resultados de la población del estudio. Deben ser solo números y estar en el formato en el que estan aquí.

    poblacion = [38, 38, 38, 40, 35, 39, 37, 37, 40, 37, 36, 35, 36, 40, 40, 42, 41, 42, 39, 41, 38, 39, 35, 36, 42, 42]


    # crear una lista de la poblacion sin resultados repetidos

    Xi = set(poblacion)

    # declarar variables
    Pii = []    # porcentaje acumulado
    Fii = []    # frecuencia absoluta acumulado
    Hii = []    # frecuencia relativa acumulada 
    Pi = 0      # Porcentajes acumulado total
    Hi = 0      # frecuencia relativa acumulada
    Fi = 0      # frecuencia absoluta acumulada total
    pi = []     # porcentaje
    hi = []     # frecuencia relativa
    fi = []     # frecuencia absoluta


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
        Hi += x
        Hii.append(Hi)

    # calcular porcentaje

    for x in hi:
        pi.append(x*100)

    # calcular porcentaje acumulado

    for x in pi:
        Pi += x
        Pii.append(Pi)

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
    worksheet.write('E1', 'Frecuencia relativa acumulada (Hi)', bold)
    worksheet.write('F1', 'Porcentaje acumulado (Pi)', bold)
    worksheet.write('G1', 'Frecuencia absoluta acumulada (Fi)', bold)

    # fila y columna donde empezar

    row = 1
    col = 0

    # crea las columnas y filas con los datos previamente calculados

    for var, fii, hii, pii, Hiii, Piii, Fiii in zip(Xi, fi, hi, pi, Hii, Pii, Fii):
        worksheet.write(row, col,     var)
        worksheet.write(row, col + 1, fii)
        worksheet.write(row, col + 2, hii)
        worksheet.write(row, col + 3, pii)
        worksheet.write(row, col + 4, Hiii)
        worksheet.write(row, col + 5, Piii)
        worksheet.write(row, col + 6, Fiii)
        row += 1
    
    workbook.close()

if __name__ == "__main__":
    main()
