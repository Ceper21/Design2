import pyzbar.pyzbar as pyzbar
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im

hauteur = 50

def convertToBytes(string01):
    liste = []
    for bit in string01:
        if str(bit) == '0':
            liste.append(0)
        if str(bit) == '1':
            liste.append(255)
        else:
            continue
    counter = len(liste)
    arrayBytes = bytes([i for i in liste])
    arrayBytes = arrayBytes*hauteur
    return(arrayBytes, counter)

def convertToBIT(string01):
    liste = []
    for bit in string01:
        if bit == 0:
            liste.append(255)
        if bit == 1:
            liste.append(0)
        else:
            continue
    counter = len(liste)
    arrayBytes = bytes([i for i in liste])
    #print('yoooooo', arrayBytes)
    arrayBytes = arrayBytes*hauteur
    return(arrayBytes, counter)

def show(im_code, largeur):
    code = np.array([int(i) for i in im_code]).reshape(hauteur, largeur)
    data = im.fromarray(code)
    data.show()

def decoder(stringin):
    # Trouver les code-barres dans l'image à partir de serial.print dans Arduino
    string, counter = convertToBytes(stringin)
    myTuple = (string, counter, hauteur)
    codes_trouves = pyzbar.decode(myTuple)
    return(codes_trouves)

def decoderWrite(stringin):
    # Trouver les code-barres dans l'image à partir de serial.write dans Arduino
    string, counter = convertToBIT(stringin)
    myTuple = (string, counter, hauteur)
    codes_trouves = pyzbar.decode(myTuple)
    return(codes_trouves)

#pour les tests (séquence de bits et non le signal)
def flipIt(stringin):
    stringout = []
    for i in stringin:
        if str(i) == '1':
            stringout.append(0)
        if str(i) == '0':
            stringout.append(1)
    return(stringout)



# code pour tester avec write

stringTest = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

stringTest = flipIt(stringTest)
stringC, counter = convertToBIT(stringTest)
print(stringC)
show(stringC, counter)
codes = decoderWrite(stringTest)
for obj in codes:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')

# code pour tester (version mise à jour)

# stringToFlip = '00000000000010101110110001001010011100010110000101001100101010100001011101001101100110011010111001000100101000000000000000'
# stringToFlip = '00000000000000010100011010010011010111101100010110111001001101010111001011100101110010100111010000101001110101000000000000000000'
# stringFlip = flipIt(stringToFlip)
# stringTest, counter = convertToBytes(stringFlip)
# show(stringTest, counter)
# codes = decoder(stringTest)
# for obj in codes:
#     print('Type : ', obj.type)
#     print('Data : ', obj.data,'\n')


# code pour tester version1 (n'est plus à jour)

# string = '00000000000010101110110001001010011100010110000101001100101010100001011101001101100110011010111001000100101000000000000000'
# stringNotFlip = flipIt(string)
# #print(stringNotFlip)
# string8, counter = convertToBytes(stringNotFlip)
# #print(string8)
# show(string8, counter)
# codes = decoder(stringNotFlip)
# for obj in codes:
#     print('Type : ', obj.type)
#     print('Data : ', obj.data,'\n')
