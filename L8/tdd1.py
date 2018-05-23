from datetime import datetime


class Greeter:

    def greet(self, name):
        hour = int(datetime.strftime(datetime.now(), "%H"))
        name = name.strip().capitalize()
        if 6 <= hour < 12:
            return "Доброе утро {}".format(name)
        elif 18 <= hour < 22:
            return "Добрый вечер {}".format(name)
        elif 22 <= hour < 24:
            return "Доброй ночи {}".format(name)
        elif 0 <= hour < 6:
            return "Доброй ночи {}".format(name)
        return "Привет {}".format(name)


if __name__ == "__main__":
    g = Greeter()
    g.greet("A")
