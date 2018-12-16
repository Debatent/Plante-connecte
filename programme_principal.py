import time
import os
from os.path.abspath(Pilote/pilote_fonction.py) import *

pin_hum_sol_surf=0
pin_hum_sol_prof=1
pin_temp=0
pin_lum=2
pin_buzzer=1

#jour=1#periode dans la quelle on regarde les mesure
periode=24 #nombre de mesure dans cette période

#intervalle=3600*1/24

fichier_sauv=str(os.getcwd())+"Save"+'/'

eau=[]
lumiere=[]
humidite=[]
temperature=[]


# while True: Si on fait en CRON, il faut changer ça : plus un while true
try:
    eau=ajout_eau(pin_hum_sol_prof,pin_hum_sol_surf,eau,periode)
except TentativeError:
    print("Le ou les capteurs d'humidité n'ont pas pu être lu")
    print("Vérifiez si le capteur d'humidité de profondeur est branché à la prise A"+pin_hum_sol_prof)
    print("Vérifiez si le capteur d'humidité de surface est branché à la prise A"+pin_hum_sol_prof)
else:
    print("Valeur de l'eau ajoutée")

time.sleep(0.5)

sauvegarder(eau, fichier_sauv+ "eau.txt")


try:
    lumiere=ajout_lumiere(pin_lum,lumiere,periode)
except TentativeError:
    print("Le capteur de luminosité n'a pas pu être lu")
    print("Vérifiez si le capteur de luminosité est branché à la prise A"+pin_lum)
else:
    print("Valeur de luminosité ajoutée")

sauvegarder(lumiere, fichier_sauv+ "lumiere.txt")

time.sleep(0.5)

try:
    humidite=ajout_humidite(pin_temp, humidite,periode)
except TentativeError:
    print("Le capteur d'humidité de l'air/température est branché à la prise D"+pin_temp)
    print("Vérifiez si le capteur d'humidité de l'air/température est branché à la prise D"+pin_temp)
else:
    print("Valeur d'humiditée ajoutée")

sauvegarder(humidite, fichier_sauv+ "humidite.txt")

time.sleep(0.5)

try:
    temperature=ajout_temperature(pin_temp,temperature,periode)
except TentativeError:
    print("Le capteur d'humidité de l'air/température n'a pas pu être lu")
    print("Vérifiez si le capteur d'humidité de l'air/température est branché à la prise D"+pin_temp)
else:
    print("Valeur de température ajoutée")

sauvegarder(temperature, fichier_sauv+ "temperature.txt")

time.sleep(0.5)

if reservoirvide():
    alerte()
    print("on ne peut pas s'assurer que la plante a assez d'eau, raison : réservoir vide")

elif suffisemment_donnee(periode,eau):
    moy=moyenne(eau)
    if ellevacrever(moy):
        quantite_eau_necessaire
        arroser
        reset(eau)
    else:
        print("Tout va bien")

if suffisemment_donnee(periode,lumiere):
    moy=moyenne(lumiere)
    if ellevacrever(moy):
        if moy <= niveauneccessaire:
            print ("Alerte: mettez votre plante plus à la lumière")
        else:
            print ("Alerte: mettez votre plante moins à la lumière")



if suffisemment_donnee(periode,temperature):
    moy=moyenne(temperature)
    if ellevacrever(moy):
        if moy <= niveauneccessaire:
            print ("Alerte: mettez votre plante dans un endroit plus chaud")
        else:
            print ("Alerte: mettez votre plante dans un endroit moins chaud")

    '''déduction luminosité, temp, et humidité sol
    if eau non suffisant:
        quantite_eau_necessaire
    if manuel:

    else envoyer_la_sauce'''
