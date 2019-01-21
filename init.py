
from pilote_fonction import *

####### Ouvrir la base de donnee sous sql
conn = sqlite3.connect('baseflor.db')
c = conn.cursor()

####### choix de la plante pour un utilisateur
id_plante = id_default()

####### interaction avec l'user

satisfait = False

while not satisfait :
	nom = input("Entrez le nom scientifique de votre plante : ")
	res = data_all(nom,c)
	if len(res) <= 0 :
		res = data_like(nom,c)
		if len(res) <= 0:
			print("Votre plante n'a pas ete trouvee dans la base de donnee, veuillez reessayer.")
		else:
			rep = ""
			for data in res:
				rep += data[1] +"\n"
			print("Votre plante ne correspond pas a aucun nom, reessayez avec un de ces noms :")
			print(rep)
	else : # nom trouve
		id_plante = res[0][0]
		satisfait = True

####### enregistrement

sauvegarder([id_plante], "plante.txt")

conn.close()