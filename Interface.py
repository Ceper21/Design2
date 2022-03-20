
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk, font
#from facture import Facture



contour = Tk()
contour.title('Identification de code-barres')
contour.geometry('1000x300')

def AfficherFacture():
    nouvellefenetre = Toplevel(contour)
    nouvellefenetre.title("Facture")
    nouvellefenetre.geometry("300x700")
    label = Label(nouvellefenetre, text ="This is a new Window")
    label.pack()

table = Frame(contour)
table['bg'] = '#AC99F2'
table.pack()

tablescroll = Scrollbar(table)
tablescroll.pack(side=RIGHT, fill=Y)

matable = ttk.Treeview(table, yscrollcommand=tablescroll.set)
tablescroll.config(command=matable.yview)

matable['columns'] = ('nom', 'qte', 'prix', 'prixtot')

matable.column("#0", width=0,  stretch=NO)
matable.column("nom", anchor=CENTER, width=250)
matable.column("qte",anchor=CENTER, width=250)
matable.column("prix",anchor=CENTER,width=250)
matable.column("prixtot",anchor=CENTER,width=250)

matable.heading("#0",text="",anchor=CENTER)
matable.heading("nom",text="Article",anchor=CENTER)
matable.heading("qte",text="Quantité",anchor=CENTER)
matable.heading("prix",text="Prix unitaire",anchor=CENTER)
matable.heading("prixtot",text="Total de la ligne",anchor=CENTER)

#matable.insert(parent='',index='end',iid=0,text='',
#values=(facture['nom'], facture['Quantite'], facture['Prix_indiv'], facture['Prix']))


matable.pack()
f2 = font.Font(family='Helvetica', size=20, weight="bold")

#total = Label(contour, text='Total : '+facture.totalFacture()+'$').pack(ipady=1)
total = Label(contour, text='Total : ' + '$').pack(ipady=1)

blackbutton = Button(contour, text="Imprimer le reçu",fg="black", height = 2, width = 20) #Mettre le calcul de sommation en commande + affichage de la facture
blackbutton['font'] = f2
blackbutton.bind("<Button>", lambda e: AfficherFacture(contour))
blackbutton.pack(side = BOTTOM)

contour.mainloop()