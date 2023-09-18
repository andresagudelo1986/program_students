import fun_student
from fun_student import name
from fun_student import num_int
from fun_student import carrers
from fun_student import num_note
from fun_student import menu
from fun_student import register_stu
from fun_student import main_menu

import json
import time

print()
print()

with open('bases_de_datos.json', 'r') as archivo:
            base_datos = json.load(archivo)
"""
Este es un programa que cumple con los requisitos minimos para que un docente ingrese los datos
de los estudiantes y retorne lo esperado en este programa se puede almacenar los datos como nombre 
las notas el promedio primer.
"""

main_menu()





