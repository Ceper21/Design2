from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre

class Facture:

    def __init__(self):
        self.facture = {}

    def updateFacture(self, dico, item):
        if item in self.facture:
                self.facture[str(item)]["Quantite"] += self.facture[str(item)]["Quantite_indiv"]
                self.facture[str(item)]["Prix"] += self.facture[str(item)]["Prix_indiv"]
        else:
            element = dico[str(item)]
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
