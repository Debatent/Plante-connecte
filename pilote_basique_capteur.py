import grovepi
import time

######################## Luminosite ###########################


def lecture_luminosite(num_pin_lum, k=1):
    #k le nombre de tentative
    grovepi.pinMode(num_pin_lum,"INPUT")
    try:
        res=grovepi.analogRead(num_pin_lum)
        return res
    except IOError :
        print("Erreur de lecture du capteur de luminosite")
        k+=1
        if k>=4:
            raise TentativeError("Nombre de tentative de lecture ecoule")
        else :
            print(k+"eme tentative")
            return lecture_luminosite (num_pin_lum,k)


######################## Humidite Sol ###########################


# NOTE:
# 	The wiki suggests the following sensor values:
# 		Min  Typ  Max  Condition
# 		0    0    0    sensor in open air
# 		0    20   300  sensor in dry soil
# 		300  580  700  sensor in humid soil
# 		700  940  950  sensor in water

# 	Sensor values observer:
# 		Val  Condition
# 		0    sensor in open air
# 		18   sensor in dry soil
# 		425  sensor in humid soil
# 		690  sensor in water


def lecture_humidite_sol (num_pin_humi_sol):
    grovepi.pinMode(num_pin_humi_sol,"INPUT")
    return grovepi.analogRead(num_pin_humi_sol)





######################## Buzzer ###########################


def sonnerie_buzzerON (num_pin_buzzer):
    grovepi.pinMode(num_pin_buzzer,"OUTPUT")

    grovepi.digitalWrite(num_pin_buzzer,1)
    print ('on')


def sonnerie_buzzerOFF (num_pin_buzzer):
    grovepi.pinMode(num_pin_buzzer,"OUTPUT")

    grovepi.digitalWrite(num_pin_buzzer,0)
    print ('off')




######################## Humidite air et temperature ###########################
def lecture_temperature(num_pin_temp,couleur=0):
    #port digital
	temp = grovepi.dht(num_pin_temp,couleur)[0]
	return temp

def lecture_humidite_air(num_pin_temp,couleur=0):
	humi_sol = grovepi.dht(num_pin_temp,couleur)[1]
	return humi_sol


######################## Relai ###########################


def fermer_relai(num_pin_relai):
    grovepi.pinMode(num_pin_relai,"OUTPUT")
    grovepi.digitalWrite(num_pin_relai,1)
    print("Relai ferme")

def ouvrir_relai(num_pin_relai):
    grovepi.pinMode(num_pin_relai,"OUTPUT")
    grovepi.digitalWrite(num_pin_relai,0)
    print("Relai ouvert")
