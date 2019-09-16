import os, sys
from text_netscan import netscan
import files as files
# Variables

inserta = "Inserta un número: "
    

# Funciones del menu

def menu():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    netscan()
    print ("------------------------------------------------------------")
    print ("            SELECIONA LO QUE QUIERES DEL MENU               ") 
    print ("------------------------------------------------------------")
    print ("")
    print ("\t1 - IP o Rango de IP's a escanear")
    print ("\t2 - Mas Cosas")
    print ("\t3 - Ayuda")
    print ("\t9 - salir")
    print("")

def menu_ip():
    os.system('clear')
    netscan()
    print ("------------------------------------------------------------")
    print ("                 CONFIGURACIÓN DE NETSCAN                   ")
    print ("------------------------------------------------------------")
    print ("")
    print ("\t1 - Establecer una IP o Rango de IP's")
    print ("\t2 - Consultar la IP o Rango de IP's establecidos")
    print ("\t3 - Borrar las configuraciones de IP establecidas")
    print ("\t4 - Atrás")
    print ("\t9 - Salir")
    print ("")

def guardar():
    w = open ('cosas.txt','a')
    w.write(intro1+lista)
    w.write("\n")
    w.close()

def ver():
    r = open('cosas.txt','r')
    print (r.readline(30))
    print (r.readline(30))
    r.close()

def comprobar():
    
    f = open('cosas.txt', 'r')
    contenido = f.read()
    if contenido == '':
        print("")
        print("******* UPSSS no tines nada configurado, ponn 1 para configurar una IP y una mascara de Red *******")
        print("")
    else:
       ver()

def borrar():
    os.system("cat /dev/null > cosas.txt")

def pregunta_guardar():
    respuesta = input("¿Quieres guardar los archivos? Si/no: ").lower()
    #print (siono[respuesta])
    try:

        if files.siono[respuesta] == "si":
            guardar()
        elif files.siono[respuesta] == "no":
            print ("Vale, ")
            input ("Pulsa cualquier tecla para volver atrás")
        else:
            print ("Prueba con otras teclas")       
    except KeyError:
        print("No es correcto lo que as escrito pulsa cualquier tecla para repetir el script")
        pregunta_guardar()

def pregunta_borrar():
    respuesta = input("¿Quieres borrar los archivos? Si/no: ").lower()
    try:

        if files.siono[respuesta] == "si":
            borrar()
        elif files.siono[respuesta] == "no":
            print ("Vale, ")
            input ("Pulsa cualquier tecla para volver atrás")
        else:
            print ("Prueba con otras teclas")       
    except KeyError:
        print("No es correcto lo que as escrito pulsa cualquier tecla para repetir el script")
        pregunta_borrar()

# El while que ejecuta el menu
try:
    while True:
        # Mostramos el menu principal
        menu()

        opcionMenu = input(inserta)
     
        if opcionMenu=="1":
            while True:
                # Mostramos el menu cambio de IP
                menu_ip()

                opcionMenu_ip = input(inserta)

                if opcionMenu_ip=="1":
                    print("")
                    intro1 = input("Escribeme la IP: ")
                    intro2 = input("Escribeme la Mascara de Red: ")
                    lista = files.subConverter[intro2]
                    print("")
                    print("Tu IP es "+intro1 +" y la Mascara de Red es " + intro2)
                    print("")
                    ######Voy a cambiar la funcion del si o no#####
                    
                    pregunta_guardar()

                    #####Fin de lo que he añadido nuevo######

                    ####DE ESTA FORMA FUNCIONA TODO CORRECTAMENTE######
                    """
                    respuesta = input("Quieres guardar la configuración Si,no: ")
                    if respuesta == "Si":
                        guardar()
                    elif respuesta == "no":
                        input("Si quieres borrar la configuración...\npulsa una tecla")
                    else:
                        print("Por favor, introduce un Si o no")
                    """
                    #######FIN DE LA FORMA QUE FUNCIONABA BIEN #####
                    #mascara = print("nmap -sP -n "+intro1+lista)

                elif opcionMenu_ip=="2":
                    ####LO QUE FALTA POR HACER ES QUE CUANDO EL ARVICHO ESTE VACIO ENTONCES TE DIGA "que este esta vacio"######
                             
                    print ("")
                    print ("Esta es la lista de IP's que se va a escanear: ")
                    comprobar()
                    #ver()
                    input("Para volver pulsa una tecla ")

                    ######FIN DEL TODO FUNCIONA##########
                    
                elif opcionMenu_ip=="3":
                   # respuesta = input("Realmente quieres borrar las cosas Si,no: ")
                    
                    ###CAMBIO###

                    pregunta_borrar()

                    ###FIN DEL CAMBIO####

                    ###EN ESTE PUNTO FUNCIONA TODO####
                    """if respuesta == "Si":
                        borrar()
                        print ("La configuración de IP's para escanear esta vacia")
                    elif respuesta == "no":
                        input("Si quieres salir pulsa cualquier tecla")
                    else:
                        print("Por favor, introduce un Si o no")
                    """
                    ###FIN DEL PUNTO ###################
                    #input("Has pulsado la opción 3...\npulsa una tecla para continuar")
                
                elif opcionMenu_ip=="4":
                    break

                elif opcionMenu_ip=="9":
                    sys.exit()

                else:
                    print ("")
                    input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        elif opcionMenu=="2":
            print ("")
            input ("Has pulsado la opción 2...\npulsa una tecla para continuar")
        elif opcionMenu=="3":
            print ("")
            input ("Has pulsado la opción 3...\npulsa una tecla para continuar")
        elif opcionMenu=="9":
            break
        else:
            print ("")
            input ("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
except KeyboardInterrupt:
    print("")
    print("El programa se va a cerrar")
    print("")