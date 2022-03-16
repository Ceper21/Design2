from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre

facture = {}
item = decodage(sequence_binaire) # ajouter la bonne variable Arduino de la sequence de bit

if validationDernierChiffre(item) == True:
    test_dico = verificationPresence(item, dico)
else:
    print("L'item que vous tenter d'acheter n'est pas disponible. Veuillez vous référer à un commis.")
if test_dico == True:
    if verificationPresence(item, facture) == True:
        facture[str(item)]["Quantite"] += facture[str(item)]["Quantite_indiv"]
        facture[str(item)]["Prix"] += facture[str(item)]["Prix_indiv"]
    else:
        element = dico[str(item)] # on crée le dico dans le main ou on le crée ici?
        nom = element["Nom"]
        quantite, total_qt = element["Quantite"]
        prix, total_px = element["Prix"]
        item_info = {'Article': nom, 'Quantite_indiv': quantite, 'Quantite': total_qt, 'Prix_indiv': prix, 'Prix': total_px}
        facture.update(str(item): item_info)