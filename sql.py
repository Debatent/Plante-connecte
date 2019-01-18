# utilisant sqlite3
# https://zestedesavoir.com/tutoriels/1294/des-bases-de-donnees-en-python-avec-sqlite3/fonctionnalites-de-base/#1-se-connecter-et-se-deconnecter

import sqlite3

# format de la base de donnée : 
# CREATE TABLE base (id real, nom string, lumi real, temp real, humi_air real, humi_sol real)


def get_data (id_plante, c) : # c est le curseur vers la base de donnée, renvoie un sextuplet, id_plante est une Id valide (obtenu grace a la fonction id_plante())
  # [0] est l'id, [1] est le nom, [2] est la luminosite, [3] est la temperature, [4] est l'humidite de l'air, [5] est l'humidite du sol
  id_plante = (id_plante,)
  c.execute('SELECT * FROM base WHERE id = ?',id_plante)
  return c.fetchall()[0]

def data_all (nom_plante, c) :# c est le curseur vers la base de donnée
  # nom_plante est une chaine de charactere qui designe le nom scientifique de la plante
  nom_plante = (nom_plante,)
  c.execute('SELECT * FROM base WHERE nom = ?', nom_plante)
  res = c.fetchall()
  return res

def data_like (nom_plante, c) :# c est le curseur vers la base de donnée
  # nom_plante est une chaine de charactere qui designe le nom scientifique de la plante
  nom_plante = ("%"+nom_plante+"%",)
  c.execute('SELECT * FROM base WHERE nom LIKE ?', nom_plante)
  res = c.fetchall()
  return res

def id_plante (nom_plante, c) :# c est le curseur vers la base de donnée
  # nom_plante est une chaine de charactere qui designe le nom scientifique de la plante
  try :
    nom_plante = (nom_plante,)
    c.execute('SELECT * FROM base WHERE nom = ?',nom_plante)
    res = c.fetchone()[0]
    return res
  except :
    print("ERREUR INATENDUE")

def get_table_entiere():
  c.execute('SELECT * FROM base')
  return c.fetchall()

def id_default() :
  return 75521.0


