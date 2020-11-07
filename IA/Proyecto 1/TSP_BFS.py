solucion = []
def verificar_nodo_final(nodo_actual, nodo_final):
    nodo_actual_aux = nodo_actual #{key:value}
    print(type(nodo_actual_aux))
    if type(nodo_actual_aux) == dict:
        dato_aux = list(nodo_actual_aux.keys())
        print(dato_aux[0])
        if dato_aux[0] == nodo_final:
            solucion.append(nodo_final)
            print(solucion) 
            #get solo retorna el valor de la llave ingresada
            dato_busqueda = nodo_actual_aux.get(nodo_final)
            print(dato_busqueda)
            solucion.append(dato_busqueda)
            print(solucion)

    else:
        if nodo_actual_aux == nodo_final:
            print("Estas en el origen")
            return 1
    return 0

nodo_actual = {'Bu':'Giu'}
nodo_final = 'Bu'
verificar_nodo_final(nodo_actual, nodo_final)