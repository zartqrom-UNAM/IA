import os
#Diccionarios que almacena cada ciudad con sus hijos y respectivos costos
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
#Datos iniciales son de tipo string
#nodo_inicial = 'Sib'
#nodo_final = 'Urz'

#Funcion principal que maneja a las demas funciones
def bfs(nodo_inicial, nodo_final):
    #Se agrega el nodo inicial a la lista VISITAR
    visitar_padre.append(nodo_inicial)
    visitar_hijo.append(nodo_inicial)
    #Bandera que registra si es el nodo inicial para el analisis
    flag_nodo_inicial = 1
    #Bucle que se repite mientras las listas VISITAR_HIJO y VISITAR_PADRE no esten vacias
    while visitar_hijo and visitar_padre:
        print('Hijos LISTA VISITAR: ', visitar_hijo)
        print('Padre LISTA VISITAR: ', visitar_padre)
        print('Hijos LISTA IGNORADOS', ignorados_hijo)
        print('Padre LISTA IGNORADOS', ignorados_padre)
        #nodo_actual = [] se pone en forma de lista
        nodo_actual = [visitar_hijo[0], visitar_padre[0]]
        #Se verifica si el nodo_actual es el nodo final, si no lo es entra a hacer las instrucciones
        if verificar_nodo_final(nodo_actual, nodo_inicial, nodo_final) == 0:
            print('Se verifico el nodo final\n')
            #os.system("pause")
            #Se declara al nodo hijo del dato [0] del nodo_actual
            hijo = nodo_actual[0]
            #Se obtiene el numero de hijos que tiene el nodo hijo, es decir el valor en el diccionario ciudades
            num_hijos = ciudades.get(hijo)
            print('Num hijos en num de hijos para visitados\n', num_hijos)
            #Validador del numero de hijos de HIJO
            # si tiene menos o igual a 1 hijo y es el primer análisis continua
            #Este analisis es para el caso de que se presente un nodo aislado como Giurgiu
            if num_hijos <= 1 and flag_nodo_inicial == 1:
                #Llama a la funcion agregar a visitados para verificar que no se encuentre ya en la lista
                #Sino se encuentra se agregan
                if agregar_visitados(nodo_actual) != 0:
                    print('Agrego visitados\n')
                    #os.system("pause")
                    agregar_hijos(nodo_actual)
                    print('Se agregaron los hijos a visitar\n')
                #os.system("pause")
                #Se saca el dato de analisis de la listas VISITAR para el siguiente analisis
                visitar_hijo.pop(0)
                visitar_padre.pop(0)
            #en caso de que el numero de hijos es mayor a 1 se verifica en AGREGAR_VISITADOS    
            elif num_hijos > 1:
                if agregar_visitados(nodo_actual) != 0:
                    print('Agrego visitados\n')
                    #os.system("pause")
                    agregar_hijos(nodo_actual)
                    print('Se agregaron los hijos a visitar\n')
                #os.system("pause")
                #Se saca el dato de analisis de la listas VISITAR para el siguiente analisis
                visitar_hijo.pop(0)
                visitar_padre.pop(0)
            else:
                #Se saca el dato de analisis de la listas VISITAR para el siguiente analisis
                visitar_hijo.pop(0)
                visitar_padre.pop(0)
        else:
            print('Calculando solucion\n')
            #Se almacena la suma final de solucion en forma de String
            sol = str(calcular_solucion())
            #Se abre un documento txt con "a" para agregar al final del archivo sin borrar lo que haya dentro
            f = open("solucion.txt","a")
            #Ciclo que manda la cadena obtenida de soluciones hacia el documento
            for cadena in soluciones:
                f.write(cadena+' ')
            #Se adiciona el dato de la suma al concluir de escribir las ciudades 
            f.write(sol+'\n')
            f.close()
        #Sentencia que declara que ya se realizo el primer analisis
        flag_nodo_inicial = 0

