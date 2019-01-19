# Plante-connecte

Projet utilisant un raspberry en IG3

## Table des matières

   I. Installations	
   II. Démarrage 	
   III. Utilisation 	
   IV. Foire Aux Questions / Frequently Asked Questions 
   V. Materiel utilisé

## Installations

Pour pouvoir utiliser sa Plante Connectée, il faut vous munir d’une plante, puis :


   1) Brancher la Raspberry et la pompe a une prise secteur chacune
    
   2) Brancher la Raspberry via le câble Ethernet a votre Box Internet / Réseau local
    
   3) Brancher les capteurs avec les câbles Grove sur la Raspberry :
       ◦ Le capteur d’humidité en A0
       ◦ Le capteur de température en D0
       ◦ Le capteur de luminosité en A2
       ◦ Le relais du câble de la pompe en D3
       
   4) Placer la pompe dans un récipient d’eau, à une distance sûre du système
   
   5) Placer le tuyau de la pompe dans la terre du pot de la plante
   
   6) Enfoncer le capteur d’humidité dans la terre du pot de la plante, de l’autre coté du tuyau
   
   7) Placer les capteurs restant autour de la plante

Et voila, vous êtes maintenant prêts à lancer votre Plante Connectée.
       
## Démarrage 

Pour démarrer votre Plante Connectée, voici ce que vous devez faire :


   1) Connectez vous à votre Raspberry :
       ◦ Ouvrer une console de commande (si vous ne savez pas comment, voir F.A.Q.)
       ◦ Entrez dans la console :
           ▪ ssh plante@ig-rasp16
       ◦ On vous demande un mot de passe : connecte 
               ( Ne vous inquietez pas si le mot de passe ne s’affiche pas) 
   2) Lorsque vous êtes connecté, entrez :
           ▪ cd Plante-connecte/
           ▪ python3 init.py
             
   3) le système vous demande alors le nom de votre plante : entrez le nom scientifique de celle-ci : le système vous indiquera s’il la trouve dans la base de donnée. S’il la trouve pas, il vous redemandera son nom.

Voilà, le système est lancé, vous pouvez refermer votre console !! Faites juste attention à ne pas débranche votre Raspberry, ce qui éteindrait votre système.

Si c'est le cas, juste rebranchez cotre raspberry, toutes les informations sont stockées

## Utilisation 

Une fois lancé, votre Plante Connectée va se mettre à mesurer l’état de votre plante automatiquement. Ce n’est pas fait pour être intéragi directement, carr il s’occupe de votre plante à votre place.

Si vous voulez consulter les résultats de ses mesures, ouvrez votre navigateur et entrez dans la barre d’adresse :

   • http://dweet.io/follow/PlanteCo
    
Normalement, vous verrez, en moins de 30 minutes, s’afficher les dernières mesures de votre Plante Connectée, ainsi que si votre Plante Connectée est dans un bon état.

## FAQ : Foire Aux Questions / Frequently Asked Questions 


   1. Comment ouvrir une console de commande ?
       ◦ Cela dépends du systeme d’expoitation de votre ordinateur :
            ▪ Windows : appuyer sur la touche + R, entrez cmd dans la boite de dialogue, puis validez
            ▪ Mac : En haut a droite, allez dans rechercher, puis entrez terminal, et ouvrez l’application terminal.
            ▪ Linux : voir sur ce lien : https://doc.ubuntu-fr.org/terminal
            
   2. Comment savoir si la plante Connectée est sous tension ?
       ◦ Normalement, plusieurs diodes de la raspberry sont allumées
        
   3. J’arrive pas à me connecter à la Plante Connectée !!
       ◦ Vérifiez que vous êtes bien connecté au même réseau / Box internet que votre Raspberry lorsque vous la mettez en route
        
   4. Est-ce que je peut laisser ma Plante Connectée seule ?
       ◦ Oui : normalement, si vous avez bien lancé le systeme, vous pouvez ensuite laisser votre Plante Connecté seule sous tension, et elle prendra ses mesures toute seule
        
   5. J’ai débranché la Plante Connectée involontairement, que dois-je faire ?
       ◦ Vous devez redemarrer la Plante Connectée comme si c’était la première fois que vous l’utilisez : ses données importantes sont sauvegardées régulièrement
        
## Materiels utilisés

RaspberryPi

GrovePlus => grovepi

4 capteurs => Seeed wiki

Python 3.7 et sqlite3

Base de donnée => philippe.julve.pagesperso-orange.fr/catminat.htm

Julve, Ph., 1998 ff. - Baseflor. Index botanique, écologique et chorologique de la flore de France. Version : "date de la version citée". http://perso.wanadoo.fr/philippe.julve/catminat.htm
