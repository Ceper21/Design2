import serial 
import time 
from DecodePyZbar import decoder
from IdentificateurCodeBarre import base_de_donnees, decodage, verificationPresence, validationDernierChiffre
from facture import Facture


#binaire = "1111111001100011"+"010"+ 6*"0001101" + "01010" + 6*"0001101" + "010"+ "000011010" # à enlever plus tard (test)

#dico = {}

# Simple test pour vérifier que les fonctions fonctionnent bien
if __name__ == "__main__":

    ser = serial.Serial('COM5', 9600, timeout=1)
    time.sleep(2)

    data = ""
    while(ser):
        photodiode_value = ser.readline()    #read a byte
        if photodiode_value:
            string = photodiode_value.decode()  #Converting the byte string to a unicode string
            real_string = string.strip()
            data += real_string
            code = decoder(data)
            if code != []:
                for obj in code:
                    print('Type : ', obj.type)
                    print('Data : ', obj.data,'\n')
                data = ''



    
    ser.close()

    #facture = Facture.facture()
    #dico = base_de_donnees(dico)
    #Code = decodage(binaire)
    #print(Code)
    #print(verificationPresence(Code, dico))
    #x = dico["000000000000"]
    #print(x)
