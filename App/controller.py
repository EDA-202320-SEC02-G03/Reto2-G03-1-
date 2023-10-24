"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import time
import csv
import tracemalloc
from DISClib.ADT import list as lt
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos
def load_first(control, filename):
    datos = control["model"][0]
    loadGoles(datos, filename)
    loadResults(datos, filename)
    loadShootout(datos, filename)

def load_data(control, goles, memflag=True):
    """
    Carga los datos del reto
    """
    data_structs = control["model"][1]
    start_time = get_time()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    loadscorers(data_structs,goles)
    loadhome(data_structs,goles)
    loadaway(data_structs,goles)

    # toma el tiempo al final del proceso
    stop_time = get_time()
    # calculando la diferencia en tiempo
    deltatime = delta_time(stop_time, start_time)

    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltamemory = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return deltatime, deltamemory

    else:
        # respuesta sin medir memoria
        return deltatime

def loadGoles (new_data_structs, filename):
    goalfile = cf.data_dir + filename[0]
    input_file = csv.DictReader(open(goalfile, encoding='utf-8'))
    for goals in input_file:
        model.add_goles(new_data_structs, goals)
    

def loadResults(new_data_structs, filename):
    resultsfile = cf.data_dir + filename[1]
    input_file = csv.DictReader(open(resultsfile, encoding='utf-8'))
    for results in input_file:
        model.add_results(new_data_structs, results)
    

def loadShootout(new_data_structs, filename):
    shootoutfile = cf.data_dir + filename[2]
    input_file = csv.DictReader(open(shootoutfile, encoding='utf-8'))
    for shootout in input_file:
        model.add_shootout(new_data_structs, shootout)

def loadscorers(data_structs,goles):
    for cada_uno in lt.iterator(goles):
        model.add_scorer(data_structs, cada_uno)

def loadhome(data_structs, goles):
    for cada_uno in lt.iterator(goles):
        model.add_home(data_structs, cada_uno)

def loadaway(data_structs, goles):
    for cada_uno in lt.iterator(goles):
        model.add_away(data_structs, cada_uno)
# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass

def sort_fecha(control):
    sortear = model.sortear_fecha(control["model"])
    return sortear

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
