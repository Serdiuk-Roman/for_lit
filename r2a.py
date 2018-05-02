#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""The converter uses an example of
a task about the smallest amount of coins to hand over."""


import re


def araic_to_roman(numb):
    """Return a string in the form of Roman numerals"""
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
        return res
    else:
        print("Error")


def roman_to_arabic(numb):
    """Return the number"""
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
    return res


def valid_roman(numb):
    """Checking makes a regular expression copied from wikipedia"""
    tpl = '^(M{0,3})(D?C{0,3}|C[DM])(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$'
    if re.match(tpl, numb) is not None:
        return True
    else:
        return False


def test_num():
    """Checking converters in the forward and reverse direction"""
    print("Roman to arabic")
    roman = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX',
             'X', 'XXXI', 'XLVI', 'XCIX', 'DLXXXIII', 'DCCCLXXXVIII',
             'MDCLXVIII', 'MCMLXXXIX', 'MMX', 'MMMCCCXXXIII', 'MMMCMXCIX']
    arab = [1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 31, 46, 99, 583, 888,
            1668, 1989, 2010, 3333, 3999]
    for i in range(len(roman)):
        answer = roman_to_arabic(roman[i])
        equal = roman_to_arabic(roman[i]) == arab[i]
        print(roman[i], "=", answer, "is", equal)
    print("\nArabic to Roman")
    for i in range(len(arab)):
        answer = araic_to_roman(arab[i])
        equal = araic_to_roman(arab[i]) == roman[i]
        print(arab[i], "=", answer, "is", equal)


def main():
    """The main function, displays a dialogue with the user
and the results of work"""
    print("""Enter a number from 1 to 3999, Roman or Arabic,
enter 'test' to launch a simple test,
or press the 'Enter' key to close the program""")
    while True:
        elem = (input("<:\t")).strip()
        if not elem:
            break
        elif elem.isnumeric() and 0 < int(elem) < 4000:
            res = araic_to_roman(int(elem))
            print("-->\t{}".format(res))
        elif valid_roman(elem.upper()):
            res = roman_to_arabic(elem.upper())
            print("-->\t{}".format(res))
        elif elem == "TEST":
            test_num()
        else:
            print("Follow the initial conditions")


if __name__ == '__main__':
    main()
