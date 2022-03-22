import serial 
import time 
import struct
from DecodePyZbar import decoderWrite, show, convertToBIT
from IdentificateurCodeBarre import Dico
from facture import Facture
from Interface import Interface


if __name__ == "__main__":

    ser = serial.Serial('COM6', 250000, timeout=1)

    dataArray = []
    FORMAT = '<B'
    facture = Facture.facture()
    dico = Dico.dico()
    dico.initDico()

    while True:
        data = ser.read(1)
        send = struct.unpack(FORMAT, data)[0]

        if send == 2:
            print(dataArray)
            code = decoderWrite(dataArray)
            dataShow, sizeShow = convertToBIT(dataArray) # a conserver pour les tests seulement (sert à afficher l'image du code bar)
            show(dataShow, sizeShow)                     # meme commentaire qu'au-dessus
            if code != []:
                for obj in code:
                    print('Code reçu : ', obj.data,'\n')
                    if dico.verificationPresence(obj) == True:
                        facture.updateFacture(dico, obj)
            dataArray = []
            time.sleep(4) # fait attendre le programme pendant 4 secondes (le temps de mettre un autre produit)
        dataArray.append(send)

# root = Tk()
# app = Interface(root)
# root.title('Identification de code-barres')
# root.geometry('1000x300') 
# root.mainloop()
