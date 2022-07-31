#Import
import pywhatkit
from pynput.keyboard import Key, Controller
import time
import os

#Das die .txt File gelöscht wird
if os.path.exists("#Dateipfad hier/pywhatkit_dbs.txt"):
    os.remove("#Dateipfad hier/pywhatkit_dbs.txt")

#Keyboard Variabel
keyboard = Controller()

#Das eigentliche Script
print('Script Made by Juri Zockt')
print('Hast du dein Handy schon mit Whatsapp Web verbunden. Wenn Nein drück Strg + c')
time.sleep(5)
telephone = int(input('Bitte Nummer eingeben (Ohne Vorwahl und Leerzeichen): '))
message = str(input('Die Nachricht: '))
h = int(input('Zu welcher Stunde soll die Nachricht ankommen: '))
m = int(input('Zu welcher Minute soll die Nachricht ankommen: '))
pywhatkit.sendwhatmsg('+49 ' + str(telephone), message, h, m)
keyboard.press(Key.esc)
keyboard.release(Key.esc)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
