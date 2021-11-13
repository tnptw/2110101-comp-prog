# Prog-07: EAN-13 Barcode

import math
import matplotlib.pyplot as plt
#-------------------------------------------------
def show_barcode(digits, ean13_code): 
    x = [[int(e) for e in ean13_code]]
    plt.axis('off')      
    plt.imshow(x, aspect='auto', cmap='binary')
    plt.title(digits)     
    plt.show()   
#-------------------------------------------------
def test1():
    digits = input('Enter a 13-digit number: ')  
    codes = encode_EAN13(digits)  
    if codes == '':   
        print(digits, 'is not an EAN-13 number.')
    else:
        decoded_digits = decode_EAN13(codes)
        if decoded_digits == digits:
            show_barcode(digits, codes)
        else:
            print('Error in decoding.')
#-------------------------------------------------
L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', \
           '0110001', '0101111', '0111011', '0110111', '0001011']
G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', \
           '0111001', '0000101', '0010001', '0001001', '0010111']
R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', \
           '1001110', '1010000', '1000100', '1001000', '1110100']

#=================================================

def codes_of(digits, patterns):
    codes = ''
    for i in range(len(patterns)) :
        if patterns[i] == 'L': codes += str(L_codes[int(digits[i])])
        elif patterns[i] == 'G': codes += str(G_codes[int(digits[i])])
        elif patterns[i] == 'R': codes += str(R_codes[int(digits[i])])
    return codes

def digits_of(codes):
    temp = []; c = 0
    for i in range(len(codes)//7):
        temp += [codes[i+c:i+c+7]]
        c += 6
    digits = ''
    for i in temp:
        if i in L_codes : digits += str(L_codes.index(i))
        elif i in G_codes : digits += str(G_codes.index(i))
        elif i in R_codes : digits += str(R_codes.index(i))
        else : return ''
    return digits

def patterns_of(codes):
    temp = []; c = 0
    for i in range(len(codes)//7):
        temp += [codes[i+c:i+c+7]]
        c += 6
    patterns = ''
    for i in temp:
        if i in L_codes : patterns += 'L'
        elif i in G_codes : patterns += 'G'
        elif i in R_codes : patterns += 'R'
        else : return ''
    return patterns

def check_digit(digits):
    A = [e for e in digits]; B = []
    for i in range(len(A)):
        if i%2 == 0: B.append('1')
        else : B.append('3')
    sum = 0
    for i in range(len(A)): sum += int(A[i])*int(B[i])
    check_digit  = 10*(int(sum/10)+(sum%10 > 0)) - sum
    return str(check_digit)

def encode_EAN13(digits):
    group_1 = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', \
        'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL']
    for i in digits:
        if i not in '1234567890': return ''
    if len(digits) != 13: return ''
    if digits[-1] != check_digit(digits[:-1]): return ''
    else:
        encode = '101'; c = 0
        for i in digits[1:7]:
            encode += codes_of(i,group_1[int(digits[0])][c])
            c += 1
        encode += '01010'
        for i in digits[7:]: encode += codes_of(i,'R')
        encode += '101'
        return encode

def decode_EAN13(codes):
    codes_1 = codes[3:45]; codes_2 = codes[50:-3]
    group_1 = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', \
        'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL']
    if len(codes) != 95: return '' 
    elif digits_of(codes_1+codes_2) == '':
        codes_rev = codes[::-1]; codes_1 = codes_rev[3:45]; codes_2 = codes_rev[50:-3]
        if digits_of((codes_1+codes_2)) != '':
            digits = str(group_1.index(patterns_of(codes_1)))
            temp = []; c = 0
            for i in range((len(codes_1))//7):
                temp += [codes_1[i+c:i+c+7]]
                c += 6
            for i in temp: digits += digits_of(i)
            temp = []; c = 0
            for i in range((len(codes_2))//7):
                temp += [codes_2[i+c:i+c+7]]
                c += 6
            for i in temp: digits += digits_of(i)
            return digits
        else: return ''
    elif digits_of((codes_1+codes_2)) != '':
        if digits_of((codes_1+codes_2))[-1] != check_digit(str(group_1.index(patterns_of(codes_1)))\
            +digits_of(codes_1+codes_2)[:-1]): return ''
        else:
            digits = str(group_1.index(patterns_of(codes_1)))
            temp = []; c = 0
            for i in range((len(codes_1))//7):
                temp += [codes_1[i+c:i+c+7]]
                c += 6
            for i in temp: digits += digits_of(i)
            temp = []; c = 0
            for i in range((len(codes_2))//7):
                temp += [codes_2[i+c:i+c+7]]
                c += 6
            for i in temp: digits += digits_of(i)
            return digits

#-------------------------------------------------
test1()