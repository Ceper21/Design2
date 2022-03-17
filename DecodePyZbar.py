import matplotlib.pyplot as plt
import numpy as np

#string = "010"+"011101100011010110001010111101111010010011"+"01010"+"111001010010001001110111010010111001000010"+"010"
string = "10100011010010011001001100011010001101000110101010110011011011001001110111001010000101000010101"
b = bytearray(b'')
im_array = bytearray(b'')
for i in string:
    if i == '1':
        b.extend(b'\xff')
    if i == '0':
        b.extend(b'\x00')
for i in range(20):
    im_array.extend(b)

code = np.array([int(i) for i in im_array]).reshape(20, len(string))
plt.imshow(code, 'gray')
plt.show()

# bit = "1111111001100011"+"010"+ 6*"0001101" + "01010" + 6*"0001101" + "010"+ "000011010"
# im_array = np.array([])

# for i in 

# for i in bit:
#     im_array.append()

# im_array = np.array([int(i) for i in bit])
# bite_array = bytearray((bit))

# print(bite_array)