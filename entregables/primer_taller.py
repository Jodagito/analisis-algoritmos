import time
from matplotlib import pyplot as plt
from random import randint

"""
1) ¿De cuantos modos pueden ubicarse en una fila de 10 sillas a 4 personas?
"""
inicio = time.time()
sillas, personas = [10, 4]
posibles_puestos = 0
for persona in range(personas):
    posibles_puestos += sillas
print(f'Se pueden ubicar de {posibles_puestos} formas')
fin = time.time()
primer_tiempo = fin - inicio
print(f'El tiempo de ejecución fue de {primer_tiempo}\n')

"""
2) Entre Manizales y Armenia hay 3 carreteras ¿ De cuantos modos puede viajarse de Manizales a Armenia?
"""
inicio = time.time()
cantidad_rutas = 0
for ruta in range(3):
    cantidad_rutas += 1
print(f'Se puede viajar de {cantidad_rutas} distintas formas')
fin = time.time()
segundo_tiempo = fin - inicio
print(f'El tiempo de ejecución fue de {segundo_tiempo}\n')

"""
3) En tres mercados de una ciudad se vfinen arroz por bulto; 
en el primer mercado hay disponibles seis tifinas, en el segundo cuatro y en el tercer mercado cinco tifinas. 
¿De cuántas maneras puede realizarse la compra de un bulto de arroz?
"""
inicio = time.time()
primero = 6
segundo = 4
tercero = 3
posibles_compras_tifina = 0
posibles_compras_totales = 0
for tifina in range(primero):
    posibles_compras_tifina += segundo
for zapato in range(tercero):
    posibles_compras_totales += posibles_compras_tifina
print(
    f'La compra de un bulto de arroz se puede realizar de {posibles_compras_totales} distintas maneras')
fin = time.time()
tercer_tiempo = fin - inicio
print(f'El tiempo de ejecución fue de {tercer_tiempo}\n')

"""
4) Veinte países mantienen relaciones diplomáticas, cada país tiene un embajador en los otros países. Indique la cantidad de embajadores que hay en total.
"""
inicio = time.time()
paises = 20
embajadores = 0
total_embajadores = 0
for pais in range(paises):
    embajadores += 1
for pais in range(paises):
    total_embajadores += embajadores
print(f'En total hay {total_embajadores} embajadores')
fin = time.time()
cuarto_tiempo = fin - inicio
print(f'El tiempo de ejecución fue de {cuarto_tiempo}\n')

"""
5) Sofia trabaja en una tifina de ropa.
Se le ha asignado la tarea de vestir a un maniquí con una falda,
una blusa y un par de zapatos de una exposición de faldas,
blusas y zapatos que hacen juego.
Ya que todas las prfinas combinan,ella puede elegir cualquier blusa,
cualquier falda y cualquier par de zapatos y el atufino se verá bien.
Si hay 3 faldas, 5 blusas y 2 pares de zapatos, ¿De cuántas maneras distintas puede vestir al maniquí?
"""
inicio = time.time()
faldas = 3
blusas = 5
zapatos = 2
posibles_conjuntos = 0
posibles_conjuntos_blusas = 0
for falda in range(faldas):
    posibles_conjuntos_blusas += blusas
for zapato in range(zapatos):
    posibles_conjuntos += posibles_conjuntos_blusas
print(f'El maniquí se puede vestir de {posibles_conjuntos} maneras')
fin = time.time()
quinto_tiempo = fin - inicio
print(f'El tiempo de ejecución fue de {quinto_tiempo}\n')


"""
6) Un restaurante de fideos ofrece 5 tipos de fideos para elegir.
Cada plato viene con una de 4 carnes y una de 6 salsas diferentes a elección.
¿Cuántas combinaciones se pueden hacer?
"""
inicio = time.time()
tipos_fideos = 5
tipos_carnes = 4
tipos_salsas = 6
posibles_conjuntos_salsas = 0
posibles_conjuntos_fideos = 0
for tipo in range(tipos_fideos):
    posibles_conjuntos_salsas += tipos_carnes
