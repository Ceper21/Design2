from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre

class Facture:

    def __init__(self):
        self.facture = {}

    def updateFacture(self, dico, sequence_binaire):
        item = decodage(sequence_binaire) # ajouter la bonne variable Arduino de la sequence de bit

        if validationDernierChiffre(item) == True:
            test_dico = verificationPresence(item, dico)
        else:
            print("L'item que vous tenter d'acheter n'est pas disponible. Veuillez vous référer à un commis.")
        if test_dico == True:
            if verificationPresence(item, self.facture) == True:
                self.facture[str(item)]["Quantite"] += self.facture[str(item)]["Quantite_indiv"]
                self.facture[str(item)]["Prix"] += self.facture[str(item)]["Prix_indiv"]
            else:
                element = dico[str(item)] # on crée le dico dans le main ou on le crée ici?
                nom = element["Nom"]
                quantite, total_qt = element["Quantite"]
                prix, total_px = element["Prix"]
                item_info = {'Article': nom, 'Quantite_indiv': quantite, 'Quantite': total_qt, 'Prix_indiv': prix, 'Prix': total_px}
                self.facture.update({str(item): item_info})

    def totalFacture(self):
        total = 0
        for item in self.facture:
            total += item["Prix"]
        return(total)

    def totalFactureTaxe(self):
        total = self.totalFacture()
        totalTPS = total*0.05
        totalTVQ = total*0.09975
        totalTaxe = total*1.14975
        return(totalTPS, totalTVQ, totalTaxe)