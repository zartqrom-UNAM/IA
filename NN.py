import pandas as pd
import numpy as np

"""
Definicion de la funcion net de los pesos
w0+wi*xi
Retorna una lista donde se almecenan los resultados
"""
def funcion_net_w(w,x):
    datos_sal = []
    m = 1
    for i in range(len(x)):
        net = w[0]
        for j in range(len(x[i])):
            net += w[m]*x[i][j]
            m += 1
        datos_sal.append(net)
    return datos_sal

"""
Definicion de la funcion sigmoide
Retorna el valor de la operacion
"""
def sigmoid(net):
    return 1 / (1 + np.exp(-net))

"""
Definicion de la funcion net de los vias
v0+vi*yi
Retorna una lista donde se almecenan los resultados
"""
def funcion_net_z(v,y):
    j=1
    datos_sal = []
    while j < len(v):
        net = float(v[0])
        #print('Dato v: ', v[0])
        #print('Suma = ', str(net))
        for i in y:
            v_aux = float(v[j])
            y_aux = float(i)
            net += v_aux * y_aux
            print("Numero: ", j)
            j += 1
        datos_sal.append(net)
    return datos_sal

"""
Definicion de la funcion que calcula
el error de cada par de datos
Retorna el valor de la operacion
"""
def calculo_error(t,z):
    #print('Valor de t: ',t)
    #print('Valor de z: ',z)
    potencia = np.power(t-z,2)
    #print(potencia)
    return (1/2)*(potencia)

"""
Definicion de la funcion que calcula las operaciones
de cada derivada
Retorna el producto de los resultados obtenidos
"""
def backward(z, t, y):
    res_der_z = derivada_z(z, t)
    res_der_net = derivada_net(z)
    derivada_vias = y
    return res_der_z*res_der_net*derivada_vias

def derivada_z(z, t):
    return z-t

def derivada_net(z):
    return z*(1-z)

"""
Definicion de la funcion que calcula los nuevos valores
de los vias
Retorna el valor de la operacion
"""
def calculo_nuevos_vias(v, grado_aprendizaje, derivada):
    return v-grado_aprendizaje*derivada

"""
Defincion del metodo principal
"""

def main():
    #Datos para analisis
    grado_aprendizaje = .5
    tolerancia = .28

    #Obtencion de los datos de un archivo excel
    datos_entrenamiento = pd.read_excel('datos.xlsx')

    #Almacenamiento de los datos objetivo
    target = datos_entrenamiento['t']

    #Tamaño de los datos en el archivo
    num_datos = len(datos_entrenamiento)

    #Numero de columnnas presentes en el archivo
    num_x = len(datos_entrenamiento.columns)

    #Obtencion de los datos independientes
    df_x = datos_entrenamiento.iloc[:, 1:num_x]

    #Numero de x presentes en el archivo
    num_x = len(datos_entrenamiento.columns)-1

    #Transifere los datos Dataframe a array
    x = df_x.to_numpy()

    tam_datos_wv = num_datos*num_x

    w = np.random.rand(tam_datos_wv+1)
    v = np.random.rand(tam_datos_wv+1)

    #w = [.35, .15, .2, .25, .3]
    #v = [.6, .4, .45, .5, .55]

    print("Datos W: ", w)
    print()
    print("Datos V: ", v)
    print()

    error = 1
    repeticion = 1

    """*************Backpropagation: Forward*********************"""

    """
    Calculo de la funcion net de "y" 
    que se almacena en la lista net_y
    """
    net_y = []
    net_y = funcion_net_w(w, x)
    print("Datos net_y: ", net_y)
    
    """
    Definicion de la lista de almacenaciento "y" a partir de la 
    funcion sigmoide
    """
    y = []
    for elem in net_y:
        y.append(sigmoid(elem))
    print('Los datos de y son: ', y)

    #Obtencion de la lista calculada del net de los vias
    net_z = funcion_net_z(v, y[0:num_x])
    print('Los datos net_z son: ', net_z)

    """
    Definicion de la lista de almacenaciento "z" a partir de la 
    funcion sigmoide
    """
    z = []
    for elem in net_z:
        z.append(sigmoid(elem))
    print('Los datos de z son: ', z)
    print()
    
    error = 0
    contador = 0
    while contador < num_datos:
        error += calculo_error(target[contador], z[contador])
        contador += 1
        #print('Error ', contador, ":", error)

    print('ERROR TOTAL = ', error)
    print("****************************************************************")

    """*************Backpropagation: Backward*********************"""
    #Calculo de las derivadas y se almacenan en la lista prod_derivadas
    prod_derivadas_vias = []
    contador = 0
    while contador < num_datos:
        for num_y in y:
            prod_derivadas_vias.append(backward(z[contador], target[contador], num_y))
        contador += 1

    #print('Resultado de producto de derivadas: ', prod_derivadas_vias)

    #Calculo de los nuevos vias almacenados en la lista aux_vias
    aux_vias = []
    aux_vias.append(v[0])
    for elem in range(len(v)-1):
        aux_vias.append(calculo_nuevos_vias(v[elem+1], grado_aprendizaje, prod_derivadas_vias[elem]))
    print("Nuevas v: ", aux_vias)
    print("Tamaño de nuevos V: ", len(aux_vias))

    derivada_error = 0
    for elem in range(len(z)):
        derivada_error += backward(z[elem], target[elem], v[2*elem+1])
    
    #print("Derivada error: ", derivada_error)

    prod_derivadas_pesos = []
    der_net_x = derivada_net(y[1])
    """contador = 0
    while contador < num_datos:
        for num_x in x:
            prod_derivadas_pesos.append(float(derivada_error*der_net_x*num_x))
        contador += 1"""
    
    for i in range(len(x)):
        for j in range(len(x[i])):
            prod_derivadas_pesos.append(float(derivada_error*der_net_x*x[i][j]))

    #print("Productos de las derivadas del peso: ", prod_derivadas_pesos)

    #Calculo de los nuevos vias almacenados en la lista aux_vias
    aux_pesos = []
    aux_pesos.append(w[0])
    for elem in range(len(w)-1):
        aux_pesos.append(calculo_nuevos_vias(w[elem+1], grado_aprendizaje, prod_derivadas_pesos[elem]))
    print("Nuevos w: ", aux_pesos)
    print()

    w = aux_pesos
    v = aux_vias

main()
