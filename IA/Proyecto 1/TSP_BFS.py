import os
#Diccionarios de cada ciudad con sus hijos y respectivos costos
cities = {
    'Sib' : {'Fag':99, 'Rim':80, 'Ara':140, 'Ora':151},
    'Ora' : {'Sib':151, 'Zer':71},
    'Zer' : {'Ora':71, 'Ara':75},
    'Ara' : {'Sib':140, 'Zer':75, 'Tim':118},
    'Tim' : {'Ara':118, 'Lug':111},
    'Lug' : {'Tim':111, 'Meh':70},
    'Meh' : {'Lug':70, 'Dro':75},
    'Dro' : {'Meh':75, 'Cra':120},
    'Cra' : {'Dro': 120, 'Pit':138, 'Rim':146},
    'Rim' : {'Sib':80, 'Pit':97, 'Cra':146},
    'Pit' : {'Bu':101, 'Rim':97, 'Cra':138},
    'Fag' : {'Sib':99, 'Bu':211},
    'Bu' : {'Fag':211, 'Pit':101, 'Giu':90, 'Urz':85},
    'Giu' : {'Buc':90},
    'Urz' : {'Bu':85, 'Hir':98, 'Vas':142},
    'Hir' : {'Urz':98, 'Efo':86},
    'Efo' : {'Hir':86},
    'Vas' : {'Urz':142, 'Ia':92},
    'Ia' : {'Vas':92, 'Nea':87},
    'Nea' : {'Ia':87}
}
#Diccionario que almacena las ciudades y sus correspondientes numeros de hijos
ciudades = {'Sib':4, 'Ora': 2, 'Ara':3, 'Zer':2, 'Tim':2, 'Lug':2, 'Meh':2, 'Dro': 2, 
    'Cra':3, 'Rim':3, 'Pit':3, 'Fag':2, 'Bu':4, 'Giu':1, 'Urz':3, 'Hir':2, 'Efo':1, 'Vas':2, 'Ia':2, 'Nea':1}
#Lista que almacenara las ciudades solucion
soluciones = []
#listas que almacenara los datos de los nodos visitados
visitados_padre = []
visitados_hijo = []
#listas que almacenara los datos de los nodos visitar
visitar_padre = []
visitar_hijo = []
#Lista de ignorados de ignorados
ignorados_padre = []
ignorados_hijo = []

#Datos iniciales
#nodo_inicial = 'Sib'
#nodo_final = 'Urz'
#Funcion principal
def bfs(nodo_inicial, nodo_final):
    visitar_padre.append(nodo_inicial)
    visitar_hijo.append(nodo_inicial)
    flag_nodo_inicial = 1
    while visitar_hijo and visitar_padre:
        nodo_actual = [visitar_hijo[0], visitar_padre[0]]
        if verificar_nodo_final(nodo_actual, nodo_inicial, nodo_final) == 0:
            print('Se verifico el nodo final\n')
            os.system("pause")
            #Se debe agregar a visitados 
            if num_hijos_visitados(flag_nodo_inicial, nodo_actual) == 0:
                if agregar_visitados(nodo_actual) != 0:
                    print('Agrego visitados\n')
                    os.system("pause")
                    agregar_hijos(nodo_actual)
                    print('Se agregaron los hijos a visitar\n')
                os.system("pause")
                visitar_hijo.pop(0)
                visitar_padre.pop(0)
        else:
            print('Calculando solucion\n')
            sol = calcular_solucion()
            f = open("solucion.txt","a")
            f.write(soluciones)
            f.write(sol)
            f.close()
        flag_nodo_inicial = 0

#nodo_actual = [hijo (esta en), padre(viene de)]
def verificar_nodo_final(nodo_actual, nodo_inicial,nodo_final):
    hijo = nodo_actual[0]
    print('Hijo verificador nodo final: ', hijo)
    padre = nodo_actual[1]
    print('Padre verificador nodo final: ', padre)
    #Se verifica si el nodo final es el mismo que el nodo actual
    if padre == hijo == nodo_final:
        print('Estas en el mismo lugar')
        visitar_hijo.pop(0)
        visitar_padre.pop(0)
        return 1
    #Si no se esta en el mismo nodo se verifica si se llego al nodo final
    elif hijo == nodo_final:
        #Se comienza a agregar a la lista soluciones el nodo final
        soluciones.append(nodo_final)
        print('Solucion iniciada: ',soluciones)
        #Se obtiene la posicion de donde se encuentra el dato padre en la lista visitados_hijo
        posicion = visitados_hijo.index(padre)
        print('Dato padre: ', visitados_padre[posicion])
        #Bucle para buscar las conexiones hacia el nodo inicial
        while visitados_hijo[posicion] != nodo_inicial:
            #Se agrega a la lista soluciones la posicion del nodo hijo
            soluciones.append(visitados_hijo[posicion])
            #Se obtiene el dato padre que esta en la misma posicion pero en la otra lista
            dato_busqueda = visitados_padre[posicion]
            print('Dato de busqueda: ', dato_busqueda)
            #Se recalcula la poscion con el dato_busqueda
            posicion = visitados_hijo.index(dato_busqueda)
        #Se agrega el ultimo dato que no se agrego debido a que termina el bucle
        soluciones.append(visitados_padre[posicion])
        print(soluciones)
        if verificar_num_hijos(nodo_actual) == 1:
            #Obtiene la posicion del dato padre del nodo_actual en la lista visitados_hijo
            posicion = visitados_hijo.index(padre)
            #Se borran los datos de las listas visitados_hijo y visitados_padre
            ignorados_hijo.append(visitados_hijo.pop(posicion))
            ignorados_padre.append(visitados_padre.pop(posicion))
        visitar_hijo.pop(0)
        visitar_padre.pop(0)
        return 1
    else:
        return 0

