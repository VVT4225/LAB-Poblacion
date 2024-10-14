import csv
from matplotlib import pyplot as plt
from collections import namedtuple

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    poblacion = []
    with open(ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        for pais, codigo, año, censo in lector:
            pais = str(pais)
            codigo = str(codigo)
            año = int(año)
            censo = int(censo)
            poblacion.append(RegistroPoblacion(pais,codigo,año,censo))
    return poblacion

