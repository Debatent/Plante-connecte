import xlrd # faire pip install xlutil

# ouverture du fichier Excel 

wb = xlrd.open_workbook('baseflor.xlsx')
 
# feuilles dans le classeur

print wb.sheet_names()
 
# lecture des données dans la première feuille
sh = wb.sheet_by_name(u'NomFeuille1')
for rownum in range(sh.nrows): # pour chaque ligne
    print sh.row_values(rownum) # lire la ligne

# lecture par colonne
colonne1 = sh.col_values(0)
print colonne1
 
colonne2=sh.col_values(1)
print colonne2
 
# extraction d'un élément particulier
print colonne1[1],colonne2[1]

a=1
b=1
c=1

# lis la valeur dans la case a,b (ligne, colonne)de la c-ieme feuille de baseflor.xlsx, en une seule expression 
print xlrd.open_workbook('baseflor.xlsx').sheet_by_name(xlrd.open_workbook('baseflor.xlsx').sheet_names[c]).col_values(b)[a]
