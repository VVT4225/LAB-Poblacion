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

def calcula_paises(poblaciones):
    conjunto = set()
    for k in poblaciones:
        conjunto.add(k[0])      # alternativamente puedes poner k.pais
    res = sorted(conjunto)
    return res

def filtra_por_pais(poblaciones, nombre_o_codigo):
    '''
    res = []
    for k in poblaciones:
        if (k[0] == nombre_o_codigo) or (k[1] == nombre_o_codigo):
            info = namedtuple('Info','Año, Censo')
            res.append(info(k[2],k[3]))
    return res
    '''

    res=[(p.año,p.censo) for p in poblaciones if p.pais==nombre_o_codigo or p.codigo==nombre_o_codigo]
    return res

def filtra_por_paises_y_year(poblaciones,year,paises):
    res = []
    for pais in paises:
        for p in poblaciones:
            if p[0] == pais:
                if p[2] == year:
                    info = namedtuple('Info','País, Censo')
                    res.append(info(p.pais,p.censo))
    return res
