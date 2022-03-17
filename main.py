from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre
from facture import Facture


binaire = "1111111001100011"+"010"+ 6*"0001101" + "01010" + 6*"0001101" + "010"+ "000011010" # à enlever plus tard (test)

dico = {}
facture = {}

# Simple test pour vérifier que les fonctions fonctionnent bien
if __name__ == "__main__":
    facture = Facture.facture()
    dico = base_de_donnees(dico)
    Code = decodage(binaire)
    print(Code)
    print(verificationPresence(Code, dico))
    x = dico["000000000000"]
    print(x)