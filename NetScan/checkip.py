import socket, os
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