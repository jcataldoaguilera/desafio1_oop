# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-05
# RLAB-23-02-09-0044-2
#

# Librerias
from pizza import Pizza

# Usar la función print(), para que al ejecutar el script se muestre en pantalla los
# valores de los atributos de clase de la clase importada, sin crear una instancia
# de ella.
print(Pizza.size, Pizza.price)

# Usar la función print(), para que al ejecutar el script se muestre en pantalla
# si el elemento “salsa de tomate” se encuentra presente en la lista [“salsa de
# tomate", "salsa bbq"]. Para ello use el método creado en el requerimiento
# 2, sin crear una instancia de la clase importada.
print(Pizza.validate("salsa de tomate",["salsa de tomate", "salsa bbq"]))

# Crear una instancia de la clase importada, y luego llamar al método del
# requerimiento 3, para que al ejecutar el script se solicite ingredientes y tipo de
# masa al usuario.
pizza1 = Pizza()
pizza1.pedido()

# Usar la función print(), para que al ejecutar el script, luego de que el usuario
# haya ingresado los ingredientes y tipo de masa, se muestre en pantalla los
# ingredientes vegetales, el ingrediente proteico y el tipo de masa de la instancia
# creada en el paso anterior, y si esa instancia es una pizza válida o no.
print(pizza1.vegetales, pizza1.carne, pizza1.masa)
print(pizza1.pizza_valida)

# Usar la función print(), para mostrar en pantalla si la clase Pizza es una pizza
# válida o no, haciendo uso del atributo creado en el requerimiento 4, sin crear
# una instancia de la clase. En este punto, la ejecución del script debe mostrar
# un error (todos los pasos anteriores se deben haber ejecutado correctamente).
print(Pizza.pizza_valida)
