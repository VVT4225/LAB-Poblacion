from poblacion import *

ruta = "C:/Users/Peke/Documents/GitHub/LAB-Poblacion/data/population.csv"


if __name__ == "__main__":
    datos_poblacion = lee_poblaciones(ruta)
    #print(datos_poblacion[20:30])
    lista_paises = calcula_paises(datos_poblacion)
    print(lista_paises)
