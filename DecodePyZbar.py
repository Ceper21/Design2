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
    arrayBytes = bytes([i for i in liste])
    arrayBytes = arrayBytes*hauteur
    return(arrayBytes)

def show(im_code, string01):
    code = np.array([int(i) for i in im_code]).reshape(hauteur, len(string01))
    plt.imshow(code, 'gray')
    plt.show()

def decoder(tuple):
    # Trouver les code-barres dans l'image
    codes_trouves = pyzbar.decode(tuple)
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


#string = "0000000000000000000000000000000001100110000001111001100001111000011000011000011110011111111001100110000001111001111000000110011001100110011000000001100000011000011000011000000111111001100001111000011110011111100001100110011000000000000000000000000"
#string = '10101101110110001000101101000110100011000110101111010101011001101100110111001011001101100110101'
string = '00000000000010101110110001001010011100010110000101001100101010100001011101001101100110011010111001000100101000000000000000'

stringNotFlip = flipIt(string)
string8 = convertToBytes(stringNotFlip)
print(type(string8))
print(type(len(string)))
print(type(hauteur))
show(string8, string)
myTuple = (string8, len(string), hauteur)
codes = decoder(myTuple)
for obj in codes:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')
