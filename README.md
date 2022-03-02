# Andromeda 1.2
Análisis de puertos automatizado de Andromeda 1.2

Usando andromeda scan con la ayuda de python y nmap ip asignado buscando puertos tcp y udp abiertos.

REQUISITOS PARA TENER ANDROMEDA:

Tener python en su versión 3

Tenga nmap instalado, de lo contrario, el script para instalar no funcionará

INSTALACIONES NECESARIAS SI NO LAS DISPONE:

sudo apt install nmap

pip install python-nmap (ESTO ES NECESARIO PARA HACER QUE EL SCRIPT FUNCIONE)

SISTEMAS PROBADOS:

UBUNTU 20.04 LTS EN FUNCIONAMIENTO
KALI LINUX 2022.4 EN FUNCIONAMIENTO
TERMUX NO FUNCIONA DE MOMENTO

EJECUCIÓN DEL SCRIPT:

python3 Andromeda.py

chmod +x Andromeda.py

./Andromeda.py (ESTO SE REALIZARÁ DESPUÉS DE DAR PERMISO CON CHMOD)

para esta versión se agregó el sistema de menús así como la opción de hacer escaneo de red local.
Otras cosas a tener en cuenta es que se espera que se le agreguen más modificaciones en el futuro para una mejor adaptación a la versión anterior de Andromeda que no tendrá soporte.