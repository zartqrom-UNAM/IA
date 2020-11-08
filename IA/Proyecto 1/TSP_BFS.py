#Diccionarios de cada ciudad con sus hijos y respectivos costos
Sib = {'Fag':99, 'Rim':80, 'Ara':140, 'Ora':151}
Ora = {'Sib':151, 'Zer':71}
Zer = {'Ora':71, 'Ara':75}
Ara = {'Sib':140, 'Zer':75, 'Tim':118}
Tim = {'Ara':118, 'Lug':111}
Lug = {'Tim':111, 'Meh':70}
Meh = {'Lug':70, 'Dro':75}
Dro = {'Meh':75, 'Cra':120}
Cra = {'Dro': 120, 'Pit':138, 'Rim':146}
Rim = {'Sib':80, 'Pit':97, 'Cra':146}
Pit = {'Bu':101, 'Rim':97, 'Cra':138}
Fag = {'Sib':99, 'Bu':211}
Bu = {'Fag':211, 'Pit':101, 'Giu':90, 'Urz':85}
Giu = {'Buc':90}
Urz = {'Bu':85, 'Hir':98, 'Vas':142}
Hir = {'Urz':98, 'Efo':86}
Efo = {'Hir':86}
Vas = {'Urz':142, 'Ia':92}
Ia = {'Vas':92, 'Nea':87}
Nea = {'Ia':87}
#Lista que almacena los diccionarios de cada ciudad
cities = [Sib, Ora, Zer, Ara, Tim, Lug, Meh, Dro, Cra, Rim, Pit, Fag, Bu, Giu, Urz, Hir, Efo, Vas, Ia, Nea]
#Diccionario que almacena las ciudades y sus correspondientes numeros de hijos
ciudades = {'Sib':4, 'Ora': 2, 'Ara':3, 'Zer':2, 'Tim':2, 'Lug':2, 'Meh':2, 'Dro': 2, 
    'Cra':3, 'Rim':3, 'Pit':3, 'Fag':2, 'Bu':4, 'Giu':1, 'Urz':3, 'Hir':2, 'Efo':1, 'Vas':2, 'Ia':2, 'Nea':1}
#Lista que almacenara las ciudades solucion
soluciones = []
#listas que almacenara los datos de los nodos visitados
visitados_padre = ['Sib','Sib','Sib','Fag']
visitados_hijo = ['Sib','Fag','Rim','Bu']
#listas que almacenara los datos de los nodos visitar
visitar_padre = []
visitar_hijo = []
#Lista de ignorados de ignorados
ignorados_padre = []
ignorados_hijo = []

#Datos iniciales
nodo_inicial = 'Sib'
nodo_final = 'Urz'
"""
#Funcion principal
def bfs(nodo_inicial, nodo_final):
    visitar_padre.append(nodo_inicial)
    visitar_hijo.append(nodo_inicial)
    flag_nodo_inicial = 1
    nodo_actual = [visitar_hijo[0], visitar_padre[0]]
    verificar_nodo_final(nodo_actual, nodo_final)
    agregar_hijos(flag_nodo_inicial, nodo_actual)

#nodo_actual = [hijo (esta en), padre(viene de)]
def verificar_nodo_final(nodo_actual, nodo_final):
    hijo = nodo_actual[0]
    print('Hijo: ', hijo)
    padre = nodo_actual[1]
    print('Padre: ', padre)
    #Se verifica si el nodo final es el mismo que el nodo actual
    if padre == hijo == nodo_final:
        print('Estas en el mismo lugar')
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
            visitados_hijo.pop(posicion)
            visitados_padre.pop(posicion)
        visitar_hijo.pop(0)
        visitados_padre.pop(0)
        return 1
    return 0

def verificar_num_hijos(nodo_actual):
    padre = nodo_actual[1]
    print('Padre: ', padre)
    #Se obtiene la posicion de donde se encuentra el dato padre en la lista vistados_hijo
    posicion = visitados_hijo.index(padre)
    #Se obtiene el nieto del dato padre a través de la posicion del dato hijo en la lista visitados_padre
    nieto = visitados_padre[posicion]
    print('Nieto: ', nieto)
    #Se obtiene el numero de hijos a traves del diccionario ciudades
    num_hijos = ciudades.get(nieto)
    print(num_hijos)
    if num_hijos <= 2:
        return 1
    return 0

def agregar_visitados(flag_nodo_inicial, nodo_actual):
    if flag_nodo_inicial != 1:
        hijo = nodo_actual[0]
        print('Hijo: ', hijo)
        padre = nodo_actual[1]
        print('Padre: ', padre)
        flag_esta = 0
        for i in range(len(visitados_padre)):
            if hijo in visitados_hijo[i]:
                if padre in visitados_padre[i]:
                    flag_esta = 1
        if flag_esta == 0:
            visitados_padre.append(padre)
            visitados_hijo.append(hijo)
        else:
            print('No se guarda. Ya existe')
        print('Visitados: ', visitados_hijo, ':', visitados_padre)
    else:
        print('No entro por ser el nodo inicial')
"""
def agregar_hijos(nodo_actual):
    hijo = nodo_actual[0]
    print('Hijo: ', hijo)
    for key in 
#bfs(nodo_inicial, nodo_final)