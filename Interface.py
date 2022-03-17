

from tkinter import *
from tkinter import ttk, font
from turtle import right
#from facture import Facture


contour = Tk()
contour.title('Identification de code-barres')
contour.geometry('1000x1000')


prix = "PRIX TOTAL DE LA COMMANDE"

total = Label(contour, text='Total : '+prix).pack(side = BOTTOM)

table = Frame(contour)
table['bg'] = '#AC99F2'
table.pack(side = LEFT)

tablescroll = Scrollbar(table)
tablescroll.pack(side=RIGHT, fill=Y)

matable = ttk.Treeview(table, yscrollcommand=tablescroll.set)
tablescroll.config(command=matable.yview)

matable['columns'] = ('nom', 'qte', 'prix', 'prixtot')

matable.column("#0", width=0,  stretch=NO)
matable.column("nom", anchor=CENTER, width=200)
matable.column("qte",anchor=CENTER, width=200)
matable.column("prix",anchor=CENTER,width=200)
matable.column("prixtot",anchor=CENTER,width=200)

matable.heading("#0",text="",anchor=CENTER)
matable.heading("nom",text="Article",anchor=CENTER)
matable.heading("qte",text="Quantité",anchor=CENTER)
matable.heading("prix",text="Prix unitaire",anchor=CENTER)
matable.heading("prixtot",text="Total de la ligne",anchor=CENTER)

matable.insert(parent='',index='end',iid=0,text='',
values=('1','Ninja','101','Oklahoma', 'Moore'))
matable.insert(parent='',index='end',iid=1,text='',
values=('2','Ranger','102','Wisconsin', 'Green Bay'))
matable.insert(parent='',index='end',iid=2,text='',
values=('3','Deamon','103', 'California', 'Placentia'))
matable.insert(parent='',index='end',iid=3,text='',
values=('4','Dragon','104','New York' , 'White Plains'))


matable.pack()
f2 = font.Font(family='Helvetica', size=20, weight="bold")

blackbutton = Button(contour, text="Imprimer le reçu",fg="black", command=contour.quit, height = 2, width = 20) #Mettre le calcul de sommation en commande + affichage de la facture
blackbutton['font'] = f2
blackbutton.pack(side = BOTTOM)

contour.mainloop()