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
#Diccionario que almacenara los datos de los nodos visitados
visitados = {'Giu':'Giu','Bu':'Giu','Pit':'Bu','Rim':'Pit'}

def verificar_nodo_final(nodo_actual, nodo_inicial, nodo_final):
    nodo_actual_aux = nodo_actual #{key:value}
    #Corrobora el tipo de entrada
    if type(nodo_actual_aux) == dict:
        #Obtiene la llave
        dato_aux = list(nodo_actual_aux.keys())
        if dato_aux[0] == nodo_final:
            soluciones.append(nodo_final)
            #get solo retorna el valor de la llave buscando la clave ingresada en los parentesis    
            dato_busqueda = nodo_actual_aux.get(nodo_final)
            #El loop esta para buscar las conexiones hacia el nodo inicial
            while dato_busqueda != nodo_inicial:
                #Se agrega el dato de busqueda a la lista soluciones
                soluciones.append(dato_busqueda)
                print('Valor de dato_busqueda primero')
                print(dato_busqueda)
                #Se redefine dato_busqueda con llave del hijo del paso anterior
                dato_busqueda = visitados.get(dato_busqueda)
                print('Valor de dato_busqueda despues')
                print(dato_busqueda)
            #Se agrega el que seria el nodo incial presente en dato_busqueda
            soluciones.append(dato_busqueda)
            print(soluciones)
            return 1
    else:
        #Verificacion cuando solo se ingresa un string y es el mismo donde nos entrogamos
        if nodo_actual_aux == nodo_final:
            print("Estas en el origen")
            return 1
    #Se devuelve cero si no se encuentra solucion
    return 0

def verificacion_num_hijos(nodo_actual):
    nodo_actual_aux = nodo_actual #{key:value}
    #Se obtiene el dato para conocer quien es el hijo
    hijo = list(nodo_actual_aux.values())
    #Se obtiene el nieto para obtener su numero de hijos guardado en el diccionario ciudades
    nieto = visitados.get(hijo)
    num_hijos = ciudades.get(nieto)
    if num_hijos <= 2:
        return 1
    return 0


verificar_nodo_final({'Sib':'Rim'},'Giu','Sib')