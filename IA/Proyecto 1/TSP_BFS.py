soluciones = []
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
            while dato_busqueda != nodo_inicial:
                soluciones.append(dato_busqueda)
                print('Valor de dato_busqueda primero')
                print(dato_busqueda)
                dato_busqueda = visitados.get(dato_busqueda)
                print('Valor de dato_busqueda despues')
                print(dato_busqueda)
            soluciones.append(dato_busqueda)
            print(soluciones)
            return 1
    else:
        if nodo_actual_aux == nodo_final:
            print("Estas en el origen")
            return 1
    return 0

def verificacion_num_hijos(nodo_actual):
    nodo_actual_aux = nodo_actual #{key:value}
    #Se obtiene el dato para conocer quien es el hijo
    hijo = list(nodo_actual_aux.values())
    nieto = visitados.get(hijo)



verificar_nodo_final({'Sib':'Rim'},'Giu','Sib')