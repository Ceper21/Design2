from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre

dico = {}
binaire = "1111111001100011"+"010"+ 42*"0" + "01010" + 42*"0" + "010"+ "000011010"
# Simple test pour vérifier que les fonctions fonctionnent bien
if __name__ == "__main__":
    dico = base_de_donnees(dico)[0]
    longueurTot = base_de_donnees(dico)[1]
    x = decodage(binaire)
    print(x, len(x))

    