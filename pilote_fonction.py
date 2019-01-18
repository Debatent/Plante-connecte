import time
from pilote_basique_capteur.py import *
from sql import *

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


def ajout_eau(pin_surf, liste, n):
    a=lecture_humidite_sol (pin_surf)
"""    b=lecture_humidite_sol (pin_prof)
    c=(a+b)/2"""
    liste.append(a)
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

def reset(liste):
    return liste=[]

#def ellevacrevereau(moy): #on va fixer une plante arbitraire, renvoie true si la plante est dans de mauvaises conditions

#def ellevacreverlumiere(moy): #idem

#def ellevacrevertemperature(moy): #idem

#def quantite_eau_necessaire(): #nom de la plante fixé arbitrairement, renvoie la quantité d'eau en litre à fournir

#def niveaunecessaireeau(): #renvoie la valeur que doit atteindre la moyenne du niveau d'eau pour que la plante soit en bonne santé

#def niveauneccessairelumiere(): #renvoie la valeur que doit atteindre la moyenne du niveau de lumiere pour que la plante soit en bonne santé

#def niveauneccessairetemperature(): #renvoie la valeur que doit atteindre la moyenne du niveau de temperature pour que la plante soit en bonne santé

################# fonction de sortie ####################

def alerte(pin):
    ouvrir_relai(pin)
    time.sleep(0.2)
    fermer_relai (pin)


def arroser(litre,pin):
    """Litre: la quantité d'eau à verser
       pin: la broche du relai"""
    debit=0.125#le debit de la pompe en litre/seconde
    eautotale=0#L'eau totale versée
    ouvrir_relai(pin)
    while eautotale < litre:
        time.sleep(1)
        eautotale+=debit
    fermer_relai(pin)
