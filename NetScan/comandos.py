import os, nmap, lanscan

import tkinter as tk
from tkinter import ttk, scrolledtext
try:
    win = tk.Tk()
    win.title("NetScan")

    # Para que la gente no pueda amplizr la ventana
    #win.resizable(0, 0)

    #aLabel = ttk.Label(win, text="NetScan Label")
    #aLabel.grid(column=0, row=0)

    #Boton y funcion de click

    def click():
        action.configure(text="Bienvenido " + numberChosen.get() + "" + name.get())
    ##Añadiendo el boton
    action = ttk.Button(win, text="Enter", command=click)
    action.grid(column=1, row=2)

    #Funcion para desabilitar el widget
    #action.configure(state="disabled")

    ttk.Label(win, text="Elige un numero: ").grid(column=1, row=0)
    number = tk.StringVar()
    numberChosen = ttk.Combobox(win, width=12, textvariable=number)
    numberChosen['values'] = (1, 2, 4, 42, 400)
    numberChosen.grid(column=1, row=1)
    numberChosen.current(0)

    ttk.Label(win, text="Escribe tu nombre: ").grid(column=0, row=0)
    name = tk.StringVar()
    nameEntered = ttk.Entry(win, width=12, textvariable=name)
    nameEntered.focus()
    nameEntered.grid(column=0, row=1)

    chVarDis = tk.IntVar()
    check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state="disabled")
    check1.select()
    check1.grid(column=0, row=4, sticky=tk.W)

    chVarUn = tk.IntVar()
    check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
    check2.deselect()
    check2.grid(column=1, row=4, sticky=tk.W)

    chVarEn = tk.IntVar()
    check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
    check3.select()
    check3.grid(column=2, row=4, sticky=tk.W)

    color1="Blue"
    color2="Gold"
    color3="Red"

    def radCall():
        radSel=radVar.get()
        if radSel == 1 :
            win.configure(background=color1)
        elif radSel == 2:
            win.configure(background=color2)
        elif radSel == 3:
            win.configure(background=color3)

    radVar = tk.IntVar()
    rad1 = tk.Radiobutton(win, text=color1, variable=radVar, value=1, command=radCall)
    rad1.grid(column=0, row=5, sticky=tk.W)

    rad2 = tk.Radiobutton(win, text=color2, variable=radVar, value=2, command=radCall)
    rad2.grid(column=1, row=5, sticky=tk.W)

    rad3 = tk.Radiobutton(win, text=color3, variable=radVar, value=3, command=radCall)
    rad3.grid(column=2, row=5, sticky=tk.W)

    scrolW = 50
    scrolH = 3

    scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
    scr.grid(column=0, columnspan=3)

    win.mainloop()
except KeyboardInterrupt:
    print("")
    print("El programa se va a cerrar")
    print("")


#######################################################################
########COMIENZO DE PRUEBA CON QtCREATOR###############################
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import (QFont, QIcon)

class ejemplo(QWidget):
    
    def __init__(self):
        super().__init__()
        self.icono()
        self.boton()

    def boton(self):
        ancho = 250
        alto = 150
        an = 250/2
        al = 150/2
        print (an)
        print (al)
        QToolTip.setFont(QFont('SansSerif', 20))
        #self.setToolTip('Esto es  <b>QWidget</b>.')
        btn = QPushButton('El boton', self)
        #btn.setToolTip('Esto es el widget del boton <b>QPushButton</b>')
        btn.resize(btn.sizeHint())
        btn.move(85, 63.5) 
        print(btn.sizeHint())   

        self.setGeometry(0, 50, ancho, alto)
        self.show()
    
    def icono(self):
        self.setWindowTitle('Icono')
        self.setWindowIcon(QIcon('netscan.jpg'))
    
        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ejemplo()
    app.exec_()
"""
#######FIN DE PRUEBA CON QtCREATOR#######################################
#########################################################################




###CON ESTA CONFIGURACION LA PARTE GRAFICA FUNCIONA#####
"""
app = QApplication(sys.argv)
button = QPushButton("Hello World", None)
#title = QWidget.setWindowTitle("NetScan")
icon = self.setWindowIcon(QtGui.QIcon("netscan,jpg"))
button.show()
icon.show()
#title.show()
app.exec_()
"""
####FIN DE PARTE GRAFICA##################################


## Importando archivos locales


#print("Hola, q tal?")
#print("Intentare ayudarte en lo que necesites para escanear la red")
#print("Selecciona la accion a realizar")


### COMPROBAR EL SO ####

#import platform
#platform.system()

### FIN COMPROBAR EL SO####


##### AQUI TIENE QUE IR UN MENU ######
#Enlace para el menu
#https://www.lawebdelprogramador.com/codigo/Python/2935-Ejemplo-de-implementar-un-menu-en-python-en-la-consola.html 






#### FIN MENU ########################


#### EJECUTAR COMANDO PARA VER LA MAC ####

#mac = os.system("cat /sys/class/net/enp8s0/address")
#mac ¡¡¡¡Esto se podria quitar!!!!

#### FIN DEL COMANDO VER LA MAC ####



###!!!NMAP SCAN WITH THE MACS¡¡¡###
# mac = os.system("nmap -sP -n 192.168.1.0/24")
# mac = os.system("nmap -PU 192.168.0.0/21") $$ Escaneo de toda la red. Con la info de la MAC
###!!!FIN NMAP SCAN WITH THE MACS¡¡¡###


##### ESCANEO RANGO DE IP #####
#rango = input("Ej: 192.168.1.0/24.   Rango de IP: " )

#print(rango) 


#nmScan = nmap.PortScanner()
#nmScan.scan()

#####FIN ESCANEO RANGO DE IP ######

#### START NMAP SCAN ####
'''
nm = nmap.PortScanner()
nm.scan('192.168.1.0', '22-443')

for host in nm.all_hosts():
     print('----------------------------------------------------')
     print('Host : %s (%s)' % (host, nm[host].hostname()))
     print('State : %s' % nm[host].state())
     for proto in nm[host].all_protocols():
         print('----------')
         print('Protocol : %s' % proto)
         lport = nm[host][proto].keys()
         lport.sort()
         for port in lport:
             print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
'''

# ----------------------------------------------------
# Host : 127.0.0.1 (localhost)
# State : up
# ----------
# Protocol : tcp
# port : 22   state : open
# port : 25   state : open
# port : 80   state : open
# port : 111  state : open
# port : 443  state : open

#### END NMAP SCAN ####