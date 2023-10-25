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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    datos = {'goles': None,
               'results': None,
               'shootout': None}

    datos['goles'] = lt.newList("ARRAY_LIST")
    datos['results'] = lt.newList("ARRAY_LIST")
    datos['shootout'] = lt.newList("ARRAY_LIST")
    

    
    data_structs = {'scorers': None,
                    'home': None,
                    'away': None,
                    'tournament': None
                    }
    
    data_structs['scorers'] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4)
    data_structs['home'] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4)
    data_structs['away'] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4)
    data_structs['tournament'] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4)
    a = [datos, data_structs]
    return a
    

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass

def add_goles(new_data_structs, goals):
    lt.addLast(new_data_structs['goles'], goals)
    return new_data_structs

def add_results(new_data_structs, results):
    lt.addLast(new_data_structs['results'], results)
    return new_data_structs

def add_shootout (new_data_structs, shootout):
    lt.addLast(new_data_structs['shootout'], shootout)
    return new_data_structs

def add_scorer(data_structs, scorer):
    scorers = data_structs['scorers']
    linea = scorer['scorer']
    existe = mp.contains(scorers, linea)
    #existe retorna True o False
    if existe:
        pareja = mp.get(scorers, linea)
        valor = me.getValue(pareja)
    else:
        valor = new_scorer(linea)
        mp.put(scorers, linea, valor)
    lt.addLast(valor["partidos"],scorer)

def new_scorer(scorer):
    entry = {'scorer': "", "partidos": None}
    entry['scorer'] = scorer
    entry['partidos'] = lt.newList('ARRAY_LIST')
    return entry

def add_home(data_structs, home_team):
    team = data_structs['home']
    linea = home_team['home_team']
    existe = mp.contains(team, linea)
    if existe:
        pareja = mp.get(team, linea)
        valor = me.getValue(pareja)
    else:
        valor = new_home(linea)
        mp.put(team, linea, valor)
    lt.addLast(valor["partidos"],home_team)

def new_home(home_team):
    entry = {'home_team': "", "partidos": None}
    entry['home_team'] = home_team
    entry['partidos'] = lt.newList('ARRAY_LIST')
    return entry

def add_away(data_structs, away_team):
    team = data_structs['away']
    linea = away_team['away_team']
    existe = mp.contains(team, linea)
    if existe:
        pareja = mp.get(team, linea)
        valor = me.getValue(pareja)
    else:
        valor = new_away(linea)
        mp.put(team, linea, valor)
    lt.addLast(valor["partidos"],away_team)

def new_away(away_team):
    entry = {'away_team': "", "partidos": None}
    entry['away_team'] = away_team
    entry['partidos'] = lt.newList('ARRAY_LIST')
    return entry

def add_tournament(data_structs, tournament):
    team = data_structs['tournament']
    linea = tournament['tournament']
    existe = mp.contains(team, linea)
    if existe:
        pareja = mp.get(team, linea)
        valor = me.getValue(pareja)
    else:
        valor = new_tournament(linea)
        mp.put(team, linea, valor)
    lt.addLast(valor["partidos"],tournament)

def new_tournament(tournament):
    entry = {'tournament': "", "partidos": None}
    entry['tournament'] = tournament
    entry['partidos'] = lt.newList('ARRAY_LIST')
    return entry
# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, matches, team, condition):
    """
    Función que soluciona el requerimiento 1
    """
    if condition == 'home':
        a = mp.get(data_structs['home'], team)
        b = lt.subList(me.getValue(a)['partidos'],1,matches)
        
    elif condition == 'away':
        a = mp.get(data_structs['away'], team)
        b = lt.subList(me.getValue(a)['partidos'],1,matches)
    
    return b

def req_2(data_structs, scores, player_name):
    """
    Función que soluciona el requerimiento 2
    """
    a = mp.get(data_structs['scorers'],player_name)
    b = me.getValue(a)['partidos']
    lon = lt.size(b)
    x = lon - scores
    c = lt.subList(b, x, scores)
    return c
    
    


