import random as rd
print("""
 _______  ______    ___   _______  __    _ 
|       ||    _ |  |   | |       ||  |  | |
|   _   ||   | ||  |   | |   _   ||   |_| |
|  | |  ||   |_||_ |   | |  | |  ||       |
|  |_|  ||    __  ||   | |  |_|  ||  _    |
|       ||   |  | ||   | |       || | |   |
|_______||___|  |_||___| |_______||_|  |__|
""")
letras='abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ'
numeros='0123456789'
simbolos='|!"#$%&/()=?¿<>'

unidos=f'{letras}{numeros}{simbolos}'

contraseña=''.join(rd.sample(unidos,10))
print('Su contraseña es : ',contraseña)