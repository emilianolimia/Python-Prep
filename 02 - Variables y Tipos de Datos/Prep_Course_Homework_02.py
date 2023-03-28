## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
mi_variable1 = 10
print(mi_variable1)

# 2) Imprimir el tipo de dato de la constante 8.5
mi_variable2 = 8.5
print(type(mi_variable2))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(mi_variable1))

# 4) Crear una variable que contenga tu nombre
mi_nombre = 'Emiliano'

# 5) Crear una variable que contenga un número complejo
num_complejo = 2 + 3j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(num_complejo))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
import math
num_pi = round(math.pi, 4)
print(num_pi)

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
mi_variable3 = True
mi_variable4 = False

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(mi_variable3))

# 10) Asignar a una variable, la suma de un número entero y otro decimal
suma = 10 + 10.25

# 11) Realizar una operación de suma de números complejos
a = 2 + 3j
b = 4 - 1j
resultado1 = a + b
print(resultado1)

# 12) Realizar una operación de suma de un número real y otro complejo
c = 2.5
d = 3 + 2j
resultado2 = c + d
print(resultado2)

# 13) Realizar una operación de multiplicación
producto = 5 * 3

# 14) Mostrar el resultado de elevar 2 a la octava potencia
potencia = 2**8
print(potencia)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27 / 4
print(cociente)

# 16) De la división anterior solamente mostrar la parte entera
cocienteEntero = 27 // 4
print(cocienteEntero)

# 17) De la división de 27 entre 4 mostrar solamente el resto
resto = 27 % 4
print(resto)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(cocienteEntero * 4 + resto)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print('Hello ' + 'world!')

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
a = '2'
b = 2
print(a == b)

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(int(a) == b)

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# Porque un número decimal en Python utiliza un punto como separador

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
numero = 3
numero -= 2
print(numero)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
# La representación binaria del número 1 es simplemente 1. 
# Al desplazarla dos posiciones hacia la izquierda, obtenemos 100, que es la representación binaria del número 4.

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido?
# ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# No, si fuesen enteros el resultado sería 4, y si fuesen strings el resultado sería 22.

# 26) Realizar una operación válida entre valores de tipo entero y string
cadena = "El resultado es: "
valor_entero = 42
resultado = cadena + str(valor_entero)