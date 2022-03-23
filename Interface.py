import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk, font
from facture import Facture

from IdentificateurCodeBarre import Dico

class Interface:

    def __init__(self, contour, facture, dico):

        def AfficherFacture(facture):
            self.nouvellefenetre = tk.Toplevel(self.contour)
            self.nouvellefenetre.title("Facture")
            self.nouvellefenetre.geometry("400x500")
            label = Label(self.nouvellefenetre, text = facture.printFacture())
            label.pack()
        
        def AjouterElement():
            monItem = self.getvalue()
            if dico.verificationPresence(monItem) == True:
                facture.updateFacture(dico, monItem)
                self.updateTable()
            else:
                self.introuvable = tk.Toplevel(self.contour)
                label2 = Label(self.introuvable, text ="Le code-barres que vous avez entré est invalide, veuillez rééssayer.")
                label2.pack()
                retourbouton = Button(self.introuvable, text="OK", command = self.introuvable.destroy)
                retourbouton.pack(side = tk.BOTTOM)

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

        self.total = Label(self.contour, text='Total : {:,.2f}$'.format(facture.totalFactureTaxe()[2])).pack(ipady=1)

        self.blackbutton = tk.Button(self.contour, text="Imprimer le reçu",fg="black", height = 2, width = 20) #Mettre le calcul de sommation en commande + affichage de la facture
        self.blackbutton['font'] = self.f2
        self.blackbutton.bind("<Button>", lambda e: AfficherFacture(facture))
        self.blackbutton.pack(side = tk.BOTTOM)

        self.codeBarre = Label(self.contour, text="Veuillez entre votre code-barres ici : ")
        self.codeBarre.pack(side=tk.LEFT)

        self.element = tk.StringVar()
        self.button_pressed = tk.StringVar()

        self.entrerCode= Entry(self.contour, textvariable = self.element)
        self.entrerCode.pack()
        self.entrerCode.focus()

        self.EntrerBouton = Button(self.contour, text="Entrée", command=lambda: self.button_pressed.set("button pressed"))
        self.EntrerBouton.pack()

        self.EntrerBouton.wait_variable(self.button_pressed)

        if self.element.get() != '':
            AjouterElement()


    def getvalue(self):
        entry = self.element.get()
        print(entry)
        return(entry) 

    def updateTable(self):
        itemiid = 0
        for item in facture.keys():
            self.matable.insert(parent='',index='end',iid=itemiid,text='', values=(facture[str(item)]['Article'], facture[str(item)]['Quantite'], facture[str(item)]['Prix_indiv'], facture[str(item)]['Prix']))
            itemiid += 1

dico = Dico()
dico.initDico()
facture = Facture()
root = tk.Tk()
app = Interface(root, facture, dico)
root.title('Identification de code-barres')
root.geometry('1000x500') 
root.mainloop()