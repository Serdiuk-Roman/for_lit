#!/usr/bin/python3
# -*- coding: utf-8 -*-


ROMAN_NUMBERS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


def roman_to_arabic (numb):
    i = 0
    res = 0
    roman = ['CM', 'M', 'CD', 'D', 'XC', 'C', 'XL', 'L', 'IX', 'X', 'IV', 'V', 'I']
    arab =  [ 900, 1000, 400, 500,  90,  100,  40,   50,   9,   10,   4,   5,   1 ]
    while True:
        try:
            # print("i=", i,"\tr=", roman[i], "\tnumb=", numb, "\tres=", res)
            if roman[i] in numb:
                res += arab[i]
                numb = numb.replace(roman[i], '', 1)
            else:
                i += 1
        except:
            break
    return res


def valid_roman (numb):
    
    for i in numb:
        if i not in ROMAN_NUMBERS:
            return False
    return True


def main ():
    while True:
        elem = (input("Введіть ціле число від 1 до 3999 римськими числами\n\t")).upper()
        if not elem:
            break
        if valid_roman(elem):
            res = roman_to_arabic(elem)
            print("\t{}".format(res))
        else:
            print("Римські числа:", *ROMAN_NUMBERS)
        


if __name__ == '__main__':
    main()