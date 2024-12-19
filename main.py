import random as rnd
import string as str

import save as save
import security as scr
import language as lang

def PasswordGenerator():
    while True:
        # Tipos de caracteres a usar
        caracteres = str.ascii_letters + str.digits + str.punctuation
        try:
            # Pedir la longitud de caracteres
            longitud = int(input(lang.Translate('length')))
            
            # Validar que la cantidad de caracteres sea al menos 8
            if longitud < 8:
                print(lang.Translate('length_error'))
                continue
            
            # Generar y aleatorizar los caracteres según la longitud
            contraseña = rnd.choices(caracteres, k=longitud)
            rnd.shuffle(contraseña)
            contraseña = ''.join(contraseña)  # Convertir a string
            
            return contraseña
        except ValueError:
            print(lang.Translate('invalid_char'))

# Llamada a las funciones
lang.Language()
longitud = input(">> ")

contraseña = PasswordGenerator()
print(lang.Translate('created', contraseña=contraseña))
save.SavePassword(contraseña)
scr.SecurityPassword(contraseña)

#encriptar las contraseñas usando cryptography module
