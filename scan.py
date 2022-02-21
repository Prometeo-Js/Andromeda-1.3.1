#!/usr/bin/python3
import nmap
from subprocess import *
print("""
   ▄████████ ███▄▄▄▄   ████████▄     ▄████████  ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄████████ ████████▄     ▄████████
  ███    ███ ███▀▀▀██▄ ███   ▀███   ███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███   ▀███   ███    ███
  ███    ███ ███   ███ ███    ███   ███    ███ ███    ███ ███   ███   ███   ███    █▀  ███    ███   ███    ███
  ███    ███ ███   ███ ███    ███  ▄███▄▄▄▄██▀ ███    ███ ███   ███   ███  ▄███▄▄▄     ███    ███   ███    ███
▀███████████ ███   ███ ███    ███ ▀▀███▀▀▀▀▀   ███    ███ ███   ███   ███ ▀▀███▀▀▀     ███    ███ ▀███████████
  ███    ███ ███   ███ ███    ███ ▀███████████ ███    ███ ███   ███   ███   ███    █▄  ███    ███   ███    ███
  ███    ███ ███   ███ ███   ▄███   ███    ███ ███    ███ ███   ███   ███   ███    ███ ███   ▄███   ███    ███
  ███    █▀   ▀█   █▀  ████████▀    ███    ███  ▀██████▀   ▀█   ███   █▀    ██████████ ████████▀    ███    █▀
                                    ███    ███
""")
#INICIO DE CODIGO
print('/////////////////////////')
print("Version 1.1")
print("ECHO POR PROMETEO-CYBER")
print('/////////////////////////')
while True:
    print('Menu')
    print('[1]Escaneo de puertos de ip')
    print('[2]Escaneo de red mediante PING')
    print('[3]Salir')
    opcion = int(input('Ingrese una de las opciones:'))
    if opcion == 1:
        ip = input('[+]Introduce direccion IP objetivo: ')
        nm = nmap.PortScanner()
        puertos_abiertos = "-p"
        count = 0
        results = nm.scan(hosts=ip, arguments="-sT -n -Pn -T4")
        print("\nHost :  %s" % ip)
        print("State : %s" % nm[ip].state())
        for proto in nm[ip].all_protocols():
            print('Protocol : %s' % proto)
            lport = nm[ip][proto].keys()
            sorted(lport)
            for port in lport:
                print('port : %s\tstate : %s' %
                    (port, nm[ip][proto][port]['state']))
                if count == 0:
                    puertos_abiertos = puertos_abiertos + " " + str(port)
                    count = 1
                else:
                    puertos_abiertos = puertos_abiertos + "," + str(port)
        print("\nPuertos abiertos:"+puertos_abiertos+" "+(ip))
    elif opcion == 2:
        cont=0
        print("PingEscaner:Buscando dispositivos")
        print("")
        for ip in range(1, 255):
            print(ip)
            ip_address= f'192.168.1.{ip}'
            print(ip_address)
            proc=Popen(["/usr/bin/ping -c 1 %s " % ip_address, ''], stdout=PIPE, shell=True)
            (stdout,stderr)=proc.communicate()
            if "bytes from" in stdout.decode():
                cont +=1
                print (" | "+str(cont)+"|%s|IP ACTIVA|" %(stdout.decode().split()[1]))
                with open("ips.txt","a")as myfile:
                    myfile.write(stdout.decode().split()[1]+'\n')
                    print ("Total De Dispositivos Activos: " + str(cont))
    elif opcion ==3:
        print("Apagando sistemas")
        break
    else:
        print("Ninguna opcion existe")
        break 