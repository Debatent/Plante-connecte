from Basique/pilote_basique_capteur.py import *

def moyenne_eau(pin_surf,pin_prof):
    try:
        a=lecture_humidite_sol (pin_surf)
        
