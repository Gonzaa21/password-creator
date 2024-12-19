import os
import language as lang

def SavePassword(contraseña):
    while True:
        guardar = input(lang.Translate('prompt_save')).lower()
        if guardar == 's' or 'y':
            # Crear carpeta saves si no existe
            os.makedirs('saves', exist_ok=True)
            
            # Guardar la contraseña
            with open('saves/passwords.txt', 'a', encoding='UTF-8') as passwords:
                passwords.write(lang.Translate(f'password_txt', contraseña=contraseña))
            
            print(lang.Translate('password_save'))
            break
        elif guardar == 'n':
            print(lang.Translate('password_not_save'))
            break
        else:
            print(lang.Translate('password_invalid'))