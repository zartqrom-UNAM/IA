solucion = []
def verificar_nodo_final(nodo_actual, nodo_final):
    nodo_actual_aux = nodo_actual #{key:value}
    if type(nodo_actual_aux) == dict:
        dato_aux = list(nodo_actual_aux.keys())
        if dato_aux[0] = nodo_final:
            solucion.append(nodo_final) 
            #get solo retorna el valor de la llave ingresada
            dato_busqueda = nodo_actual_aux.get(nodo_final)

    else:
        if nodo_actual_aux == nodo_final:
            print("Estas en el origen")
            return 1
    return 0