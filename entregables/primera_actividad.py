def addition(*args):
    return sum(args)

def multiplication(*args):
    value = 1
    for integer in args:
        value *= integer
    return value
    

"""
1) Lucia, tiene en su ropero cuatro vestidos y cinco conjuntos deportivos
¿De cuántas maneras puede vestirse?
"""
print(addition(4, 5))

"""
2) En un baile escolar la profesora forma parejas extrayendo de una bolsa
el nombre de un niño y de otra bolsa el nombre de la niña. Si en el aula
hay 9 niños y 7 niñas, ¿cuántas posibles parejas distintas se podrían formar?
"""
print(multiplication(7, 9))

"""
3) Veinte países mantienen relaciones diplomáticas, cada país tiene un embajador en los los
otros países. Indique la cantidad de embajadores que hay en total.
"""
print(multiplication(20, 20))

"""
4) ¿Cuántos números de 3 cifras existen? Donde el número no puede empezar con 0
"""

"""
5) En el estante de una biblioteca hay cinco libros de estadística y 
siete libros de matemáticas de autores diferentes. Si deseamos seleccionar un solo libro,
¿Cuántas opciones diferentes tenemos?
"""
print(addition(5, 7))

"""
6) En tres mercados de una ciudad se venden arroz por bulto; en el primer mercado
hay disponibles seis tiendas, en el segundo cuatro y el tercer mercado cinco.
¿De cuántas maneras puede realizarse la compra de un bulto de arroz?
"""
print(addition(6, 4, 5))