from numpy import true_divide
import serial 
import time 
from DecodePyZbar import decoderWrite, show, convertToBIT
from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre
import struct
from facture import Facture
# from Interface import Interface
# from tkinter import *


# Simple test pour vérifier que les fonctions fonctionnent bien
if __name__ == "__main__":

    ser = serial.Serial('COM6', 250000, timeout=1)

    dataArray = []
    FORMAT = '<B'
    facture = Facture.facture()

    while True:
        data = ser.read(1)
        send = struct.unpack(FORMAT, data)[0]

        if send == 2:
            print(dataArray)
            code = decoderWrite(dataArray)
            dataShow, sizeShow = convertToBIT(dataArray) # a conserver pour les tests seulement (sert à afficher l'image du code bar)
            show(dataShow, sizeShow)
            if code != []:
                for obj in code:
                    print('Type : ', obj.type)
                    print('Data : ', obj.data,'\n')
            dataArray = []
        dataArray.append(send)

# root = Tk()
# app = Interface(root)
# root.title('Identification de code-barres')
# root.geometry('1000x300') 
# root.mainloop()
