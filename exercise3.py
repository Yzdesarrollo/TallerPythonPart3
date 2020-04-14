
# Algoritmos

# Promedio edad
# n = 0
# edad = 0
# contPers =0
# acumEdad = 0
# continuar = 1

# while (continuar != 0):
#     edad = int(input("Ingrese la edad: "))    
#     contPers+=1
#     acumEdad += edad

#     if (edad > 18):
#         contPers = contPers - 1 
#         acumEdad = acumEdad - edad
#         continuar = int(input("Escriba 0 para terminar o 1 para seguir: "))
#     else:
#         continuar = 1

# print("Promedio de edad: " + str(acumEdad/contPers))

# Suma de diez cantidades

# acum = 0
# n = 0

# for i in range(0,10):
#     n = int(input("Ingrese el número: "))
#     acum = acum + n 
#     print("La suma del 1 al 10 es: "+ str(acum))

# Estatura promedio de un numero de personas

# est = 1.0
# acumEst = 0
# contPers =0

# while (est != 0): 
#         est = float(input("Ingrese la estatura en metros o 0 para terminar: "))
#         if (est==0):
#             contPers-=1
        
#         contPers+=1
#         acumEst += est
    
# print("Promedio de estatura: " + str(acumEst/contPers))

# N cantidades <= 0 y >= 0

# num = ""
# countMj=0
# countMn=0

# while (num != "*"): 
#     num = int(input("Ingrese el numero o ' * ' para terminar: "))
#     if (num<=0):
#         countMn+=1
#     elif(num>0):
#         countMj+=1
    
# print("Cantidad de numeros menores o iguales a cero: " +countMn +"\n" + "Cantidad de numeros mayores a cero: " + countMj)

# Numeros pares e impares entre 0 y 100

# par = []
# impar = []

# for i in range(0,100):
#     if (i % 2 == 0):
#         par.append(i)
#     else:
#         impar.append(i)
# print("Los números pares son : " + str(par))
# print("Los números impares son: "+ str(impar))

# Fibonnacci
# 0+1= 1
# 1+1=2
# 1+2=3
# 2+3=5
# 3+5=8

# n = int(input("¿Cuántos números de Fibonacci quiere generar? : "))
# array = [] #sucesion de números entrero en orden: 0, 1, 2...

# for i in range (0,n):
#     if(i==0):
#         array.append(0)
#     elif(i==1):
#         array.append(1)
#     else:
#         array.append(array[i-1]+array[i-2])
# print(array)
