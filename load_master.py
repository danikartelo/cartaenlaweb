#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Daniel Rodríguez García"
__copyright__ = "Copyright 2020, Caratenlaweb.com"
__credits__ = ["Daniel Rodríguez García"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Daniel Rodríguez García"
__email__ = ["info@cartaenlaweb.com","daniel.teleco@gmail.com"]
__status__ = "Production"


MASTER_FILE = "./master/master_page.txt"         #Fichero con el contenido de la pagina master,, en el futuro lo cargare de la BD

#-------------
import pandas as pd
class Section:
  def __init__(self, name):
    self.name = name
    self.text = '[vc_tta_section tab_id="' + self.name.lower()  +'" title="'+ self.name.capitalize() + '"]'
  def __str__(self):
    return self.text
#-------------

master_content = open(MASTER_FILE, "r").read()
# print(master_content)


x = master_content.find("dish")         # Buscar el elemento objetivo -- esto vale para acordeones, columnas, filas, pero no para elementos internos como imagenes, titulos, descripciones
#x = master_content.find("id=\"nombre\"")
#print(x)
y = master_content.rfind("[",0,x)       # Buscar el [ previo = inicio estructura
#print(y)
#print(master_content[y:y+100])
z = master_content.find(" ",y)          # Buscar tipo de estructrua
struct_type = master_content[y+1:z]     # La guardo en struct_type
a = master_content.find(("/" + struct_type),y)     # Buscar el fianl de la estructura
b = master_content.find("]",a)          # Buscarl el cierre
complete_struct = master_content[y:b+1] # Extraer la estructura entera

print(struct_type)
print(x)
print(y)
print(z)
print(a)
print(complete_struct)


#c = master_content.[y:b+1]find("photo",y)
c = master_content.find("photo",y)
d = master_content.rfind("image",0,c)
e = master_content.find(" ",d)
actual_image =  master_content[d:e]

master_content = master_content[:d] + "image=\"200\"" + master_content[e:]
print(c)
print(d)
print(e)
print(actual_image)
print(master_content[d:e])
print(master_content[y:b+1])




# Búsqueda dentro de photo -- buscar: image="198"
# Búsqueda dentro de nombre -- buscar: text="Papas"
# Búsqueda dentro de descripcion -- buscar: >con mojo rojo y mojo verde</p>
# Búsqueda dentro de alergenos -- pendiente
# Búsqueda dentro de precios -- buscar: text="4,51 €"

# Otra opcion e sponer una palabra clave, lo malo es que el master se queda medio raro, aunque pueden ser varias palabras o frases clave y en la imagen no es texto. un poco lio, casi mejor dejarlo así


#
