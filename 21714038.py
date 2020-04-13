import sys
import math
import random
sys.stdin.encoding
from random import *
'UTF-8' 
from builtins import str

correo = "correo@gmail.com"
expediente = 21714038

def Ej_A_QuickSort(list):#Complejidad [O(n^2)]

    left = []
    mid = []
    right = []

    if len(list) > 1:

        pivot = list[0]

        for i in list:

            if i < pivot:

                left.append(i)

            elif i == pivot:

                mid.append(i)

            elif i > pivot:

                right.append(i)

        return Ej_A_QuickSort(left)+mid+Ej_A_QuickSort(right)

    else:

        return list    

def Ej_A_Mediana (list):#Complejidad [O(2n)]

    if(len(list)%2!=0):

        pos =int((len(list)/2)+1)

        print("Es impar",
        ", La posicion de la mediana es ",pos,"y su valor es ",list[pos-1])
    else:

        pos =int((len(list)/2))
        dato = list[pos-1]+list[pos]
        med = dato/2

        print("Es par y la mediana es: ", med)
 
def Ej_A_Ordenar(list1,list2):#Complejidad [O(n)]

    for i in range (0,len(list2)):
        list1.append(list2[i])

    print("lista sin ordenar: ",list1)

    list1 = Ej_A_QuickSort(list1)

    print("lista ordenada: ",list1)

    return list1       





def Ej_C_Trasponer(m , a, b, c, d):#Complejidad [O(n)]

    if(a<b):

        fmedio = int((a+b)/2)
        cmedio = int((c+d)/2)

        Ej_C_Trasponer(m, a, fmedio, c, cmedio)
        Ej_C_Trasponer(m, a, fmedio, cmedio+1, d)
        Ej_C_Trasponer (m, fmedio+1, b, c, cmedio)
        Ej_C_Trasponer (m, fmedio+1, b, cmedio+1, d)

        matriz =Ej_C_Intercambio (m, fmedio+1, c, a, cmedio+1, b-fmedio)
        return matriz
        
def Ej_C_Intercambio(m, x, y,z,w,d):#Complejidad[O(n^2)]

    a = 0
    b = 0
    while a<= d-1:

        while b<= d-1:

            aux = m[x+a][y+b]
            m[x+a][y+b] = m[z+a][w+b]
            m[z+a][w+b] = aux

            b+=1
            a+=1
            
    return m

       
def login():

    email = input("Ingrese su email de la uem:")
    correo = email

    contrasenia = (input("Ingrese su numero de expediente:"))
    expedienteContrasenia = int(contrasenia)

    if(expedienteContrasenia != expediente):

        print("Email o Expediente incorrecto. . .")

    else: menu()


def menu():

    print("\n******************** UNIVERSIDAD EUROPEA DE MADRID *************************\n"
         + ( "Escuela de Ingenieria Arquitectura y Diseno\n\n"))

    print("*****************MENU**********************\n"
          "A: Ejercicio A\n"
          "B: Ejercicio B\n"
          "C: Ejercicio C\n"
          "D: Ejercicio D\n")

    print("\nDaniel Sabbagh Pastor\n")

    op = input("Elija una op:")
    
    if op == "A" or op=="a":

        print("\n__________EJERCICIO A__________")

        list1 = [2,1,6,5,3]
        list2 = [4,0,8,7]
        listV = Ej_A_Ordenar(list1, list2)

        Ej_A_Mediana(listV)

        print("__________\n")

        menu()
    elif op == "B" or op =="b":

       print("Proximamente. . .\n")

        menu()

    elif op == "C" or op =="c":

        print("\n__________EJERCICIO C__________")

        m=[[5,9],[2,1]]
        print("Matriz: ",m)

        matriz = Ej_C_Trasponer(m, 0, len(m)-1, 0, len(m)-1)

        print("Traspuesta: ",matriz)
        print("__________\n")

        menu()
    elif op == "D" or op =="d":

       print("Proximamente. . .")

       menu()


login()




