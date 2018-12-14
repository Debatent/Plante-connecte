# utilisant sqlite3
#https://zestedesavoir.com/tutoriels/1294/des-bases-de-donnees-en-python-avec-sqlite3/fonctionnalites-de-base/#1-se-connecter-et-se-deconnecter

import sqlite3

# Ouvrir la base de donnée sous sql
conn = sqlite3.connect('baseflor.db')
c = conn.cursor()

def get_Data (id_plante) :
  # nom_plante est une chaine de charactere qui designe le nom scientifique de la plante
  id_plante = (id_plante,)
  c.execute('SELECT * FROM base WHERE id = ?',id_plante)
  return c.fetchall()[0]

def id_plante (nom_plante) :
  # il faut appeler
  try :
    nom_plante = (nom_plante,)
    c.execute('SELECT * FROM base WHERE nom = ?',nom_plante)
    res = c.fetchone()[0]
    return res
  except :
    print("Le nom selectionné n'est pas dans la base, réessayez")

def get_Table_Entiere():
  c.execute('SELECT * FROM base')
  return c.fetchall()
