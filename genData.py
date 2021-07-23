import random
import csv



def genAltura(fileAlturas, numeroFilas):
    with open(fileAlturas, 'w+') as file:
        file.write('números\n')
        data = '{:.0f}\n'
        for rand in range(numeroFilas):
            alturas = (random.uniform(1, 50))
            file.write(data.format(alturas))


def aleatorio_unico(fileUnico, numeroFilas):
    with open(fileUnico, 'w+') as file:
        """file.write('números\n')
        lista_numbers = list(range(1, numeroFilas+1))
        random.shuffle(lista_numbers) # revuelve la lista
        for i in lista_numbers:
            file.write(str(i)+"\n")"""
        lista_numeros = [random.randint(1, numeroFilas)] # lista_numeros[0]
        i = 1
        while i < numeroFilas:
            x = random.randint(1, numeroFilas) # es decir (1, 50)
            if x not in lista_numeros:
                lista_numeros.append(x)
                i += 1
        for n in lista_numeros:
            file.write(str(n)+"\n")


def barajar(filecsv):
    with open(filecsv, 'w+', newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in range(file):
            print(', '.join(row))



def genPeso(filePeso, numeroFilas):
    with open(filePeso, 'w+') as file:
        file.write('Peso\n')
        data = '{:.2f}\n'
        for rand in range(numeroFilas):
            peso = (random.uniform(30, 101))
            file.write(data.format(peso))


def genxy(filexy, numeroFilas):
    X = list()
    Y = list()
    formatDato = '{:.2f}'

    for n in range(numeroFilas):
        X.append(random.uniform(1.45, 2.00))
        Y.append(random.uniform(45, 102))

    with open(filexy, 'w+') as file:
        file.write('valor x \t valor y\n')
        for x, y in zip(X, Y):
            file.writelines(formatDato.format(x) + '\t' + formatDato.format(y) + '\n')


def agrupar(fileToGroup, groupData):
    with open(fileToGroup, 'r') as file:
        with open(groupData, 'w+') as groupfile:
            file.seek(0)
            alturas = file.readlines()
            cabecera = alturas[0]
            alturas.pop(0)
            alturas.sort()

            ''' Iteración de lista para guardar datos en diccionario, {key:value} '''
            dict_altura = dict()
            for i in alturas:
                dict_altura[i] = dict_altura.get(i, 0) + 1

            ''' Escribe en archivo csv los nombres de las columnas'''
            groupfile.seek(0)
            groupfile.write(cabecera.rstrip() + '\tFrecuencia' + '\tF. Ac.\n')

            f_ac = 0
            ''' Iteración de diccionario, genera frecuencia acumulada y posteriormente escribe en archivo csv'''
            for k in dict_altura:
                print(k.rstrip(), dict_altura[k])
                f_ac += dict_altura[k]
                groupfile.writelines(k.rstrip() + '\t' + str(dict_altura[k]) + '\t' + str(f_ac) + '\n')

