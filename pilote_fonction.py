from pilote_basique_capteur import *
from sql import *

################### Pilote de sauvegarde/chargement ###########################

def sauvegarder(liste, nom_fichier):
    texte=""
    virgule = ""
    for i in liste:
        texte += virgule + str(i)
        virgule = ","

    fichier = open(nom_fichier,'w')
    fichier.writelines(texte)

    print(nom_fichier+" sauvegarde")

    fichier.close()

def charger (nom_fichier):

    fichier =open(nom_fichier,'r')
    texte=fichier.readline()

    print(nom_fichier + " charge")
    fichier.close()
    texte=texte.split(",")
    resultat=[]
    for i in texte:
        resultat.append(i)
    print(resultat)
    return resultat

####################### fonction ###############################


def ajout_eau(pin_surf, liste, n):
    a=lecture_humidite_sol (pin_surf)
    liste.append(a)
    if len(liste)>n:
        return liste[:1]
    else:
        return liste

def ajout_lumiere(pin, liste, n):
    a=lecture_luminosite(pin)
    liste.append(a)
    if len(liste)>n:
        return liste[:1]
    else:
        return liste

def ajout_humidite(pin, liste, n):
    a=lecture_humidite_air(pin)
    liste.append(a)
    if len(liste)>n:
        return liste[:1]
    else:
        return liste

def ajout_temperature(pin, liste, n):
    a=lecture_temperature(pin)
    liste.append(a)
    if len(liste)>n:
        return liste[:1]
    else:
        return liste


################## fonction d'analyse ##################

def suffisemment_donnee(n, liste):
    return len(liste)==n


def moyenne(liste):
    a=0
    for i in liste:
        a+=float(i)
    return a/len(liste)

def reset(liste):
    liste=[]
    return liste

################## Fonctions qui ont besoin de la bdd ############# 

# Ouvrir la base de donnee sous sql
# conn = sqlite3.connect('baseflor.db')
# c = conn.cursor()

def ellevacrevereau(moy, plante): #on va fixer une plante arbitraire, renvoie true si la plante est dans de mauvaises conditions
    mesure=niveaunecessaireeau(plante)
    return mesure > (0.8 * moy) 

def ellevacreverlumiere(moy, plante): #idem
    mesure=niveauneccessairelumiere(plante)
    return (mesure > (0.3 * moy) or mesure < (1.7 * moy))

def ellevacrevertemperature(moy, plante): #idem
    mesure=niveauneccessairetemperature(plante)
    return (mesure > (0.2 * moy) or mesure < (1.8 * moy))

def ellevacreverhumidite(moy, plante): #idem
    mesure=niveauneccessairehumidite(plante)
    return (mesure > (0.2 * moy) or mesure < (1.8 * moy))

def niveaunecessaireeau(plante): #renvoie la valeur que doit atteindre la moyenne du niveau d'eau pour que la plante soit en bonne sante
    conn=sqlite3.connect('baseflor.db')
    c=conn.cursor()
    mesure=get_data(plante, c)[5]
    conn.close()
    return float(mesure)*60 

def niveauneccessairelumiere(plante): #renvoie la valeur que doit atteindre la moyenne du niveau de lumiere pour que la plante soit en bonne sante
    conn=sqlite3.connect('baseflor.db')
    c=conn.cursor()
    mesure=get_data(plante, c)[2]
    conn.close()
    return float(mesure) * 70

def niveauneccessairehumidite(plante): #renvoie la valeur que doit atteindre la moyenne du niveau de humi pour que la plante soit en bonne sante
    conn=sqlite3.connect('baseflor.db')
    c=conn.cursor()
    mesure=get_data(plante, c)[4]
    conn.close()
    return float(mesure)*5

def niveauneccessairetemperature(plante): #renvoie la valeur que doit atteindre la moyenne du niveau de temperature pour que la plante soit en bonne sante
    conn=sqlite3.connect('baseflor.db')
    c=conn.cursor()
    mesure=get_data(plante, c)[3]
    conn.close()
    return 10 + float(mesure)*4 

def quantite_eau_necessaire(moy, plante): #id de la plante fixe arbitrairement, renvoie la quantite d'eau en litre a fournir
    return (niveaunecessaireeau(plante) - moy) / 100


def init_est_fait():
    return len(charger("plante.txt"))>0

################# fonction de sortie ####################

def alerte(pin):
    ouvrir_relai(pin)
    time.sleep(0.2)
    fermer_relai (pin)


def arroser(litre,pin):
    """Litre: la quantite d'eau a verser
       pin: la broche du relai"""
    debit=0.125 # le debit de la pompe en litre/seconde
    eautotale=0 # L'eau totale versee
    fermer_relai(pin)
    while eautotale < litre:
        time.sleep(1)
        eautotale+=debit
    ouvrir_relai(pin)