#nodo_actual = [hijo (esta en), padre(viene de)]
#Funcion que verifica si el nodo actual es el nodo final
def verificar_nodo_final(nodo_actual, nodo_inicial, nodo_final):
    #Se establece de la lista ingresada de nodo_actual quien es el nodo padre y el nodo hijo
    hijo = nodo_actual[0]#urz
    print('Hijo verificador nodo final: ', hijo)
    padre = nodo_actual[1]#Buc
    print('Padre verificador nodo final: ', padre)
    #Se verifica si el nodo final es el mismo que el nodo actual, es decir estas en el mismo lugar
    if padre == hijo == nodo_final:
        print('Estas en el mismo lugar')
        #Se tiene que sacar el dato
        visitar_hijo.pop(0)
        visitar_padre.pop(0)
        return 1
    #Si no se esta en el mismo nodo se verifica si se llego al nodo final con el nodo hijo
    elif hijo == nodo_final:
        #Se limpia la lista soluciones en el caso de ya haber sido utilizada
        soluciones.clear()
        #Se comienza a agregar a la lista soluciones el nodo final
        soluciones.append(nodo_final)
        print('Solucion iniciada: ',soluciones)
        #Se obtiene la posicion de donde se encuentra el dato padre en la lista visitados_hijo
        #Urz:Bu
        #Bu:Fag
        #Fag:sib
        posicion = visitados_hijo.index(padre)
        print('Dato padre: ', visitados_padre[posicion])
        #Bucle para buscar las conexiones hacia el nodo inicial a traves de los indices
        while visitados_hijo[posicion] != nodo_inicial:
            #Se agrega a la lista soluciones la posicion del nodo hijo en la lista VISITADOS_HIJO 
            soluciones.append(visitados_hijo[posicion])
            #Se obtiene el dato padre que esta en la misma posicion pero en la otra lista
            dato_busqueda = visitados_padre[posicion]
            print('Dato de busqueda: ', dato_busqueda)
            #Se recalcula la poscion del siguiente hijo con el dato_busqueda
            posicion = visitados_hijo.index(dato_busqueda)
        #Se agrega el ultimo dato que no se agrego debido a que termina el bucle
        soluciones.append(visitados_padre[posicion])
        print(soluciones)
        #Verificador que checa las conexiones con  otros nodos para ver si se conserva, sino para desecharlo
        if verificar_num_hijos(nodo_actual) == 1:
            #Obtiene la posicion del dato padre del nodo_actual en la lista visitados_hijo
            posicion = visitados_hijo.index(padre)
            #Se borran los datos de las listas visitados_hijo y visitados_padre
            #Antes se agregan los datos a las listas IGNORADOS  
            print('***SE IGNORA hijo: ', visitados_hijo[posicion])
            ignorados_hijo.append(visitados_hijo[posicion])
            visitados_hijo.pop(posicion)
            print('***SE IGNORA padre: ', visitados_padre[posicion])
            ignorados_padre.append(visitados_padre[posicion])
            visitados_padre.pop(posicion)
        #Se saca el nodo que se analizaba de la lista VISITAR
        visitar_hijo.pop(0)
        visitar_padre.pop(0)
        return 1
    else:
        return 0

#Funcion que verifica el numero de hijos del nodo nieto del nodo actual para verificar si hay que desecharlo
def verificar_num_hijos(nodo_actual):
    padre = nodo_actual[1]#Bu
    print('Padre verificador num de hijos: ', padre)
    #Se obtiene la posicion de donde se encuentra el dato padre en la lista vistados_hijo
    posicion = visitados_hijo.index(padre)
    #Se obtiene el nieto del dato padre a través de la posicion del dato hijo en la lista visitados_padre
    nieto = visitados_padre[posicion]
    print('Nieto verificador num de hijos: ', nieto)
    #Se obtiene el numero de hijos del nieto a traves del diccionario ciudades
    num_hijos = ciudades.get(nieto)
    print(num_hijos)
    if num_hijos <= 2:
        return 1
    else:
        return 0

