# Declarar una variable de tipo entero y mostrar su valor.
sueldo= 5000
print(sueldo)

# Declarar una variable de tipo cadena y mostrar su valor.
nombre='Pedro'
print(nombre)

# Concatenar dos cadenas.

nombre= 'Pedro'
Apellido='Garcia'

print(Apellido  + ' ' +  nombre )

# Mostrar el tipo de una variable.
sueldo=5000
print(type(sueldo))

# Operaciones básicas con enteros (suma, resta, multiplicación, división).
a= 15
b=6

suma= a + b
resta= a-b
multiplicacion= a*b
division= a/b

print(suma, resta , multiplicacion , division )

# Operaciones con números flotantes.

precio= 15.50
precio2= 21.35
cantidad=5


suma=precio + precio2
resta=precio2-precio
multiplicacion=precio*cantidad
dividir=multiplicacion/precio

print (suma, resta, multiplicacion, dividir)

# Conversiones entre tipos de datos (de cadena a entero, etc.).

edad='25'

print((int(edad)))


# Capturar un número entero desde el usuario y mostrarlo.

edad=int(input("ingresa tu edad: "))


print(edad)

# Capturar una cadena desde el usuario y mostrarla.

nombre=input("ingresa tu nombre: ")


print(nombre)


# Usar la función len() para contar los caracteres de una cadena.
ciudad='Buenos Aires'

print(len(ciudad))



# Realizar una operación matemática con números capturados por el usuario.
precio=float(input('ingrese el precio del producto: '))
cantidad=float(input('ingrese la cantidad de productos: '))

total_compra= precio * cantidad

print('el total de la compra es:', total_compra)



# Suma de tres números introducidos por el usuario.

numero1=int(input('Ingrese numero 1:' ))
numero2=int(input('Ingrese numero 2:' ))
numero3=int(input('Ingrese numero 3:' ))

suma= numero1+numero2+numero3

print(suma)

# Mostrar el valor de una expresión matemática (ej., 2+3*4).

expresion= 2*3+5+3/5

print(expresion)

# Mostrar el resultado de dividir dos números (como flotante y entero).

numero= 43
numero2=13.8

division= numero/numero2

print(division)

# Uso de operadores lógicos: and, or, not.

# a y b  son verdaderos la respuetsa es verdadera si uno de los es falso la respuesta es falsa
# a o b si uno de los dos es verdadero la respuesta es verdadera, si ambos falson la respuesta es falsa
# si a o b son negado, la respuesta es el contrario 

numero1= 4
Numero2= 16
numero3= 5

if  (numero1 and Numero2)== numero3:
    print('V')
else:
    print('F')

if numero1> numero3 or Numero2 >numero3:
    print('V')
else:
    print('F')


if   not numero1 < numero3 :
    print('V')
else:
    print('F') 

# Crear un programa que determine si un número es par o impar.

numero =5
numero2=4

if numero % 2 == 0:  # % significa modulo de un numero 
    print('es par')
else:
    print('impar')

if numero2 % 2 == 0:
    print('es par')
else:
    print('impar') 




# Convertir una cadena de texto a minúsculas y a mayúsculas.
ciudad= "monterrey"
pais='ESPAÑA'
pais2= pais.lower()
ciudad2=ciudad.upper()

print(ciudad)
print(ciudad2)
print(pais)
print(pais2)

# Buscar un valor dentro de una lista y mostrar su índice.

# listas: son conjuntos de elementos que van agrupados []
  #          0          1          2      3
mercado=['tomate','cebolla','lechuga','papa']

print(mercado)
print(mercado[0])

# Crear una lista con varios tipos de datos y mostrarlos.

conjunto=[34, 'casa', 14.5 , False]

print(conjunto)
print(conjunto[2])


# Acceder a elementos de una lista utilizando índices.

conjunto=[34, 'casa', 14.5 , False]

print('El indice 1 de la lista es:',  conjunto[1])