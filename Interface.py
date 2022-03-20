
from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import ttk, font
#from facture import Facture

class Interface:

    def __init__(self, contour):

        def AfficherFacture():
            self.nouvellefenetre = Toplevel(self.contour)
            self.nouvellefenetre.title("Facture")
            self.nouvellefenetre.geometry("400x500")
            label = Label(self.nouvellefenetre, text ='Voici une facture')
            #label = Label(self.nouvellefenetre, text = Facture.facture())
            label.pack()
        
        self.contour = contour

        self.table = tkinter.Frame(self.contour)
        self.table['bg'] ='#AC99F2'
        self.table.pack()

        self.tablescroll = Scrollbar(self.table)
        self.tablescroll.pack(side=RIGHT, fill=Y)

        self.matable = ttk.Treeview(self.table, yscrollcommand=self.tablescroll.set)
        self.tablescroll.config(command=self.matable.yview)

        self.matable['columns'] = ('nom', 'qte', 'prix', 'prixtot')

        self.matable.column("#0", width=0,  stretch=NO)
        self.matable.column("nom", anchor=CENTER, width=250)
        self.matable.column("qte",anchor=CENTER, width=250)
        self.matable.column("prix",anchor=CENTER,width=250)
        self.matable.column("prixtot",anchor=CENTER,width=250)

        self.matable.heading("#0",text="",anchor=CENTER)
        self.matable.heading("nom",text="Article",anchor=CENTER)
        self.matable.heading("qte",text="Quantité",anchor=CENTER)
        self.matable.heading("prix",text="Prix unitaire",anchor=CENTER)
        self.matable.heading("prixtot",text="Total de la ligne",anchor=CENTER)

        #self.matable.insert(parent='',index='end',iid=0,text='', values=(facture['nom'], facture['Quantite'], facture['Prix_indiv'], facture['Prix']))

        self.matable.pack()
        self.f2 = font.Font(family='Helvetica', size=20, weight="bold")

        #total = Label(contour, text='Total : '+facture.totalFacture()+'$').pack(ipady=1)
        self.total = Label(self.contour, text='Total : ' + '$', font = ("Courier", 30)).pack(ipady=1)

        self.blackbutton = tkinter.Button(self.contour, text="Imprimer le reçu",fg="black", height = 2, width = 20) #Mettre le calcul de sommation en commande + affichage de la facture
        self.blackbutton['font'] = self.f2
        self.blackbutton.bind("<Button>", lambda e: AfficherFacture())
        self.blackbutton.pack(side = BOTTOM)

root = Tk()
app = Interface(root)
root.title('Identification de code-barres')
root.geometry('1000x300') 
root.mainloop()
