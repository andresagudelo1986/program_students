import json
import time
#function para numero entero parametros. c = edad minima. d=edad maxima+1. mesage=el mensaje que desee
#retorna numero entero dentro del rango c-d

def num_int (c,d,mesage):                      # this funtion return int  
    while True:                                # the loop repeat until complete 
        a=(input(mesage))  
        try:                                   #manejo de los herrores _error handling                        
                                            
            b=int(a) 
            if b in range(c,d):                #question is in range?- esta en el rango
                return int(a)
                break
            else:
                print("~" * 50)                              #control range- por fuera del rango
                print(f"La seleccion debe ser >= a '{c}' y >= '{d - 1}'")
                print("~" * 50)
        except ValueError:                     # error control-
            if a.isalpha() or a.count(' ')> 0 :                #is alpha o it have spaces-- es letra o tiene espacios
                print("~" * 50)
                print("\nERROR \nIngresa un numero\n")
                print("~" * 50)
            elif a.count('.')== 1 and a[0].isnumeric():        # is float chain?-- es cadena decimal?
                e = float(eval(a))                             # this made str a operable fact
                f = int(eval(a))                               # hace una cadena operable matemati..
                resta = lambda x,y:x-y                         # to rest
                g= resta(e,f)                                  # call to lambda
                if g == 0.0:                                   #is int with float
                    return (int(f))
                    break
                else:
                    print("~" * 50)
                    print (f"\n {a} : no es numero entero \n ")   
                    print("~" * 50)
#*************************************************************************************************
# funcion para pedir nombre recibe una sola palabra.parametros solo el mensaje como quieras pedir el nombre
#retorna nombre

def name(men):
    while True:
        a=input(men)
                                              # filtro los datos en el strin "a"
        if list(filter(lambda e : e.isalpha(),a)) and not list(filter(lambda e : e.isnumeric(),a)) and a.count(' ')==0:
            return a
            break
        else:                                 # si no se dan los requisitos en el if no es lo que requiero dentra en el else
            print("~" * 50)
            print("por favor ingrese un dato valido")
            print('~' * 50)
#*************************************************************************************************
# funcion ingresa nota no tiene parametros

def num_note ():
    while True:
        try:
            numero = float(input("por favor ingresa la nota del estudiante de 0.0 a 5.0: "))
            
            if numero >= 0.0 and numero <= 5.0:   # rango de la nota
                return numero
                break
            
            else:
                 print("~" * 50)
                 print("El rango es de 0 a 5")
                 print("~" * 50)
        
        except ValueError:
                print("~" * 50)
                print("\nPor favor ingrese un dato valido\n")
                print("~" * 50)
        
        except TypeError:
             print("~" * 50)
             print ("\npor favor la nota debe de estar en un rango de 0.0 a 5.0:\n")
             print("~" * 50)
#*************************************************************************************************                
#funcion para pedir carrera no tiene parametros retorna el strin de la carrera

def carrers ():
    while True:
        try:
            print("~" * 50)
            a =int( input("Selecione el programa: \n\n1. Ingeniería de Productividad y Calidad.\n2. Ingeniería Agropecuaria.\n3. Ingeniería civil.\n4. Ingeniería en Seguridad y Salud en el Trabajo.\n5. Ingeniería en Automatización y Control.\n6. Ingeniería Informatica. \n"))
            if isinstance(a,int) and a <=6 and a>=1:
                if a == 1:
                    return "Ingeniería de Productividad y Calidad."
                elif a == 2:
                    return "Ingeniería Agropecuaria."
                elif a == 3:
                    return "Ingeniería civil."
                elif a == 4:
                    return "Ingeniería en Seguridad y Salud en el Trabajo."
                elif a == 5:
                    return "Ingeniería en Automatización y Control."
                elif a == 6:
                    return "Ingeniería Informatica."
                
            
            else:
                print("~" * 50)
                print("Recuerde que las opcion son de 1 a 6")
                print("~" * 50)
            
        except ValueError:
            print("~" * 50)
            print("Por favor ingrese un dato valido")
            print("~" * 50)
#************************************************************************************************* 
#funcion menu sin parametros retorna el numero de la opcion selecionada usa la funcion num_int 

def menu ():
    while True:
            print('~' * 50)
            print('MENU')
            print('~' * 50)
            print('Seleccione una opción')
            print('~' * 50)
            print("1. Registrar estudiante. ")
            print("2. Consultar estudiante de una carrera. ")
            print("3. Calcular promedio general.  ")
            print("4. Ver estudiantes destacados. ")
            print("5. Salir")
            a = num_int(1,6,"Seleccione: ")
            return a
#*************************************************************************************************    
#funcion registar estudiantes sin parametros. pero usa todas las funciones del scrip funciones_snake.py
#retorna un diccionario con los datos del ultimo estudiante agregado 
# esta funcion es la que usa import json homologa de pickle para serializar los datos
def register_stu():
    
    try:
        with open('bases_de_datos.json', 'r') as archivo:
            base_datos = json.load(archivo)
    except FileNotFoundError: 
        base_datos = {"nombres" : [],
                      "edad":[],
                      "carrera":[],
                      "promedio":[] }
    
    base_datos["nombres"].append(name ("Por favor ingrese el nombre del estudiante: "))  
    
    base_datos["edad"].append(num_int(8,101,"Ingrese la edad del estudiante: "))

    base_datos["carrera"].append(carrers())

    base_datos["promedio"].append(num_note())
    
    #abrir un archivo binario en modo escritura
    with open('bases_de_datos.json', 'w') as archivo:
        json.dump(base_datos, archivo)
        
    print(base_datos)
#*************************************************************************************************
# esta funcion es el menu principal y para todas sus funciones
def main_menu():
    import time
    a=1
    while (a):
        a = menu()
        if a ==1:               #registrar estudiante
            register_stu()
        elif a==2:
            choose = carrers()
            print (choose)
        elif a==3:
            pass
        elif a==4:
            pass

        else:
            print("Gracias hasta pronto")
            a=0
# inicio de pruebas de las funciones


if __name__ == '__main__':       #entry point sirve para que se ejecute las pruebas de las funciones
                                 # solo en el scrip donde este la funcion
    #prueba para edad
    num_int(8,101,"Ingrese la edad del estudiante: ")

    #prueba para ingresar datos register_stu
    a=register_stu()
    print(a)
    
    #prueba para funcion del nombre
    nombre = name("por favor ingrese un nombre de una sola palabra: ")
    print(nombre)

    #prueba para ingresar nota
    calificacion = num_note ()
    print(calificacion)    

    #prueba para la funcion carrers
    carrera=carrers()
    print(carrera)

    #prueba para la funcion menu
    n = menu()
    print(n)
