import time
from Pilote/pilote_fonction.py import  *

pin_hum_sol_surf=0
pin_hum_sol_prof=1
pin_temp=0
pin_lum=2
pin_buzzer=1


eau=[]
lumiere=[]
humidite=[]
temperature=[]


while True:
    try:
        eau=ajout_eau(pin_hum_sol_prof,pin_hum_sol_surf,eau)
    except TentativeError:
        print("Le ou les capteurs d'humidité n'ont pas pu être lu")
        print("Vérifiez si le capteur d'humidité de profondeur est branché à la prise A"+pin_hum_sol_prof)
        print("Vérifiez si le capteur d'humidité de surface est branché à la prise A"+pin_hum_sol_prof)
    else:
        print("Valeur de l'eau ajoutée")


    try:
        lumiere=ajout_lumiere(pin_lum,lumiere)
    else:
        print("Valeur de luminosité ajoutée")


    try:
        humidite=ajout_humidite(pin_temp, humidite)
    else:
        print("Valeur d'humiditée ajoutée")

    try:
        temperature=ajout_temperature(pin_temp,temperature)
        else:
            print("Valeur de température ajoutée")
