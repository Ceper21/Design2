from numpy import true_divide
import serial 
import time 
from DecodePyZbar import decoder
from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre
#from facture import Facture
from facture import Facture
from Interface import Interface
from tkinter import *


# Simple test pour vérifier que les fonctions fonctionnent bien
if __name__ == "__main__":

    ser = serial.Serial('COM4', 9600, timeout=1)

    dataArray = []

    while True:
        data = ser.readline()
        dataArray.append(str(data).strip("b'\\r\\n"))
        print(dataArray)
        code = decoder(data)
        if code != []:
            for obj in code:
                print('Type : ', obj.type)
                print('Data : ', obj.data,'\n')
            dataArray = []
    #facture = Facture.facture()
    #dico = base_de_donnees(dico)
    #Code = decodage(binaire)
    #print(Code)
    #print(verificationPresence(Code, dico))
    #x = dico["000000000000"]
    #print(x)

root = Tk()
app = Interface(root)
root.title('Identification de code-barres')
root.geometry('1000x300') 
root.mainloop()
