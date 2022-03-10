from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre

dico = {}
# Simple test pour vérifier que les fonctions fonctionnent bien
if __name__ == "__main__":
    dico = base_de_donnees(dico)[0]
    longueurTot = base_de_donnees(dico)[1]
    print(dico["070989348417"])