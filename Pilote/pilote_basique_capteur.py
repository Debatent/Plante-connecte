"""
MIT License
Copyright (c) 2018 Debatent and GuillaumeClementPolytech
Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is furnished to do so, subject 
to the following conditions:
The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import grovepi
import time

######################## Luminosité ###########################


def lecture_luminosite(num_pin_lum):
    grovepi.pinMode(num_pin_lum,"INPUT")
    print(grovepi.analogRead(num_pin_lum))



######################## Humidité Sol ###########################


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




######################## Humidité air et température ###########################
def lecture_temperature(num_pin_temp,couleur=0):
	temp = grovepi.dht(num_pin_temp,couleur)[0]
	return temp

def lecture_humidite_air(num_pin_temp,couleur=0):
	humi_sol = grovepi.dht(num_pin_temp,couleur)[1]
	return humi_sol

	
######################## Relai ###########################


def fermer_relai(num_pin_relai):
    grovepi.pinMode(num_pin_relai,"OUTPUT")
    grovepi.digitalWrite(num_pin_relai,1)
    
def ouvrir_relai(num_pin_relai):
    grovepi.pinMode(num_pin_relai,"OUTPUT")
    grovepi.digitalWrite(num_pin_relai,0)
