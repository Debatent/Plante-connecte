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
# utilisant sqlite3
#https://zestedesavoir.com/tutoriels/1294/des-bases-de-donnees-en-python-avec-sqlite3/fonctionnalites-de-base/#1-se-connecter-et-se-deconnecter

import sqlite3

# Ouvrir la base de donnée sous sql
conn = sqlite3.connect('baseflor.db')
c = conn.cursor()

def get_Data (id_plante) : # nom_plante est une chaine de charactere qui designe le nom scientifique de la plante
  c.execute('SELECT * FROM baseflor WHERE id = ?',id_plante)
  return c.fetchall()

def id_plante (nom_plante) :
  c.execute('SELECT * FROM baseflor WHERE nomPlante = ?',nom_plante)
  res = c.fetchone()
  try : 
    k = r[0]
    return r
  except :
    print("Le nom selectionné n'est pas dans la base, réessaiyez plus tard")
