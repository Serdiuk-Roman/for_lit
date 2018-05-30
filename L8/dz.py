# from datetime import datetime


class StringCalculator:

    def add(self, number_str):
        number_str = number_str.replace(",", " ")
        number_str = number_str.replace("\n", " ")
        print(number_str)
        if "//" in number_str[:2]:
            number_str = number_str.replace("//", "")
            number_str = number_str.replace("#", " ")
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

        res = [
            int(x)
            for x in number_list
            if 0 < int(x) < 1000
        ]
        return sum(res)


if __name__ == "__main__":
    g = StringCalculator()
    g.add("5 3, 2")
