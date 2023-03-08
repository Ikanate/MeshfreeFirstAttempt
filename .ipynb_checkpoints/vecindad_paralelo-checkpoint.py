#Biblitecas
import numpy as np
from shapely import Point

def pts_vecindad(arr,pt_c,h):
    
    """
    Objetivo: El objetivo de la funcion es encontrar todos los puntos (x,y) que se encuentran dentro de 
    una vecindad circular con cierto radio R y regresar los indices correspondientes 
    
    Datos de entrada:
        arr:
            Arreglo tipo numpy
            Dimensiones   ->    (renglones,columnas)
                                (        N,       2)
                                N es un numero entero deseado
        pt_c:
            Arreglo tipo numpy o lista, preferiblemente un arreglo
            Dimensiones   ->    (renglones,columnas)
                                (        1,       2)
        h:
            Variable tipo flotante
    Datos de salida:
        indices_arr:
            Arreglo tipo numpy con tipo de dato np.float64
            Dimensiones   ->    (renglones,columnas)
                                (        M,       1)
                                M es la canatidad de indices que la funcion encuentre
                                dentro de la vecindad
    nota: Se espera que una futura implementación permita tambien reducir la cantidad de calculos
          tomando encuenta que un pt1 ya se encuentra en la vecindad de otro pt2, por lo que pt2
          es parte de la vecindad de pt1
          
    """
    arr_u = np.array(arr,copy=True)
    N = len(arr_u)
    
    indices_arr = np.zeros((N,1),np.float64)
    
    #Cuenta cuantos pts caen dentro de la vecindad
    cont_in_h = 0
    
    
    for i in range(0,N):
        
        #Observamos que no haya dos puntos iguales mas de dos veces, por que si hay dos puntos iguales
        #mas de dos veces tenemos un error en nuestro filtrado de puntos en el poligono
        
        
        #Observamos si la distancia entre los puntos pt_c, y arr_u[i] es menor que
        #el radio de la vecindad y 
        distance = Point(pt_c[0],pt_c[1]).distance(Point(arr_u[i,0],arr_u[i,1]))
        if (h > distance) and (distance!=0.0):
            #Si es menor entonces guardamos el indice y aumentamos el contador
            indices_arr[cont_in_h,0] = i
            cont_in_h +=1
        elif distance==0.0:
            continue
            
    #Regresamos un indice con esos datos y solo esos datos
    return indices_arr[:cont_in_h]


def vecindad_paralelo_proceso(h,Ni,Nf,pt_g_u):  
    """
    Objetivo funcion
    Darle en la madre a todos
    """
    #En este arreglo guardaremos los puntos vecinos de cada punto
    #que toca
    pts_veci_local_lista = []
    for i in range(Ni,N_f):
        indices_arr = pts_vecindad(pt_g_u[:,:],pt_g[i,:])
        indices_arr_lista = indices_arr.astype(int).flatten().tolist()
        pts_veci_local_lista.append(indices_arr_lista)
    return pts_veci_local_lista