def verificar_num_hijos(nodo_actual):
    padre = nodo_actual[1]
    print('Padre verificador num de hijos: ', padre)
    #Se obtiene la posicion de donde se encuentra el dato padre en la lista vistados_hijo
    posicion = visitados_hijo.index(padre)
    #Se obtiene el nieto del dato padre a través de la posicion del dato hijo en la lista visitados_padre
    nieto = visitados_padre[posicion]
    print('Nieto verificador num de hijos: ', nieto)
    #Se obtiene el numero de hijos a traves del diccionario ciudades
    num_hijos = ciudades.get(nieto)
    print(num_hijos)
    if num_hijos <= 2:
        return 1
    else:
        return 0

def agregar_visitados(nodo_actual):
    hijo = nodo_actual[0]
    print('Hijo agregar visitados: ', hijo)
    padre = nodo_actual[1]
    print('Padre agregar visitados: ', padre)
    flag_esta = 0
    for i in range(len(visitados_padre)):
        if padre in visitados_hijo[i]:
            if hijo in visitados_padre[i]:
                flag_esta = 1
    if flag_esta == 0:
        visitados_padre.append(padre)
        visitados_hijo.append(hijo)
        print('Visitados: ', visitados_hijo, ':', visitados_padre)
        return 1
    else:
        print('No se guarda. Ya existe')
        print('Visitados: ', visitados_hijo, ':', visitados_padre)
        return 0
    

def num_hijos_visitados(flag_nodo_inicial, nodo_actual):
    hijo = nodo_actual[0]
    if flag_nodo_inicial != 1:
        num_hijos = ciudades.get(hijo)
        print('Num hijos en num de hijos para visitados', num_hijos)
        if num_hijos <= 1:
            return 1
        else:
            return 0
    else:
        print('No entro por ser el nodo inicial')
        return 0

def agregar_hijos(nodo_actual):
    hijo = nodo_actual[0]
    print('Hijo AGREGAR HIJOS: ', hijo)
    #Se hace uso de un diccionario auxliar para acceder a las siguiente llaves
    dicc_aux = cities.get(hijo)
    #Por cada llave almacenada en el diccionario auxiliar
    for key in dicc_aux.keys():
        #Bandera que nos ayudara a verificar existencia en la lista de ignorados
        #Se coloca aqui para volver a inicializarla cada vez que se encuentre otra llave
        flag_esta_ignorados = 0
        #Bucle que analiza si encuentra los datos en la listas ignorados
        for i in range(len(ignorados_hijo)):
            if hijo in ignorados_hijo[i]:
                if key in ignorados_padre[i]:
                    print('Ignorados: ',i,hijo, key)
                    flag_esta_ignorados = 1
        #Bandera que nos ayudara a verificar existencia en la lista de visitados
        #Se coloca aqui para volver a inicializarla cada vez que se encuentre otra llave
        flag_esta_visitados = 0
        #Bucle que analiza si encuentra los datos en la listas visitados
        for j in range(len(visitados_padre)):
            if hijo in visitados_hijo[j]:
                if key in visitados_padre[j]:
                    flag_esta_visitados = 1
                    print('Visitados: ',j,hijo, key)
        #Condicional que agregara los datos analizados si no se encuentran en la lista de ignorados o en la lista de visitados
        if flag_esta_ignorados == 0 or flag_esta_visitados == 0:
            visitar_hijo.append(key)
            visitar_padre.append(hijo)
            print('Agregando a visitar')
            print('Hijos: ',visitar_hijo)
            print('Padres: ',visitar_padre)
        #Si si se encuentran en alguna lista se omite
        else:
            print('Ya se ha analizado')
            print('Hijos: ',visitar_hijo)
            print('Padres: ',visitar_padre)
#['Sib','Fag','Bu', 'Urz']
def calcular_solucion():
    suma = 0
    for i in range(len(soluciones)-1):
        padre = soluciones[i]
        print('Padre:',padre)
        hijo = soluciones[i+1]
        print('Hijo:',hijo)
        dicc_aux = cities.get(padre)
        suma += int(dicc_aux.get(hijo))
    print(suma)
    return suma

#Agregar un contador para analizar la lista de lugares
lugares = ['Sib','Urz']
for i in range(len(lugares)-1):
        inicio = lugares[i]
        print('Estoy en: ',inicio)
        fin = lugares[i+1]
        print('Quiero llegar a: ',fin)
        bfs(inicio, fin)
        #Se borran todas las listas al conluir con el primer par de nodos visitados
        soluciones.clear()
        visitados_padre.clear()
        visitados_hijo.clear()
        visitar_hijo.clear()
        visitar_padre.clear()
        ignorados_hijo.clear()
        ignorados_padre.clear()