"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

default_limit = 1000

sys.setrecursionlimit(default_limit*10)

def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Listar los últimos N partidos de un equipo")
    print("3- Listar los primeros N goles anotados por un jugador")
    print("4- Consultar los partidos que disputó un equipo durante un periodo")
    print("5- Consultar los partidos relacionados con un torneo durante un periodo")
    print("6- Consultar las anotaciones de un jugador durante un periodo")
    print("7- Clasificar los N mejores equipos de un torneo en un periodo")
    print("8- Clasificar los N mejores anotadores en partidos oficiales dentro de un periodo")
    print("9- Comparar el desempeño histórico de dos selecciones en torneos oficiales")
    print("0- Salir")


def load_data(control, goles, results):
    """
    Carga los datos
    """
    return controller.load_data(control, goles, results) 

def load_first(control):
    """
    Carga los datos
    """
    filename = ('football/goalscorers-utf8-large.csv', 'football/results-utf8-large.csv', 'football/shootouts-utf8-large.csv')
    return controller.load_first(control, filename)

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    head = ["date","home_team","away_team","home_score","away_score","country","city","tournament"]
    matches = int(input("Number of matches: "))
    team = input("Team name: ")
    condition = input("Team condition: ")
    a = controller.req_1(control, matches, team, condition)
    tab = controller.tabular(a, head)
    t = tabulate(tab,headers="keys",tablefmt="grid",maxcolwidths = [10,13,13,10,10,20])
    return t


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    head = ["date","home_team","away_team","team","scorer","minute","own_goal","penalty"]
    scores = int(input("Number of scores: "))
    player_name = input("Player name: ")
    a = controller.req_2(control, scores, player_name)
    t2 = controller.lista_tabulate(a, head)
    tabulate_results = controller.tabla(t2)
    t = tabulate(tabulate_results,headers= head,tablefmt="grid",maxcolwidths = [10,13,13,10,10,20])
    return print(t)

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print("=============== Req No. 3 Inputs ===============")
    equipo = input("Team name: ")
    inicio = input("Start date:")
    final = input("End date: ")
    print("=============== Req No. 3 Results ===============")
    head = ["date","home_score","away_score","home_team","away_team","country","city","tournament","penalty","own_goal"]
    solreq3,size,z,k,t= controller.req_3(control,equipo,inicio,final)
    delta_time = f"{t:.3f}"
    tabla = controller.tabular(solreq3,head)
    fin = tabulate(tabla,headers=head,tablefmt="grid")
    print(equipo+ " Total games: " + size)
    print(equipo+ " Total home games: "+ str(z))
    print(equipo+ " Total away games: "+str(k))
    print("Para", equipo, "entre",inicio,"y",final, "delta tiempo:", str(delta_time),"[ms]")
    return fin


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    head = ["date","tournament","country","city","home_team","home_team","away_team","home_score","away_score","winner"]
    start = input("Start date: ")
    end = input("End date: ")
    tournament = input("Tournament name: ")
    a = controller.req_4(control, tournament, start, end)
    tab = controller.tabular(a, head)
    t = tabulate(tab,headers="keys",tablefmt="grid",maxcolwidths = [10,13,13,10,10,20])

    return print(t)

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_first(control)
            sorteado = controller.sort_fecha(control)
            load_data(control, sorteado[0], sorteado[1])
            print("Cargado con exito")
        elif int(inputs) == 2:
            print(print_req_1(control))

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