#Funcion que se encarga del analisis en las listas VISITADOS y agrega los datos del nodo actual en caso de no estar
def agregar_visitados(nodo_actual):
    hijo = nodo_actual[0]#Urz
    print('Hijo agregar visitados: ', hijo)
    padre = nodo_actual[1]#Buc
    print('Padre agregar visitados: ', padre)
    #Dato bandera que se activara si se encuentra el par de datos en las listas
    flag_esta = 0
    #Ciclo que verifica si los datos almacenados en padre e hijo se encuentran en las posiciones homologas, es decir, [0,0],[1,1]...
    for i in range(len(visitados_padre)):
        if hijo in visitados_hijo[i]:#0
            if padre in visitados_padre[i]:#0
                flag_esta = 1
    #Si no se encuentran en las listas VISITADOS se pueden agregar
    if flag_esta == 0:
        visitados_padre.append(padre)
        visitados_hijo.append(hijo)
        print('Hijo Visitados: ', visitados_hijo)
        print('Padre Visitados:', visitados_padre)
        return 1
    #Si ya se encuentran se descartan
    else:
        print('No se guarda. Ya existe')
        print('Hijo Visitados: ', visitados_hijo)
        print('Padre Visitados: ', visitados_padre)
        return 0

#Funcion que agrega los hijos del nodo actual a las listas VISITAR
def agregar_hijos(nodo_actual):
    hijo = nodo_actual[0]#Fag
    print('Hijo AGREGAR HIJOS: ', hijo)
    #Se hace uso de un diccionario auxliar para acceder a las siguiente llaves que estan almacenadas en otro diccionario
    dicc_aux = cities.get(hijo)
    #Por cada llave (padre) almacenada en el diccionario auxiliar
    for key in dicc_aux.keys():
        #Bandera que nos ayudara a verificar existencia en la lista de ignorados
        #Se coloca aqui para volver a inicializarla cada vez que se encuentre otra llave
        flag_esta_ignorados = 0
        #Bucle que analiza si encuentra los datos en la listas IGNORADOS con sus homologos [0,0],[1,1]...
        for i in range(len(ignorados_hijo)):
            if key in ignorados_hijo[i]:
                if hijo in ignorados_padre[i]:
                    print('Ignorados: ',i,hijo, key)
                    flag_esta_ignorados = 1
        #Bandera que nos ayudara a verificar existencia en la lista de visitados
        print(flag_esta_ignorados)
        #Se coloca aqui para volver a inicializarla cada vez que se encuentre otra llave
        flag_esta_visitados = 0
        #Bucle que analiza si encuentra los datos en la listas VISITADOS con sus homologos [0,0],[1,1]...
        for j in range(len(visitados_padre)):
            if key in visitados_hijo[j]:
                if hijo in visitados_padre[j]:
                    flag_esta_visitados = 1
                    print('Esta en visitados: ',j, hijo, key)
        #Condicional que agregara los datos analizados si no se encuentran en la lista de IGNORADOS y en la lista de VISITADOS
        if flag_esta_ignorados == 0 and flag_esta_visitados == 0:
            #Se agregan al final de las listas VISISTAR
            visitar_hijo.append(key)
            visitar_padre.append(hijo)
            print('Agregando a visitar')
            print('Hijos: ',visitar_hijo)
            print('Padres: ',visitar_padre)
        #Si si se encuentran en alguna lista se omiten los datos
        else:
            print('Ya se ha analizado')
            print('Hijos: ',visitar_hijo)
            print('Padres: ',visitar_padre)
            
#['Sib','Fag','Bu', 'Urz']
#Funcion que toma los datos de la lista SOLUCIONES y busca sus valores en el diccionario de diccionarios retornando la suma total
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

#Lista que alcenara los lugares que se deben visitar
lugares = ['Sib','Urz']
for i in range(len(lugares)-1):
        inicio = lugares[i]
        print('Estoy en: ',inicio)
        fin = lugares[i+1]
        print('Quiero llegar a: ',fin)
        #Se mandan los datos a la funcion principal
        bfs(inicio, fin)
        #Se borran todas las listas al conluir con el primer par de nodos visitados
        soluciones.clear()
        visitados_padre.clear()
        visitados_hijo.clear()
        visitar_hijo.clear()
        visitar_padre.clear()
        ignorados_hijo.clear()
        ignorados_padre.clear()