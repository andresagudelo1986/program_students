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
print(base_datos.items())


main_menu()




