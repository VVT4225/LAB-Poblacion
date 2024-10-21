from poblacion import *

ruta = "C:/Users/Peke/Documents/GitHub/LAB-Poblacion/data/population.csv"


if __name__ == "__main__":
    datos_poblacion = lee_poblaciones(ruta)
    #print(datos_poblacion[20:30])
    lista_paises = calcula_paises(datos_poblacion)
    #print(lista_paises)
    datos_pais = filtra_por_pais(datos_poblacion,"ESP")
    print(datos_pais)
    paises = {"Spain","Sri Lanka"}
    filtra_pais_year = filtra_por_paises_y_year(datos_poblacion,1990,paises)
    #print(filtra_pais_year)