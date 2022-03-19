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

    for i in range(50):
        photodiode_value = ser.readline()    #read a byte
        if photodiode_value:
            string = photodiode_value.decode()  #Converting the byte string to a unicode string
            real_string = string.strip()
            print(real_string)
    
    

    
    ser.close()

    #facture = Facture.facture()
    #dico = base_de_donnees(dico)
    #Code = decodage(binaire)
    #print(Code)
    #print(verificationPresence(Code, dico))
    #x = dico["000000000000"]
    #print(x)
