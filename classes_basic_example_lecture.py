# Pedro Concejero for UTAD Programming for Animation
# https://www.u-tad.com/lds/grado-animacion/
# 2020/03/19

"""
Ejemplo básico de programación por clases y de estructura básica de script python
"""

# A continuación orden de Imports
# Parece ser que no hay estándar, buena fuente esta:
# https://medium.com/@rukavina.andrei/how-to-write-a-python-script-header-51d3cec13731

# Futures
from __future__ import print_function

# Built-in/Generic Imports
import os
import sys

# Libs
import datetime as dt

# Own modules
# from {path} import {class}

# Algunos datos básicos (totalmente opcional)

__author__ = '{Pedro Concejero}'
__email__ = '{pedro.concejero@u-tad.com}'
__copyright__ = 'Copyright {year}, {project_name}'
__credits__ = '{credit_list}'
__license__ = '{license}'
__version__ = '{mayor}.{minor}.{rel}'
__maintainer__ = '{maintainer}'
__status__ = '{dev_status}'

# A continuación ejemplos muy básicos de clases
# Tomados de aquí:
# https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/

### Creemos una clase vacía para ver qué la sintaxis básica
# Ojo a las reglas (recomendaciones) de nombres
# Y ojo también a que python es siempre sensible (diferencia) may. de minúsculas.

class MiClaseDeEjemplo:
    pass

MiClaseDeEjemplo

# Ahora la podemos instanciar

esto_es_otro_objeto = MiClaseDeEjemplo()

print(esto_es_otro_objeto)

# Las clases incluyen atributos 

class MiClaseDeEjemplo02:
    name = 'Pedro Concejero'  # se define atributo name de la clase

# La clase la instanciamos entonces y la asignamos por ejemplo a una variable

primer_ejemplo = MiClaseDeEjemplo02()

print(MiClaseDeEjemplo02.name)

### Métodos

# Una vez que hay atributos que "pertenecen" a la clase
# se pueden definir funciones que accederán a dichos atributos.
# Estas funciones se llaman métodos y a partir de ese momento
# se podrán acceder utilizando la conocida sintaxis clase.metodo(parametros)
# PERO
# Ahora debes proporcionar un primer argumento al método con la
# keyword 'self'

# For example, you can define a class Snake, 
# which has one attribute name and one method change_name. 
# The method change name will take in an argument new_name along with the keyword self.

class MiClaseDeEjemplo03:
    name = 'Pedro Concejero'  # se define atributo name de la clase
    
    def change_name(self, new_name): # note that the first argument is self
        self.name = new_name # access the class attribute with the self keyword


# Now, you can instantiate this class Snake with a variable snake 
# and then change the name with the method change_name.

# instantiate the class
nombre = MiClaseDeEjemplo03()

# print the current object name 
print(nombre.name)

# change the name using the change_name method
nombre.change_name("pon_aqui_tu_nombre")
print(nombre.name)


### Instance attributes in python and the init method

# You can also provide the values for the attributes at runtime. 
# This is done by defining the attributes inside the init method. 
# The following example illustrates this.

class MiClaseDeEjemplo04:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

# Now you can directly define separate attribute values for separate objects. 
# For example,

# two variables are instantiated
yo = MiClaseDeEjemplo04("Pedro Concejero Cerezo")
mi_abuelo = MiClaseDeEjemplo04("Pedro Concejero Caballero")

# print the names of the two variables
print(yo.name)

print(mi_abuelo.name)

