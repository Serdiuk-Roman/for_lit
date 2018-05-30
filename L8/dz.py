# from datetime import datetime


class StringCalculator:

    def add(self, number_str):
        print()
        print(number_str)
        number_str = number_str.replace(",", " ")
        number_str = number_str.replace("\n", " ")
        if "//" in number_str[:2]:
            separ = ""
            number_str = number_str.replace("//", "")
            for char in number_str:
                if char.isdigit():
                    break
                else:
                    separ = separ + char
            print(separ)
            number_str = number_str.replace(separ, " ")
            print(number_str)
        number_list = number_str.split()
        if "-" in number_str:
            negatives = [
                x
                for x in number_list
                if "-" in x
            ]
            return "отрицательные числа запрещены: {}".format(
                ",".join(negatives)
            )
        print(number_list)
        res = [
            char
            for char in number_list
            if len(char) > 0
        ]
        res = map(int, number_list)
        return sum(res)


if __name__ == "__main__":
    g = StringCalculator()
    g.add("5 3, 2")
    g.add("5 3 2")
    g.add("")
    g.add("1")
    g.add("10,20")
    g.add("1\n2")
    g.add("1\n2,3\n4")
    g.add("-1,2,-3")
    g.add("1000,2,3000")
    g.add("//#\n1#2")
    g.add("//###\n1###2")
