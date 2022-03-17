import matplotlib.pyplot as plt
import numpy as np

string = "11000010110001001100011"
b = bytearray(b'')
im_array = bytearray(b'')
for i in string:
    if i == '1':
        b.extend(b'\xff')
    if i == '0':
        b.extend(b'\x00')
for i in range(7):
    im_array.extend(b)

code = np.array([int(i) for i in im_array]).reshape(7, len(string))
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