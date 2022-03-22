from numpy import true_divide
import serial 
import time 
from DecodePyZbar import decoderWrite, show, convertToBIT
from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre
import struct
# #from facture import Facture
# from Interface import Interface
# from tkinter import *


# Simple test pour vérifier que les fonctions fonctionnent bien
if __name__ == "__main__":

    ser = serial.Serial('COM6', 250000, timeout=1)

    dataArray = []
    counter = 0
    FORMAT = '<B'
    termination_line = 0
    stop_condition = 1
    compteur0 = 1
    lastLecture = 2
    compteurMax = 0

    while True:
        counter += 1
        data = ser.read(1)
        send = struct.unpack(FORMAT, data)[0]

        if lastLecture == 0:
            compteur0 += 1
        else:
            if compteur0 > compteurMax:
                compteurMax = compteur0
            compteur0 = 1

        #dataArray.append(data)
        if counter == 10000:
            print(dataArray)
            code = decoderWrite(dataArray)
            dataShow, sizeShow = convertToBIT(dataArray)
            show(dataShow, sizeShow)
            if code != []:
                for obj in code:
                    print('Type : ', obj.type)
                    print('Data : ', obj.data,'\n')
            dataArray = []
            counter = 0
            stop_condition = 0
        dataArray.append(send)
        lastLecture = send
        if stop_condition == termination_line:
            break
    print(compteurMax)

# root = Tk()
# app = Interface(root)
# root.title('Identification de code-barres')
# root.geometry('1000x300') 
# root.mainloop()
