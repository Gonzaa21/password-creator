#crear seleccion de idioma

#Diccionario
traducciones = {
    "es": {
        "length":"Ingrese la cantidad de caracteres de la contraseña: ",
        "length_error":"Debe contener al menos ocho caracteres, vuelva a intentarlo.",
        "invalid_char":"Caracter inválido, vuelva a intentarlo.",
        "created":"Contraseña creada con éxito, por favor no la comparta: {contraseña}",
        "prompt_save":"¿Desea guardar su contraseña? (s/n): ",
        "password_txt":"Contraseña: {contraseña}\n",
        "password_save":'Contraseña guardada con éxito en "saves/passwords.txt".',
        "password_not_save":"Contraseña no guardada.",
        "password_invalid":"Respuesta inválida, vuelva a intentarlo.",
        "indicator_strong":"Indicador de Seguridad: Fuerte\n\n",
        "indicator_moderate":"Indicador de Seguridad: Moderado\n\n",
        "indicator_weak":"Indicador de Seguridad: Débil\n\n"
    },
    
    "en": {
        "length":"Enter the number of password characters: ",
        "length_error":"It must contain at least eight characters, please try again.",
        "invalid_char":"Invalid character, please try again.",
        "created":"Password successfully created, please do not share: {contraseña}",
        "prompt_save":"Do you want to save your password? (y/n): ",
        "password_txt":"Password: {contraseña}\n",
        "password_save":'Password successfully saved in "saves/passwords.txt".',
        "password_not_save":"Password not saved.",
        "password_invalid":"Invalid response, please try again.",
        "indicator_strong":"Safety Indicator: Strong\n\n",
        "indicator_moderate":"Safety Indicator: Moderate\n\n",
        "indicator_weak":"Safety Indicator: Weak\n\n"
    }
}

actual = 'es'

def Language():
    global actual
    print("Seleccione un idioma / Select a language:\n1. Español (es)\n2. English (en)")
    while True:
        opcion = input(">> ").strip()
        if opcion == "1":
            actual = 'es'
            print("Idioma cambiado a Español. Porfavor presione y envie cualquier tecla.")
            break
        elif opcion == "2":
            actual = 'en'
            print("Language changed to English. Please press and send any key.")
            break
        else:
            print('Opción inválida. / Invalid option. Please try again.')

def Translate(clave,**kwargs):
    mensaje = traducciones[actual].get(clave, clave)
    return mensaje.format(**kwargs)
