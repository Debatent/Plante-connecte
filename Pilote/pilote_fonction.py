import time
from pilote_basique_capteur.py import *
from sql.py import *

################### Pilote de sauvegarde/chargement ###########################

def sauvegarder(liste, nom_fichier):
    texte=""
    virgule = ""
    for i in liste:
        texte=text+ virgule +str(i)
        virgule = ","

    try:
        fichier = open (nom_fichier,w)
        fichier.writeline (texte)
    else:
        print(fichier+" sauvegardé")
    finally:
        fichier.close()

def charger (nom_fichier):
    try:
        fichier =open (nom_fichier,r)
        texte=fichier.readline()

    else:
        print (fichier + " chargé")
    finally:
        fichier.close()
    texte=texte.split(",")]
    resultat=[]
    for i in texte:
        resultat.append(int(i))
    return resultat

####################### fonction ###############################


def ajout_eau(pin_surf, pin_prof, liste, n):
    a=lecture_humidite_sol (pin_surf)
    b=lecture_humidite_sol (pin_prof)
    c=(a+b)/2
    liste.append(c)
    if len(liste)>n:
        return liste[1:]
    else:
        return liste

def ajout_lumiere(pin, liste, n):
    a=lecture_luminosite(pin)
    liste.append(a)
    if len(liste)>n:
        return liste[1:]
    else:
        return liste

def ajout_humidite(pin, liste, n):
    a=lecture_humidite_air(pin)
    liste.append(a)
    if len(liste)>n:
        return liste[1:]
    else:
        return liste

def ajout_temperature(pin, liste, n):
    a=lecture_temperature(pin)
    liste.append(a)
    if len(liste)>n:
        return liste[1:]
    else:
        return liste


################## fonction d'analyse ##################

def suffisemment_donnee(n, liste):
    return len(liste)==n


def moyenne(liste):
    a=0
    for i in liste:
        a+=i
    return a/len(liste)


################# fonction de sortie ####################

def alerte(pin):
    ouvrir_relai(pin)
    time.sleep(0.2)
    fermer_relai (pin)
