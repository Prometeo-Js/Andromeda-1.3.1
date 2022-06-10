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
#Sera vienbenida toda ayuda posible 
print('/////////////////////////')
print("Version 1.3")
print("MADE BY PROMETEO-CYBER")
print("GNU GENERAL PUBLIC LICENSE VERSION 2 SUPPORTS THIS SCRIPT")
print('/////////////////////////')
while True:
    print('Menu')
    print('[1]ip port scan')
    print('[2]Network scan by PING')
    print('[3]Exit')
    opcion = int(input('Enter one of the options:'))
    if opcion == 1:
        ip = input('[+]Enter a target IP address:')
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
        print("PingEscaner:Scan for devices")
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
                    print ("Total of active devices: " + str(cont))
    elif opcion ==3:
        print("Closing Tools")      
        break
    else:
        print("No options exist")
        break 