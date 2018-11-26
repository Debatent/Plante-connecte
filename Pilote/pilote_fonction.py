from Basique/pilote_basique_capteur.py import *

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
