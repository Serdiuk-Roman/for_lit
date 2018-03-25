#!/usr/bin/python3
# -*- coding: utf-8 -*-


import re


def araic_to_roman(numb):
    arab = [1000, 900, 500, 400, 100, 90,
            50, 40, 10, 9, 5, 4, 1]
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC',
             'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    index = 0
    res = ""
    while True and index < len(arab):
        if numb >= arab[index]:
            res = res + roman[index]
            numb -= arab[index]
        else:
            index += 1
    if valid_roman(res):
        print("\t{}".format(res))
    else:
        print("Error")


def roman_to_arabic(numb):
    roman = ['CM', 'M', 'CD', 'D', 'XC', 'C',
             'XL', 'L', 'IX', 'X', 'IV', 'V', 'I']
    arab = [900, 1000, 400, 500, 90, 100,
            40, 50, 9, 10, 4, 5, 1]
    index = 0
    res = 0
    while True and index < len(roman):
        if roman[index] in numb:
            res += arab[index]
            numb = numb.replace(roman[index], '', 1)
        else:
            index += 1
    print("\t{}".format(res))


def valid_roman(numb):
    tpl = '^(M{0,3})(D?C{0,3}|C[DM])(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$'
    if re.match(tpl, numb) is not None:
        return True
    else:
        return False


def test_roman_num():
    roman_to_arabic('I')  # 1
    roman_to_arabic('II')  # 2
    roman_to_arabic('III')  # 3
    roman_to_arabic('IV')  # 4
    roman_to_arabic('V')  # 5
    roman_to_arabic('VI')  # 6
    roman_to_arabic('VII')  # 7
    roman_to_arabic('VIII')  # 8
    roman_to_arabic('IX')  # 9
    roman_to_arabic('X')  # 10
    roman_to_arabic('XXXI')  # 31
    roman_to_arabic('XLVI')  # 46
    roman_to_arabic('XCIX')  # 99
    roman_to_arabic('DLXXXIII')  # 583
    roman_to_arabic('DCCCLXXXVIII')  # 888
    roman_to_arabic('MDCLXVIII')  # 1668
    roman_to_arabic('MCMLXXXIX')  # 1989
    roman_to_arabic('MMX')  # 2010
    roman_to_arabic('MMXI')  # 2011
    roman_to_arabic('MMXII')  # 2012
    roman_to_arabic('MMMCMXCIX')  # 3999


def main():
    print("""Введіть число від 1 до 3999, римськими або арабськими,
або натисніть клавішу 'Enter', щоб закіничити програму""")
    while True:
        elem = (input("-->\t")).upper()
        if not elem:
            break
        elif elem.isnumeric() and 0 < int(elem) < 4000:
            araic_to_roman(int(elem))
        elif valid_roman(elem):
            roman_to_arabic(elem)
        elif elem == "TEST":
            test_roman_num()
        else:
            print("Виконайте початкові умови")


if __name__ == '__main__':
    main()
