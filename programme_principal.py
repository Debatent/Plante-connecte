import time
from pilote_fonction.py import  *

pin_hum_sol_surf=0
pin_hum_sol_prof=1
pin_temp=0
pin_lum=2
pin_buzzer=1

jour=1#periode dans la quelle on regarde les mesure
periode=24 #nombre de mesure dans cette période

intervalle=3600*1/24

fichier_sauv="Save"+'/'

eau=[]
lumiere=[]
humidite=[]
temperature=[]


while True:
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
    else:
        print("Valeur de luminosité ajoutée")

    sauvegarder(lumiere, fichier_sauv+ "lumiere.txt")



    try:
        humidite=ajout_humidite(pin_temp, humidite,periode)
    else:
        print("Valeur d'humiditée ajoutée")

    sauvegarder(humidite, fichier_sauv+ "humidite.txt")



    try:
        temperature=ajout_temperature(pin_temp,temperature,periode)
    else:
        print("Valeur de température ajoutée")

    sauvegarder(temperature, fichier_sauv+ "temperature.txt")

    '''if suffisemment_donne:
        déduction luminosité, temp, et humidité sol
        if eau non suffisant:
            quantite_eau_necessaire
        if manuel:

        else envoyer_la_sauce'''
