
import xlrd # faire pip install xlutils

## ouverture du fichier Excel 
# wb = xlrd.open_workbook('baseflor.xlsx')
## feuilles dans le classeur
# print wb.sheet_names()
## lecture des données dans la première feuille
# sh = wb.sheet_by_name(u'NomFeuille1')
# for rownum in range(sh.nrows): # pour chaque ligne
#     print sh.row_values(rownum) # lire la ligne
## lecture par colonne
# colonne1 = sh.col_values(0)
# print colonne1
# colonne2=sh.col_values(1)
# print colonne2
## extraction d'un élément particulier
# print colonne1[1],colonne2[1]

def afficheContenuCase (a,b): #la base de donnée à besoin d'être dans le même dossier que ce fichier, a est la ligne, b la colonne
	wb = xlrd.open_workbook('baseflor.xlsx') # C'est cette etape qui prend le plus longtemps
	return wb.sheet_by_name(wb.sheet_names()[0]).col_values(b)[a]

