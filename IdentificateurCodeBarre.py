# On commence par upload les infos concernant les produits ATTENTION --> Si vous voulez tester il faut placer le bon lien de l'emplacement
# de sauvegarde sur votre ordi du fichier upcPrice
fichier_UPC_A = open(rb"C:\Users\spart\Desktop\Hiver2022\Design2\Design2\upcPrice.txt", encoding="utf8", errors='ignore')
contenu = fichier_UPC_A.read()
liste_contenu = contenu.split("\n")

#La corrrespondance de ce que représente les nombres binaires en UPC-A pour les côtés gauche et droit Left Right
dicoL = {"0001101": "0", "0011001": "1", "0010011": "2", "0111101": "3", "0100011": "4",
"0110001": "5", "0101111": "6", "0111011": "7", "0110111": "8", "0001011": "9"}

dicoR = {"1110010" : "0", "1100110": "1", "1101100": "2", "1000010": "3", "1011100": "4",
"1001110": "5", "1010000": "6", "1000100": "7", "1001000": "8", "1110100": "9"}


# Fonction qui serait appelée au lancement du code (juste une fois car prend du temps) pour placer les infos suivantes dans un dico :
# {clée = Code-barre : [Nom du produit, Prix]} Bref à travailler... 
def base_de_donnees(dico):
    for article in liste_contenu:
        elements = article.split(",") # elements = [[Code_barre, Qte, Nom, prix], [etc]]
        if len(elements[0]) == 13:
            if len(elements) == 2:
                dico.update({elements[0][1:]: {"Nom": "Non-défini", "Quantité": "Non-défini", "Prix": "Non-défini"}})

            elif len(elements) == 3:
                dico.update({elements[0][1:]: {"Nom": elements[-1], "Quantité": elements[1], "Prix": "Non-défini"}})

            elif int(elements[0][0]) == 0:
                dico.update({elements[0][1:]: {"Nom": elements[2], "Quantité": elements[1], "Prix": elements[-1]}})
        if len(elements[0]) > 13:
            dico.update({elements[0][2:]: {"Nom": elements[2], "Quantité": elements[1], "Prix": elements[-1]}})
    return (dico)


# Fonction servant à convertir le nombre binaire provenant de l'Arduino en nombre décimale
# On doit également donner une version inversée du code reçut en raison du fait que le
# laser peut aller dans les deux sens ou que le code peut être à l'envers 
def decodage(binaire):

    stockage = []
    compteur = 1
    for bit in binaire:
        stockage.append(bit)

        if len(stockage) == 3:
            if stockage == ["0","1" ,"0" ]:
                continue
            stockage.pop(0)
        if len(stockage) in range(50, 94):
            if int(bit) == 0:
                bit = '1'
            elif int(bit) == 1:
                bit = '0'
            stockage.pop(-1)
            stockage.append(bit)

        if len(stockage) > 91:
            break
    stockage = "".join(stockage[3:45] + stockage[50:])
    decoupage = [stockage[i:i+7] for i in range(0, len(stockage), 7)]
    nombre = ''
    for position, paquet in enumerate(decoupage):
        if position in range(0, 6):
            if paquet in dicoL:
                nombre += dicoL[paquet]

        else:
            if paquet in dicoR:
                nombre += dicoR[paquet]
    return nombre

# On vérifie si le Code_barre à l'endroit ou celui inversé se trouve dans notre banque de données.
def verificationPresence(Code, dico):

    if Code in dico:
        return True
    else:
        return False

# Fonction qui sert à valider le dernier chiffre du code reçut. Sert à valider le bon sens 
# du code, mais aussi évite d'aller fouiller dans le dictionnaire de produits (sauve du temps)
def validationDernierChiffre(Code_barre):
    convert = map(int, Code_barre)
    code = list(convert)
    nombre = 3*sum(code[1: -1: 2]) + sum(code[0: -1: 2])
    pGMultiple = (int(nombre/10) + 1) * 10

    if (pGMultiple - nombre) == int(Code_barre[13]):
        return True
    else:
        return False
