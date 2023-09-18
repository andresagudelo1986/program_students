import time
import json
with open('bases_de_datos.json', 'r') as archivo:
            base_datos = json.load(archivo)
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
        lista = ["Ingeniería de Productividad y Calidad.","Ingeniería Agropecuaria.","Ingeniería civil.",
                 "Ingeniería en Seguridad y Salud en el Trabajo.","Ingeniería en Automatización y Control.","Ingeniería Informatica."]
        try:
            print("~" * 50)
            a =int( input( f"Selecione el programa: \n\n1. {lista[0]} \n2. {lista[1]} \n3. {lista[2]} \n4. {lista[3]} \n5. {lista[4]}  \n6. {lista[5]}  \n"))
            if isinstance(a,int) and a <=6 and a>=1:        # isinstance es una funcion que me retorna bool 
                                                            #si el parametro1, es del tipo que hay en el perametro dos
                print (lista[a-1])
                return lista[a-1]
                
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
            break
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
    with open('bases_de_datos.json', 'r') as archivo:
            base_datos = json.load(archivo)
    a = len(base_datos["nombres"])
    print("cargando datos....\n")
    time.sleep(3)
    print("....Base cargada\n")

    print (f"Hola se acaba de cargar una base de datos con {a} Estudiantes")
    
    time.sleep(3)
    a=1
    while (a):
        a = menu()
        if a ==1:               #registrar estudiante
            register_stu()
        elif a==2:
            find_carrer (carrers())

        elif a==3:
            media()
        elif a==4:
            destacados()
        else:
            print("Gracias hasta pronto")
            a=0
#*************************************************************************************************
#funcion para buscar los estudiantes de un acarrera
def find_carrer (ingenieria):
    with open('bases_de_datos.json', 'r') as archivo:
            base_datos = json.load(archivo)
    base_datos
    for i in range (len(base_datos["carrera"])):
        print('~' * 50)
        print(ingenieria)
        print('~' * 50)
        
        if ingenieria in base_datos.get("carrera"):

            indices = [indice for indice,ing in enumerate(base_datos["carrera"] )   if ing == ingenieria  ] # list comprehencion
            students_in = [base_datos["nombres"][i]   for i in indices]
            cant_estud=len(students_in)
            
            print("Los estudiantes son:\n")
            for i in range(cant_estud):
                print(f"--{students_in[i]}")
        else:
            print('~' * 50)
            print(f"{ingenieria}\n{'*' * 6}No se encontró en la lista")
        time.sleep(2)
        break
#*************************************************************************************************
#funcoin promedio general
def media():
    with open('bases_de_datos.json', 'r') as archivo:
            base_datos = json.load(archivo)
    media = sum(base_datos["promedio"])/len(base_datos["promedio"])
    print('~' * 50)
    print(f"La media en El Politecnico Colombiano\nJaime Isaza Cadavid es: {round(media,1)}")
    time.sleep(2)
#*************************************************************************************************
def destacados():
    with open('bases_de_datos.json', 'r') as archivo:
            base_datos = json.load(archivo)
    indices = [indice for indice,nota in enumerate(base_datos["promedio"] )   if nota >= 4  ]
    notas = [nota for indice,nota in enumerate(base_datos["promedio"] )   if nota >= 4  ]
    students_in = [base_datos["nombres"][i]   for i in indices]
    programa = [base_datos["carrera"][i]   for i in indices]
    cant_estud=len(students_in)
    for i in range (cant_estud):
         print(f"Nombre: {students_in[i]}     Nota:{notas[i]}     Programa:{programa[i]}\n")
    time.sleep(3)
#*************************************************************************************************
# inicio de pruebas de las funciones


if __name__ == '__main__':       #entry point sirve para que se ejecute las pruebas de las funciones
    #prueba
    main_menu()
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