def req_3(data_structs,equipo, start,end):     
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    lista1 = lt.newList("ARRAY_LIST")
    homesize = 0
    awaysize = 0
    equiposa = mp.get(data_structs["away"],equipo)
    equiposh = mp.get(data_structs["home"],equipo)
    partidoa= me.getValue(equiposa)["partidos"]
    partidoh = me.getValue(equiposh)["partidos"]
    #goles = mp.get(data_structs["scorers"],equipo)
    #fgoles = me.getValue(goles)["partidos"]
    for i in lt.iterator(partidoa):
        if i["date"]>= start and i["date"]<= end:
            #i["penalty"]=="Unknown"
            #i["own_goal"]=="Unknown"
            #for k in lt.iterator(fgoles):
                #if k["date"]>= start and k["date"]<= end:
                    #k["penalty"]==i["penalty"]
                    #k["own_goal"]==i["own_goal"]
            awaysize+=1
            lt.addLast(lista1,i)
    for j in lt.iterator(partidoh):
        if j["date"]>= start and j["date"]<= end:
            #j["penalty"]=="Unknown"
            #j["own_goal"]=="Unknown"
            #for p in lt.iterator(fgoles):
                #if p["date"]>= start and k["date"]<= end:
                    #p["penalty"]==j["penalty"]
                    #p["own_goal"]==j["own_goal"]
            homesize+=1
            lt.addLast(lista1,j)
    size = lt.size(lista1)
    listaordenada = quk.sort(lista1,compare_results)
    x = lt.newList("ARRAY_LIST")
    lt.addLast(x, lt.getElement(listaordenada, 1))
    lt.addLast(x, lt.getElement(listaordenada, 2))
    lt.addLast(x, lt.getElement(listaordenada, 3))
    lt.addLast(x, lt.getElement(listaordenada, lt.size(listaordenada)-2))           
    lt.addLast(x, lt.getElement(listaordenada, lt.size(listaordenada)-1))
    lt.addLast(x, lt.getElement(listaordenada, lt.size(listaordenada)))
    return x,size,homesize,awaysize


def req_4(data_structs, tournament, start, end):
    """
    Función que soluciona el requerimiento 4
    """
    c = lt.newList("ARRAY_LIST")
    a = mp.get(data_structs['tournament'],tournament)
    b = me.getValue(a)['partidos']
    for cu in lt.iterator(b):
        if cu["date"] >= start and cu["date"] <= end:
                lt.addLast(c, cu)
    x = lt.newList("ARRAY_LIST")
    lt.addLast(x, lt.getElement(c, 1))
    lt.addLast(x, lt.getElement(c, 2))
    lt.addLast(x, lt.getElement(c, 3))
    lt.addLast(x, lt.getElement(c, lt.size(c)-2))           
    lt.addLast(x, lt.getElement(c, lt.size(c)-1))
    lt.addLast(x, lt.getElement(c, lt.size(c)))
    return x


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def sortear_fecha(datos):
    datos = datos[0]
    goles = datos["goles"]
    results = datos["results"]
    shootouts = datos["shootout"]

    sorted_list = (quk.sort(goles, compare_goalscorers), quk.sort(results, compare_results), quk.sort(shootouts, compare_shootouts))
    datos["goles"] = sorted_list[0]
    datos["results"] = sorted_list[1]
    datos["shootout"] = sorted_list[2]
    return sorted_list

def compare_goalscorers(goles1, goles2):
    if goles1["date"] > goles2["date"]:
        return goles1["date"]>goles2["date"]
    
    elif goles1["date"] == goles2["date"]:
        if goles1["minute"]>goles2["minute"]:
            return goles1["minute"]>goles2["minute"]
        elif goles1["minute"]==goles2["minute"]:
            return goles1["scorer"]>goles2["scorer"]

def compare_results(results1, results2):
    if results1["date"] > results2["date"]:
        return results1["date"]>results2["date"]
    
    elif results1["date"] == results2["date"]:
        return results1["home_score"]>results2["home_score"]

def compare_shootouts(s1, s2):
    if s1["date"] > s2["date"]:
        return s1["date"]>s2["date"]
    
    elif s1["date"] == s2["date"]:
        return s1["home_team"]>s2["home_team"]
    
def lista_reqs(lista, headers):
    t2 = {}
    final = {}   
    for header in headers:
        t1 = []
        for elemento in lt.iterator(lista):
            if header not in elemento:
                elemento[header] = "Unknown"
            else:
                t1.append(elemento[header])
        t2[header] = t1  
    for header in headers:
        if len(t2[header]) < 6:
            final = t2
        else:
            final[header] = [t2[header][0], t2[header][1], t2[header][2], t2[header][-3], t2[header][-2],t2[header][-1]]
    return final