import time
from Pilote/pilote_fonction.py import  *

pin_hum_sol_surf=0
pin_hum_sol_prof=1
pin_temp=0
pin_buzzer=1
pin_lum=2

while True:
    try:
        a=moyenne_eau(pin_hum_sol_prof,pin_hum_sol_surf)
    except TentativeError:
        print("Le ou les capteurs d'humidité n'ont pas pu être lu")
        print("Verifiez si le capteur d'humidité de profondeur est branché à la prise A"+pin_hum_sol_prof)
        print("Verifiez si le capteur d'humidité de surface est branché à la prise A"+pin_hum_sol_prof)
