from genData import genAltura, genPeso, agrupar, genxy, aleatorio_unico, barajar


def menu(self):

    if self == 1:
        fileAlturas = 'alturas.csv'
        try:
            numeroFilas = input('escribe un número mayor a 30 y menor a 150 > ')
            numeroFilas = int(numeroFilas)

            genAltura(fileAlturas, numeroFilas)

        except ValueError:
            print(ValueError, ":", numeroFilas, 'no es un número')

    elif self == 2:
        filePeso = 'pesos.csv'
        try:
            rango = input('escribe un número mayor a 30 y menor a 150 > ')
            rango = int(rango)

            genPeso(filePeso, rango)

        except ValueError:
            print(ValueError, ":", rango, 'no es un número')

    elif self == 3:
        fileAlturas = 'alturas.csv'
        groupData = 'alturas_agrupadas.csv'

        agrupar(fileAlturas, groupData)

    elif self == 4:
        filexy = 'fileXY.csv'
        try:
            numeroFilas = input('escribe un número mayor a 30 y menor a 150 > ')
            numeroFilas = int(numeroFilas)

            genxy(filexy, numeroFilas)

        except ValueError:
            print(ValueError, ":", numeroFilas, 'no es un número')

    elif self == 5:
        fileunico = 'fileUnico.csv'
        try:
            numeroFilas = input('escribe un número  --> ')
            numeroFilas = int(numeroFilas)

            aleatorio_unico(fileunico, numeroFilas)

        except ValueError:
            print(ValueError, ":", numeroFilas, 'no es un número')

    elif self == 6:
        filecsv = 'Archivo.csv'
        barajar(filecsv)


def main():

    sel = 0

    while sel != 5:
        try:
            sel = input("1 - Generar alturas\n"
                        "2 - Generar pesos\n"
                        "3 - Agrupar alturas\n"
                        "4 - Generar X & Y datos\n"
                        "5 - Genera números aleatorios únicos\n"
                        "6 - Barajar\n"
                        "7 - Salir\n"
                        "-->  ")
            sel = int(sel)
            if sel == 7: break
            menu(sel)
        except ValueError:
            print(ValueError, ":", sel, "no es un valor numérico")


if __name__ == "__main__":

    main()
