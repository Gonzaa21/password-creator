import random as rnd
import string as str

import save as save
import security as scr
import language as lang

def PasswordGenerator():
    while True:
        # Type of characters
        caracteres = str.ascii_letters + str.digits + str.punctuation
        try:
            # Length
            longitud = int(input(lang.Translate('length')))
            
            # Verify if the password is more than 8 char.
            if longitud < 8:
                print(lang.Translate('length_error'))
                continue
            
            # Generate and randomize depending the length
            contraseña = rnd.choices(caracteres, k=longitud)
            rnd.shuffle(contraseña)
            contraseña = ''.join(contraseña)  # Convert to str
            
            return contraseña
        except ValueError:
            print(lang.Translate('invalid_char'))

# Call functions
lang.Language()
longitud = input(">> ")

contraseña = PasswordGenerator()
print(lang.Translate('created', contraseña=contraseña))
save.SavePassword(contraseña)
scr.SecurityPassword(contraseña)

#encriptar las contraseñas usando cryptography module
