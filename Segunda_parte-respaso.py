# Sumar todos los elementos de una lista.
"""lista=[20,15,12,14]
print(sum(lista))"""

# Ordenar una lista de números de menor a mayor.
"""lista=['hielo','zorro','dedo', 'mesa', 'queso', 'arbol', 'torre' ]
Numeros_ordenados= sorted(lista)
print(Numeros_ordenados)"""

# Crear un programa que convierta un número de grados Celsius a Fahrenheit.
"""celsius= 40
Fahrenheit= (celsius *9/5)+32
print(Fahrenheit)"""

# Contar cuántas vocales hay en una cadena.
"""frase= ' el arbol tiene manzanas'
vocales='aeiouAEIOU'
contador=0

for letra in frase:
    if letra in vocales:    
        contador= contador + 1
print('el numero de vocales es:', contador )"""
  

# Comprobar si una palabra es un palíndromo (que se lee igual de atrás hacia adelante).

"""palabra='radar'
palindrono= palabra.lower().replace('','')
if palindrono == palindrono[::-1]:
   print('la palabra es un palindrono')
else:
     print('la palabra  no es un palindrono')"""

# Crear un programa que pida al usuario un número y muestre la tabla de multiplicar de ese número.
"""numero=int(input(" ingrese un nuemro del 1 al 9:"    ))
print('Tabla de multiplicar de el numero:', numero)
for i in range(1,11):
    print(numero, 'x', i , '=' , numero * i )"""


# Calcular la suma de los primeros 100 números naturales.
"""numeros_naturales= sum(range(1,101))
print(numeros_naturales)"""

# Verificar si una lista está vacía.
"""objetos= []

if objetos==[]:
    print('objetos es una lista vacia')
else:
    print('objetos no es una lista vacia')"""