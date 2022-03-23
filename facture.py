from IdentificateurCodeBarre import Dico
class Facture(dict):

    def __init__(self):
        super().__init__()

    def updateFacture(self, dico, item):
        if dico.verificationPresence(item) == True:
            if item in self.keys():
                    self[str(item)]["Quantite"] += 1
                    self[str(item)]["Prix"] += float(self[str(item)]["Prix_indiv"])
            else:
                element = dico[str(item)]
                nom = element["Nom"]
                quantite = element["Quantité"]
                prix = total_px = float(element["Prix"])
                total_qt = 1
                item_info = {'Article': nom, 'Quantite_indiv': quantite, 'Quantite': total_qt, 'Prix_indiv': prix, 'Prix': total_px}
                self.update({str(item): item_info})

    def totalFacture(self):
        total = 0
        for item in self.keys():
            total += self[str(item)]["Prix"]
        return(total)

    def totalFactureTaxe(self):
        total = self.totalFacture()
        totalTPS = total*0.05
        totalTVQ = total*0.09975
        totalTaxe = total*1.14975
        return(totalTPS, totalTVQ, totalTaxe)

    def printFacture(self):
        string = 'Votre reçu!\n\n------------------------------------------------------------\n\n'
        for i in self.keys():
            string += str(self[str(i)]['Article']) +'\n'
            string += "Prix unitaire: {prixInd} {espace} {prix}$\n\n".format(espace = ' '*(30-len(str(self[str(i)]['Prix']))), prixInd=str(self[str(i)]['Prix_indiv']), prix=str(self[str(i)]['Prix']))
        TPS, TVQ, totalTaxe = self.totalFactureTaxe()
        string += '\n\n\n------------------------------------------------------------\n\nAVANT LES TAXES{}${:,.2f}\n'.format(' '*(30-len('AVANT LES TAXES')), self.totalFacture())
        string += 'TPS{}${:,.2f}\n'.format(' '*(30-len('TPS')), TPS)
        string += 'TVQ{}${:,.2f}\n'.format(' '*(30-len('TVQ')), TVQ)
        string += 'TOTAL{}${:,.2f}\n'.format(' '*(30-len('TOTAL')), totalTaxe) + '\n\n\n------------------------------------------------------------\n'
        string += "Merci d'avoir magasiner chez nous!"
        return(string)
