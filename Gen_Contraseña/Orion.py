#!/usr/bin/python3
import random as rd

print("""
   ____         _               
  / __ \       (_)              
 | |  | | _ __  _   ___   _ __  
 | |  | || '__|| | / _ \ | '_ \ 
 | |__| || |   | || (_) || | | |
  \____/ |_|   |_| \___/ |_| |_|
  
""")
letras='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros='123456789'
simbolos='|!"#$%&/()=?¡¿<>'

unidos=f'{letras}{numeros}{simbolos}'

contraseña=''.join(rd.sample(unidos,10))
print(contraseña)