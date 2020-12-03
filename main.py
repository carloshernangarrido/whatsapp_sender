import pywhatkit
from datetime import datetime as dt, timedelta
from functions import e164, close_tab, wait_seconds
import openpyxl as xl
import myexceptions as ex
import os


wellcome_message = """
********************************************************************************
********************* Whatsapp sender v0.0 *************************************
********************************************************************************
Hola!  (Developed by Hernán Garrido)
Este programa envía mensajes del archivo mess.xlsx usando Whatsapp Web y Chrome.
La primera columna debe contener números de teléfono, y la segunda el mensaje.
Si necesitás saltos de línea en el mensaje, usá Alt+Enter.

Asegurate de que todos los teléfonos tengan el 15 o el 9 (válido para Argentina).
Preferentemente que tengan el formato E164 (por ejemplo, para Mendoza: +5492615555222).
Todas las celdas tienen que tener formato 'texto'.

Vamos a mandar los mensajes de a poco... Nadie quiere ser baneado :-)
Ojo que no vamos a dejar de mandar hasta encontrar una celda en blanco!
Ahora, dejá la PC libre. Si tengo algún problema, te avisaré.
"""

print(wellcome_message)

try:
    path = os.getcwd()
    wb = xl.load_workbook(os.path.join(os.getcwd(), "mess.xlsx"))
except FileNotFoundError:
    print(ex.E2)
    exit(0)

list_with_issues = []
sheet_names = wb.sheetnames
sheet = wb[sheet_names[0]]
row = 1
number = str(sheet[f'a{row}'].value)
message = str(sheet[f'b{row}'].value)
first = True
while number:
    number_ok = e164(number)

    if not number_ok == -1:
        now_ = dt.now()
        print([number, number_ok, message])
        if first:
            send_at = now_ + timedelta(minutes=2)
            first = False
        else:
            send_at = now_ + timedelta(minutes=1)
        pywhatkit.sendwhatmsg(number_ok, message, send_at.hour, send_at.minute)
        wait_seconds(2)
        close_tab()
    else:
        list_with_issues += number

    row += 1
    number = sheet[f'a{row}'].value
    message = str(sheet[f'b{row}'].value)


print("Terminé bien.")
if list_with_issues:
    print(f"salvo por problemas con los siguientes números: {list_with_issues}")

input("Presioná Enter para cerrar.")