for tipo in range(tipos_salsas):
    posibles_conjuntos_fideos += posibles_conjuntos_salsas
print(f'Pueden haber {posibles_conjuntos_fideos} combinaciones de fideos')
fin = time.time()
sexto_tiempo = fin - inicio
print(f'El tiempo de ejecución fue de {sexto_tiempo}\n')

# Grafico Primera Parte

x = range(1, 7)
y = [primer_tiempo, segundo_tiempo, tercer_tiempo, cuarto_tiempo, quinto_tiempo, sexto_tiempo]
plt.plot(x, y)
plt.title('Tiempos de Ejecución Parte I')
print('Para continuar con la segunda parte cierre el gráfico.\n')
plt.show()

# Segunda Parte

# 1) Crear un array números aleatorios. El tamaño del array lo debe de ingresar el usuario.


def generar_array(dimension_array, array=None):
    if not array:
        array = []
    if dimension_array:
        array.append(randint(0, 100))
        dimension_array -= 1
        return generar_array(dimension_array, array)
    print(f'El array generado fue {array}')

dimension_array = int(input('Ingrese la dimensión del array '))
inicio = time.time()
generar_array(dimension_array)
fin = time.time()
primer_tiempo_parte_dos = fin - inicio
print(f'El tiempo de ejecución fue de {primer_tiempo_parte_dos}\n')

# 2) Igual que el ejercicio anterior, pero meter en el array números aleatorios sin que se repitan.


def generar_array_sin_duplicados(dimension_array, array=None):
    if not array:
        array = []
    if dimension_array:
        numero_aleatorio = randint(0, 100)
        while numero_aleatorio in array:
            numero_aleatorio = randint(0, 100)
        array.append(numero_aleatorio)
        dimension_array -= 1
        return generar_array_sin_duplicados(dimension_array, array)
    print(f'El array generado fue {array}')


dimension_array = int(input('Ingrese la dimensión del array '))
inicio = time.time()
generar_array_sin_duplicados(dimension_array)
fin = time.time()
segundo_tiempo_parte_dos = fin - inicio
print(f'El tiempo de ejecución fue de {segundo_tiempo_parte_dos}\n')

# 3) Escribe una función recursiva que dado un número entero n, retorne un array con todos los números enteros en orden decreciente desde n a 1.


def generar_array_descendiente(dimension_array, array=None):
    if not array:
        array = []
    if dimension_array:
        array.append(dimension_array)
        dimension_array -= 1
        return generar_array_descendiente(dimension_array, array)
    print(f'El array generado fue {array}')


dimension_array = int(input('Ingrese la dimensión del array '))
inicio = time.time()
generar_array_descendiente(dimension_array)
fin = time.time()
tercer_tiempo_parte_dos = fin - inicio
print(f'El tiempo de ejecución fue de {tercer_tiempo_parte_dos}\n')

# 4) Escribir un programa que encuentre la suma de los enteros positivos pares desde N hasta 2. Comprobarque si N es impar se imprima un mensaje de error.

def calcular_suma(rango_numeros, acumulado=0):
    if rango_numeros >= 2:
        acumulado += rango_numeros
        rango_numeros -= 1
        return calcular_suma(rango_numeros, acumulado)
    print(f'La suma de los números en el rango dado da un total de {acumulado}')


rango_numeros = int(input('Ingrese el rango de números a sumar '))
inicio = time.time()
calcular_suma(rango_numeros)
fin = time.time()
cuarto_tiempo_parte_dos = fin - inicio
print(f'El tiempo de ejecución fue de {cuarto_tiempo_parte_dos}\n')


# Grafico Segunda Parte

x = range(1, 5)
y = [primer_tiempo_parte_dos, segundo_tiempo_parte_dos, tercer_tiempo_parte_dos, cuarto_tiempo_parte_dos]
plt.plot(x, y)
# Transforma el eje 'x' para que no muestre decimales
plt.xticks(x)
plt.title('Tiempos de Ejecución Parte II')
plt.show()
