from Basique/pilote_basique_capteur.py import *

def ajout_eau(pin_surf, pin_prof, liste, n):
    a=lecture_humidite_sol (pin_surf)
    b=lecture_humidite_sol (pin_prof)
    c=(a+b)/2
    liste.append(c)
    if len(liste)>n:
        return liste[1:]
    else:
        return liste
