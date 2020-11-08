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
    nodo_actual = [visitar_hijo[0], visitar_padre[0]]
    verificar_nodo_final(nodo_actual, nodo_final)
"""
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
        #Se obtiene la posicion de donde se encuentra el dato padre en la lista vistados_hijo
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
        return 1
    return 0

#bfs(nodo_inicial, nodo_final)
verificar_nodo_final(['Urz','Bu'], nodo_final)