#!/usr/bin/env python
import struct

class Conversor: 

    def __init__(self):
        pass

    def double_to_decimal(self, number: str):

        if number[1:12] == '0'*11: 
            if number[12:] == '0'*52: 
                return 0
            else: 
                # Subnormal numbers
                x = 0
                for i in range(12,64):
                    if number[i] == '0':
                        x += 1
                    else: 
                        break  
                m = sum([int(number[i+12])*2**(-i) for i in range(11)])
                return m*2**(x+1-1023)
        elif number[1:12] == '1'*11: 
            if number[12:] == '0'*52:
                # Infinite numbers 
                if number[0] == '0': 
                    return 'Inf'
                else: 
                    return '-Inf'
            else: 
                return 'NaN' 
        else: 
            s = int(number[0])
            c = sum([int(number[i+1])*2**(10-i) for i in range(11)])
            m = sum([int(number[i+12])*2**(-i-1) for i in range(11)])

        return (-1)**s*2**(c - 1023)*(1 + m)

    def decimal_to_double(self, num: float):

        s = struct.pack('!d', num) # packs the num to the decimal format
        s = struct.unpack('!Q', s)[0] # unpacks in long integer format. 
        s = bin(s) # converts to binary form.
        s = s[2:].zfill(64) # fills with zeros until reaches length 64.
        return s[0] + ' ' + s[1:12] + ' ' + s[12:]

if __name__ == '__main__': 

    exer2 = ['1100000010101001001100000000000000000000000000000000000000000000',
    '0011111111110101001100000000000000000000000000000000000000000000',
    '0000000000000101001100000000000000000000000000000000000000000000',
    '1111111111110000000000000000000000000000000000000000000000000000',
    '1111111111110000000000000000000000000000000000000000000000001111']

    exer6 = ['1100000010101001001100000000000000000000000000000000000000000001',
    '0011111111110101001100000000000000000000000000000000000000000001',
    '0000000000000101001100000000000000000000000000000000000000000001',
    '1111111111110000000000000000000000000000000000000000000000000001',
    '1111111111110000000000000000000000000000000000000000000000010000']

    convert = Conversor()
    for i in range(5): 
        print("Exercise {}: {}".format(i+1, convert.double_to_decimal(exer2[i])))
    for i in range(5): 
        print("Exercise 6, {}: {}".format(i+1, convert.double_to_decimal(exer6[i])))

    exer3 = [1/4, 1/3, 2/3, 0.9, 71/127, 125/252]
    for i in range(6): 
        print("Exercise {}: {}".format(i+1, convert.decimal_to_double(exer3[i])))
        
    print(convert.decimal_to_double(7*(1/7)))
    print(convert.decimal_to_double(1))

    print('-----------------------------')

    print(convert.decimal_to_double(8.8))
    print(convert.decimal_to_double(7.8))
    print(convert.decimal_to_double(8.8-7.8))

