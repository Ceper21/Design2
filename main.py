import serial 
import time 
import struct
import tkinter as tk
from DecodePyZbar import decoderWrite, show, convertToBIT
from IdentificateurCodeBarre import Dico
from facture import Facture
from Interface import Interface


if __name__ == "__main__":

    dico = Dico()
    dico.initDico()
    facture = Facture()
    root = tk.Tk()
    app = Interface(root, facture, dico)
    root.title('Identification de code-barres')
    root.geometry('1000x500') 
    root.mainloop()

    # ser = serial.Serial('/dev/cu.usbmodem14201', 2000000, timeout=1)

    # dataArray = []
    # FORMAT = '<B'

    # while True:
    #     data = ser.read(1)
    #     send = struct.unpack(FORMAT, data)[0]

    #     if send == 2:
    #         code = decoderWrite(dataArray)
    #         dataShow, sizeShow = convertToBIT(dataArray) # a conserver pour les tests seulement (sert à afficher l'image du code bar)
    #         show(dataShow, sizeShow)                     # meme commentaire qu'au-dessus
    #         if code != []:
    #             for obj in code:
    #                 print('Code reçu : ', obj.data,'\n')
    #                 root.AjouterElement(obj)
    #         dataArray = []
    #         time.sleep(4) # fait attendre le programme pendant 4 secondes (le temps de mettre un autre produit)
    #     dataArray.append(send)
