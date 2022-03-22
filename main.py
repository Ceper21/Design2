from numpy import true_divide
import serial 
import time 
from DecodePyZbar import decoder, decoderWrite
from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre
# #from facture import Facture
# from Interface import Interface
# from tkinter import *


# Simple test pour vérifier que les fonctions fonctionnent bien
if __name__ == "__main__":

    ser = serial.Serial('COM6', 250000, timeout=1)

    dataArray = []
    counter = 0

    while True:
        counter += 1
        data = ser.read(1)
        print(data)
        dataArray.append(data)
        if counter == 10000:
            print(dataArray)
            code = decoderWrite(data)
            if code != []:
                for obj in code:
                    print('Type : ', obj.type)
                    print('Data : ', obj.data,'\n')
            dataArray = []

# root = Tk()
# app = Interface(root)
# root.title('Identification de code-barres')
# root.geometry('1000x300') 
# root.mainloop()
