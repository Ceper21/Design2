import pyzbar.pyzbar as pyzbar
import matplotlib.pyplot as plt
import numpy as np

def convertToBytes(string01):
    b = bytearray(b'')
    im_array = bytearray(b'')
    for i in string01:
        if i == '1':
            b.extend(b'\x00')
        if i == '0':
            b.extend(b'\xff')
    for i in range(50):
        im_array.extend(b)
    return(im_array)


def show(im_code, string01):
    code = np.array([int(i) for i in im_code]).reshape(50, len(string01))
    plt.imshow(code, 'gray')
    plt.show()

def decode(tuple):
    # Trouver les code-barres dans l'image
    codes_trouves = pyzbar.decode(tuple)
    return(codes_trouves)

#string = "010"+"011101100011010110001010111101111010010011"+"01010"+"111001010010001001110111010010111001000010"+"010"
string = "0000000000000000000000000000000001100110000001111001100001111000011000011000011110011111111001100110000001111001111000000110011001100110011000000001100000011000011000011000000111111001100001111000011110011111100001100110011000000000000000000000000"

string8 = convertToBytes(string)
#print(string8)
show(string8, string)
myTuple = (string8, 0, 0)
codes = decode(myTuple)
for obj in codes:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')
