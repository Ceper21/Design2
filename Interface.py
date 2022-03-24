import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk, font
from playsound import playsound
from facture import Facture

from IdentificateurCodeBarre import Dico

class Interface:

    def __init__(self, contour, facture, dico):

        self.facture = facture
        self.dico = dico
        self.contour = contour

        self.table = tk.Frame(self.contour)
        self.table['bg'] ='#AC99F2'
        self.table.pack()

        self.tablescroll = Scrollbar(self.table)
        self.tablescroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.matable = ttk.Treeview(self.table, yscrollcommand=self.tablescroll.set)
        self.tablescroll.config(command=self.matable.yview)

        self.matable['columns'] = ('nom', 'qte', 'prix', 'prixtot')

        self.matable.column("#0", width=0,  stretch=tk.NO)
        self.matable.column("nom", anchor=tk.CENTER, width=250)
        self.matable.column("qte",anchor=tk.CENTER, width=250)
        self.matable.column("prix",anchor=tk.CENTER,width=250)
        self.matable.column("prixtot",anchor=tk.CENTER,width=250)

        self.matable.heading("#0",text="",anchor=tk.CENTER)
        self.matable.heading("nom",text="Article",anchor=tk.CENTER)
        self.matable.heading("qte",text="Quantité",anchor=tk.CENTER)
        self.matable.heading("prix",text="Prix unitaire",anchor=tk.CENTER)
        self.matable.heading("prixtot",text="Total de la ligne",anchor=tk.CENTER)

        self.matable.pack()
        self.f2 = font.Font(family='Helvetica', size=20, weight="bold")

        self.total = Label(self.contour, text='Total sans taxes : {:,.2f}$'.format(facture.totalFacture()))
        self.total.pack(ipady=1)

        self.tps = Label(self.contour, text='TPS : {:,.2f}$'.format(facture.totalFactureTaxe()[0]))
        self.tps.pack(ipady=1)

        self.tvq = Label(self.contour, text='TVQ : {:,.2f}$'.format(facture.totalFactureTaxe()[1]))
        self.tvq.pack(ipady=1)

        self.totalTaxe = Label(self.contour, text='Total : {:,.2f}$'.format(facture.totalFactureTaxe()[2]))
        self.totalTaxe.pack(ipady=1)
        self.totalTaxe['font'] = self.f2

        self.blackbutton = tk.Button(self.contour, text="Imprimer le reçu",fg="black", height = 2, width = 20) #Mettre le calcul de sommation en commande + affichage de la facture
        self.blackbutton['font'] = self.f2
        self.blackbutton.bind("<Button>", lambda e: self.AfficherFacture(facture))
        self.blackbutton.pack()

        self.codeBarre = Label(self.contour, text="En cas de problème, veuillez entrer manuellement votre code-barre ici : ")
        self.codeBarre.pack(side=tk.LEFT)

        self.element = tk.StringVar()

        self.entrerCode= Entry(self.contour, textvariable = self.element)
        self.entrerCode.pack(side=tk.LEFT)
        self.entrerCode.focus()

        self.EntrerBouton = Button(self.contour, text="Entrée", command=self.clickEnter)
        self.EntrerBouton.pack(side=tk.LEFT)

    def AfficherFacture(self, facture):
        nouvellefenetre = tk.Toplevel(self.contour)
        nouvellefenetre.title("Facture")
        label = Label(nouvellefenetre, text = facture.printFacture())
        label.pack()

    def AfficherErreur(self):
        introuvable = tk.Toplevel(self.contour)
        label2 = Label(introuvable, text ="Le code-barres que vous avez entré est invalide, veuillez rééssayer.")
        label2.pack()
        retourbouton = Button(introuvable, text="OK", command = introuvable.destroy)
        retourbouton.pack(side = tk.BOTTOM)

    def AjouterElement(self, monItem):
        if self.dico.verificationPresence(monItem) == True:
            playsound('Barcode-scanner-beep-sound.mp3')
            #playsound('beep.mp3')
            self.facture.updateFacture(self.dico, monItem)
            self.updateTable()
        else:
            self.AfficherErreur()

    def clickEnter(self):
        if self.element.get() != '':
            monItem = self.element.get().strip()
            self.AjouterElement(monItem)
            self.entrerCode.delete(0, tk.END)

    def updateTable(self):
        for item in self.matable.get_children():
            self.matable.delete(item)
        itemiid = 0
        for item in self.facture.keys():
            self.matable.insert(parent='',index='end',iid=itemiid,text='', values=(self.facture[str(item)]['Article'], self.facture[str(item)]['Quantite'], self.facture[str(item)]['Prix_indiv'], self.facture[str(item)]['Prix']))
            itemiid += 1
        self.total.config(text='Total sans taxes : {:,.2f}$'.format(self.facture.totalFacture()))
        self.tps.config(text='TPS : {:,.2f}$'.format(self.facture.totalFactureTaxe()[0]))
        self.tvq.config(text='TVQ : {:,.2f}$'.format(self.facture.totalFactureTaxe()[1]))
        self.totalTaxe.config(text='Total : {:,.2f}$'.format(self.facture.totalFactureTaxe()[2]))

# dico = Dico()
# dico.initDico()
# facture = Facture()
# root = tk.Tk()
# app = Interface(root, facture, dico)
# root.title('Identification de code-barres')
# root.geometry('1000x500') 
# root.mainloop()