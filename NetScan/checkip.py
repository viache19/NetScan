import socket, os
import subprocess
#-----------------Saber IP (falta la Mascara de Red)----------
#gw = os.popen("ip -4 route show default").read().split()
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#print(gw)
#print(s.connect((gw[2], 0)))
#ipaddr = s.getsockname()[0]
#gateway = gw[2]
#host = socket.gethostname()
#print ("IP:", ipaddr)
#------------------------Fin saber IP------------------
def ipa():
    ip = subprocess.check_output("ip addr show enp8s0 | grep 'enp8s0' | grep 'inet' | awk '{print $2}'", shell=True).rstrip()
    print("Tu direccion actual es: " + str(ip.decode("utf-8")))

ipa()