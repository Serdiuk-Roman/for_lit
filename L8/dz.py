# from datetime import datetime


class StringCalculator:

    def add(self, number_str):
        str_list = number_str.split()
        print(str_list)
        number_list = [int(x) for x in str_list]
        res = sum(number_list)
        return res


if __name__ == "__main__":
    g = StringCalculator()
    g.add("5 3, 2")
