# Declaracion de una lista para almacenar los numeros
numeros=[]

# Contador para la cantidad de numeros de la lista
contar_numeros = 0

'''Bucle while para ingreso de los numeros en la lista, 
se ejecuta hasta que se ingresaron 5 numeros'''

while contar_numeros<5:
    try:
        
        num=int(input("Ingrese un numero entero "))
        #agregamos el numero a la lista 
        numeros.append(num)
        # incremente del contador de numeros ingresados
        contar_numeros += 1
    except Exception:
            print("Error de formato") 
        
         
#Suma de los numeros
def sumar_lista(lista):
    suma = 0
    
    for  numero in lista:
        suma += numero
        
    return suma





#Calculo del promedio
   

#Encontrando el maximo  de los numeros  


#Encontrando el minimo  de los numeros  

def minimo_lista(numeros):
    # inicialmente el minimo sera el primer numero de la lista

    minimo=numeros[0]
    #Seguimos recorriendo la lista  a partir del segundo valor

    for i in range(1,len(numeros)):
        # si el valor de la lista es memor que el minimo ,
        # asignamos este valor a minimo
         
        if(numeros[i]< minimo):
	        minimo=numeros[i]	
    return minimo


# Mostramos la suma, el promedio ,el maximo y el minimo
# de los numeros de la lista

print("La suma de los numeros es ",sumar_lista(numeros))
#print("El promedio de los numeros es ",promedio_lista(numeros))
#print("El mayor  de los numeros es ",maximo_lista(numeros))
print("El menor de los numeros es ",minimo_lista(numeros))
