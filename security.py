import string as str
import language as lang

def SecurityPassword(contraseña):
    longitud = len(contraseña)
    mayus = any(c.isupper() for c in contraseña)
    minus = any(c.islower() for c in contraseña)
    int = any(c.isdigit() for c in contraseña)
    symbol = any(c in str.punctuation for c in contraseña)

    puntuacion = sum([mayus, minus, int, symbol])
    
    with open('saves/passwords.txt', 'a', encoding='UTF-8') as passwords:
        if longitud >= 12 and puntuacion == 4:
            return passwords.write(lang.Translate('indicator_strong'))
        elif longitud >= 8 and puntuacion >= 3:
            return passwords.write(lang.Translate('indicator_moderate'))
        else:
            return passwords.write(lang.Translate('indicator_weak'))