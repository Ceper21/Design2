import pyzbar.pyzbar as pyzbar
import matplotlib.pyplot as plt
import numpy as np

hauteur = 50

def convertToBytes(string01):
    liste = []
    for bit in string01:
        if bit == '0':
            liste.append(0)
        if bit == '1':
            liste.append(255)
    counter = len(liste)
    arrayBytes = bytes([i for i in liste])
    arrayBytes = arrayBytes*hauteur
    return(arrayBytes, counter)

def convertToBIT(string01):
    liste = []
    for bit in string01:
        if bit == b'\x00':
            liste.append(0)
        if bit == b'\x01':
            liste.append(255)
    counter = len(liste)
    arrayBytes = bytes([i for i in liste])
    arrayBytes = arrayBytes*hauteur
    return(arrayBytes, counter)

def show(im_code, string01):
    code = np.array([int(i) for i in im_code]).reshape(hauteur, len(string01))
    plt.imshow(code, 'gray')
    plt.show()

def decoder(stringin):
    # Trouver les code-barres dans l'image à partir de serial.print dans Arduino
    string = convertToBytes(stringin)
    myTuple = (string, len(stringin), hauteur)
    codes_trouves = pyzbar.decode(myTuple)
    return(codes_trouves)

def decoderWrite(stringin):
    # Trouver les code-barres dans l'image à partir de serial.write dans Arduino
    string = convertToBIT(stringin)
    myTuple = (string, len(stringin), hauteur)
    codes_trouves = pyzbar.decode(myTuple)
    return(codes_trouves)

#pour les tests (séquence de bits et non le signal)
def flipIt(stringin):
    stringout = ''
    for i in stringin:
        if i == '1':
            stringout += '0'
        if i == '0':
            stringout += '1'
    return(stringout)


# code pour tester (version mise à jour)

#stringToFlip = '00000000000010101110110001001010011100010110000101001100101010100001011101001101100110011010111001000100101000000000000000'
# stringToFlip = '00000000000000010100011010010011010111101100010110111001001101010111001011100101110010100111010000101001110101000000000000000000'
# stringTest = flipIt(stringToFlip)
# codes = decoder(stringTest)
# for obj in codes:
#     print('Type : ', obj.type)
#     print('Data : ', obj.data,'\n')


# code pour tester version1 (n'est plus à jour)

# string = '00000000000010101110110001001010011100010110000101001100101010100001011101001101100110011010111001000100101000000000000000'
# stringNotFlip = flipIt(string)
# string8, counter = convertToBytes(stringNotFlip)
# print(type(string8))
# print(type(len(string)))
# print(type(hauteur))
# show(string8, string)
# myTuple = (string8, len(string), hauteur)
# codes = decoder(myTuple)
# for obj in codes:
#     print('Type : ', obj.type)
#     print('Data : ', obj.data,'\n')
