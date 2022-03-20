from numpy import true_divide
import serial 
import time 
from DecodePyZbar import decoder
from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre
#from facture import Facture


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
