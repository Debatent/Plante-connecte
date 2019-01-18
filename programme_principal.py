import time

from pilote_fonction import *

pin_hum_sol_surf=0
pin_hum_sol_prof=1
pin_temp=0
pin_lum=2
pin_buzzer=1
pin_relai=3

#jour=1#periode dans la quelle on regarde les mesure
periode=24 #nombre de mesure dans cette période

#intervalle=3600*1/24
automatique = True




eau=[]
lumiere=[]
humidite=[]
temperature=[]


# while True: Si on fait en CRON, il faut changer ça : plus un while true
try:
    eau=ajout_eau(pin_hum_sol_surf, eau, periode)
except TentativeError:
    print("Le ou les capteurs d'humidité n'ont pas pu être lu")
    #print("Vérifiez si le capteur d'humidité de profondeur est branché à la prise A"+pin_hum_sol_prof)
    print("Vérifiez si le capteur d'humidité de surface est branché à la prise A"+pin_hum_sol_prof)
else:
    print("Valeur de l'eau ajoutée")

sauvegarder(eau, "eau.txt")

time.sleep(0.5)





try:
    lumiere=ajout_lumiere(pin_lum,lumiere,periode)
except TentativeError:
    print("Le capteur de luminosité n'a pas pu être lu")
    print("Vérifiez si le capteur de luminosité est branché à la prise A"+pin_lum)
else:
    print("Valeur de luminosité ajoutée")

sauvegarder(lumiere, "lumiere.txt")

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

sauvegarder(temperature,"temperature.txt")

time.sleep(0.5)








"""
if reservoirvide():
    alerte()
    print("on ne peut pas s'assurer que la plante a assez d'eau, raison : réservoir vide")
"""




elif suffisemment_donnee(periode,eau):
    moy=moyenne(eau)
    if ellevacrevereau(moy):
        if automatique:
            quantite=quantite_eau_necessaire()
            arroser(quantite, pin_relai)
            reset(eau)
        else:
            if eau[-1] >= niveaunecessaireeau():
                reset(eau)
            else:
                print("Alerte: veulliez arroser votre plante")
    else:
        print("Tout va bien")






if suffisemment_donnee(periode,lumiere):
    moy=moyenne(lumiere)
    if ellevacreverlumiere(moy):
        if moy <= niveauneccessairelumiere():
            print ("Alerte: mettez votre plante plus à la lumière")
        else:
            print ("Alerte: mettez votre plante moins à la lumière")






if suffisemment_donnee(periode,temperature):
    moy=moyenne(temperature)
    if ellevacrevertemperature(moy):
        if moy <= niveauneccessairetemperature():
            print ("Alerte: mettez votre plante dans un endroit plus chaud")
        else:
            print ("Alerte: mettez votre plante dans un endroit moins chaud")


print("la boucle s'est terminée")


    '''déduction luminosité, temp, et humidité sol
    if eau non suffisant:
        quantite_eau_necessaire
    if manuel:

    else envoyer_la_sauce'''
