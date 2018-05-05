#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Сдвиг влево:
    Числа не должны двигаться, если уже занимают правильную позицию.
    Числа не должны двигаться, если нет свободных ячеек в ряду.
    Все числа должны сдвигаться влево, если самая левая ячейка пустая.
    Если ячейка свободна - все числа справа от неё сдвигаются влево.

Сдвиг вправо/верх/вниз по аналогии со сдвигом влево.

Объединение ячеек:
    Любые два одинаковых числа, находящихся друг возле друга, должны
    быть объединены в одну ячейку значение которой - сумма двух этих чисел.
    Любые два одинаковых числа, разделённых пустотой, должны быть
    объединены в одну ячейку значение которой - сумма двух этих чисел.

Подсчёт очков:
    Игра начинается с 0 очков.
    Количество очков должно увеличиваться на значение объединённых ячеек.

Конец игры:
    Конец игры наступает когда все ячейки уже заняты
    и невозможно добавить новых чисел.

Игровое поле:
    Игровое поле должно отображаться в виде сетки 4x4.
    В начале игры поле пустое,
    за исключением двух случайно выбранных ячеек, равных 2.
    После каждого сдвига две случайно выбранные
    пустые ячейки заполняются числами 2 или 4.
"""


from random import choice, randint


class Game:

    def __init__(self, size):
        self.size = size
        self.field = [[0 for x in range(self.size)] for y in range(self.size)]
        self.random_coount = (1, 2)
        self.random_value = (4, 2, 2, 2, 2, 2, 2, 2, 2, 2)

        for i in range((self.size ** 2) // 8):
            row_index = randint(0, self.size - 1)
            cell_index = randint(0, self.size - 1)
            self.field[row_index][cell_index] = choice(self.random_value)

    def change_free_cell(self):
        while True:
            row_index = randint(0, self.size - 1)
            column_index = randint(0, self.size - 1)
            if self.field[row_index][column_index] == 0:
                self.field[row_index][column_index] = choice(self.random_value)
                return

    def move_left(self):
        for row in self.field:
            for cell_index in range(1, len(row)):
                if row[cell_index] == row[cell_index - 1]:
                    row[cell_index - 1] *= 2
                    row[cell_index] = 0
        # raise NotImplementedError

    def move_right(self):
        pass
        # raise NotImplementedError

    def move_up(self):
        pass
        # raise NotImplementedError

    def move_down(self):
        pass
        # raise NotImplementedError

    def has_moves(self):
        for row in self.field:
            if 0 in row:
                return True
        return False
        # raise NotImplementedError

    def get_score(self):
        pass
        # raise NotImplementedError

    def get_field(self):
        return self.field
        # raise NotImplementedError


def main():
    size = input("Enter size(default=4)> ")
    if size == "":
        size = 4
    else:
        size = int(size)
    game = Game(size)

    while True:
        field = game.get_field()
        cell_width = len(str(max(
            cell
            for row in field
            for cell in row
        )))

        # print("\033[H\033[J", end="")
        print("Score: ", game.get_score())
        print('\n'.join(
            ' '.join(
                str(cell).rjust(cell_width)
                for cell in row
            )
            for row in field
        ))

        if not game.has_moves():
            print("No available moves left, game over.")
            break

        print("L, R, U, D - move")
        print("Q - exit")

        try:
            c = input("> ")
        except (EOFError, KeyboardInterrupt):
            break

        if c in ('l', 'L'):
            game.move_left()
            if game.has_moves():
                game.change_free_cell()
        elif c in ('r', 'R'):
            game.move_right()
        elif c in ('u', 'U'):
            game.move_up()
        elif c in ('d', 'D'):
            game.move_down()
        elif c in ('q', 'Q'):
            break

    print("Bye!")


if __name__ == '__main__':
    main()
