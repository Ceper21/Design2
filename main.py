from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre



if __name__ == "__main__":
    dico = base_de_donnees()
    for i in range(10):
        x = input("Veuillez entrer le code-barre")
        print(verificationPresence(str(x), dico))