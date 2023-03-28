## Flujos de Control

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
num = 5
if (num < 0):
    print ('El número es menor a 0')
elif (num > 0):
    print ('El número es mayor a 0')
else:
    print ('El número es igual a 0')

#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
a = 5
b = 'Hola'
if (type(a) == type(b)):
    print ('Las variables son del mismo tipo')
else:
    print('Las variables son de distinto tipo')

#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for i in range(1, 21):
    if (i % 2 == 0):
        print('El número es par')
    else:
        print('El número es impar')

#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range(0, 6):
    print(i**3)

#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
num2 = 10
for i in range(0, num2):
    print(i)

#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
var = 4
if (type(var) == int):
    if (var > 0):
        factorial = var
        while (var > 2):
            var = var - 1
            factorial = factorial * var
        print(factorial)

#7) Crear un ciclo for dentro de un ciclo while
while (var > 0):
    for i in range(1, var):
        print(i)
    var = var - 1

#8) Crear un ciclo while dentro de un ciclo for
n = 5
for i in range(1, n):
    while(n < 5):
        n -= 1
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))

#9) Imprimir los números primos existentes entre 0 y 30
numMax = 30
numMin = 0
primo = True
while (numMin < numMax):
    for i in range(2, numMin):
        if (numMin % i == 0):
            primo = False
            break
    if (primo):
        print (numMin)
    else:
        primo = True
    numMin += 1

#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
# Ya está mejorado

#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
ciclos_sin_break = 0
n = 0
primo = True
while (n < numMax):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))

#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
#Obviamente....

#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
n = 99
while(n <= 300):
    n += 1
    if (n % 12 != 0):
        continue
    print(n, ' es divisible por 12')

#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
n = 1
sigue = 1
primo = True
while (sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        print('¿Desea encontrar el siguiente número primo?')
        if (input() != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1

#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
n = 100
while(n<=300):
    if (n % 6 == 0):
        print('El número es: ', str(n))
        break
    n += 1