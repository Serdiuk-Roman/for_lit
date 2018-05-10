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


import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import choice, randint


class Game:

    def __init__(self, size, window):
        self.window = window
        self.score = 0
        self.size = size
        self.field = [[0 for x in range(self.size)] for y in range(self.size)]
        self.random_coount = (1, 2)
        self.random_value = (4, 2, 2, 2, 2, 2, 2, 2, 2, 2)

        for i in range((self.size ** 2) // 8):
            row_index = randint(0, self.size - 1)
            cell_index = randint(0, self.size - 1)
            self.field[row_index][cell_index] = choice(self.random_value)

    def render(self):
        y_row = 2
        for row in self.field:
            str_row = '│'.join(str(cell).center(6) for cell in row)
            self.window.addstr(y_row, 1, str_row)
            y_row += 4

    def change_free_cell(self):
        while True:
            row_index = randint(0, self.size - 1)
            col_index = randint(0, self.size - 1)
            if self.field[row_index][col_index] == 0:
                self.field[row_index][col_index] = choice(self.random_value)
                return

    def move_left(self):
        for row in self.field:
            moved_el = [x for x in row if x != 0]
            for i in range(1, len(moved_el)):
                if moved_el[i] == moved_el[i - 1]:
                    moved_el[i - 1] *= 2
                    moved_el[i] = 0
                    self.score += moved_el[i - 1]
            moved_el = [x for x in moved_el if x != 0]
            delta_len = self.size - len(moved_el)
            if delta_len:
                moved_el.extend([0 for i in range(delta_len)])
            for i in range(self.size):
                row[i] = moved_el[i]

    def move_right(self):
        for row in self.field:
            moved_el = [x for x in row if x != 0]
            for i in range(-2, -(len(moved_el) + 1), -1):
                if moved_el[i] == moved_el[i + 1]:
                    moved_el[i + 1] *= 2
                    moved_el[i] = 0
                    self.score += moved_el[i + 1]
            moved_el = [x for x in moved_el if x != 0]
            delta_len = self.size - len(moved_el)
            if delta_len:
                update_row = [0 for i in range(delta_len)]
                update_row.extend(moved_el)
            else:
                update_row = moved_el
            for i in range(self.size):
                row[i] = update_row[i]

    def move_up(self):
        for i in range(self.size):
            row = [x[i] for x in self.field]
            moved_el = [x for x in row if x != 0]
            for j in range(1, len(moved_el)):
                if moved_el[j] == moved_el[j - 1]:
                    moved_el[j - 1] *= 2
                    moved_el[j] = 0
                    self.score += moved_el[j - 1]
            moved_el = [x for x in moved_el if x != 0]
            delta_len = self.size - len(moved_el)
            if delta_len:
                moved_el.extend([0 for i in range(delta_len)])
            for k in range(self.size):
                self.field[k][i] = moved_el[k]

    def move_down(self):
        for i in range(self.size):
            row = [x[i] for x in self.field]
            moved_el = [x for x in row if x != 0]
            for j in range(-2, -(len(moved_el) + 1), -1):
                if moved_el[j] == moved_el[j + 1]:
                    moved_el[j + 1] *= 2
                    moved_el[j] = 0
                    self.score += moved_el[j + 1]
            moved_el = [x for x in moved_el if x != 0]
            delta_len = self.size - len(moved_el)
            if delta_len:
                update_row = [0 for i in range(delta_len)]
                update_row.extend(moved_el)
            else:
                update_row = moved_el
            for k in range(self.size):
                self.field[k][i] = update_row[k]

    def has_moves(self):
        for row in self.field:
            if 0 in row:
                return True
            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    return True
        for i in range(self.size):
            row = [x[i] for x in self.field]
            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    return True
        return False

    def get_score(self):
        return self.score

    def get_field(self):
        return self.field
        # raise NotImplementedError


def main():
    size = input("Enter size (default = 4) > ")
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

        print("W, A, S, D - move")
        print("Q - exit")

        try:
            c = input("> ")
        except (EOFError, KeyboardInterrupt):
            break

        if c in ('a', 'A'):
            game.move_left()
            if game.has_moves():
                game.change_free_cell()
        elif c in ('d', 'D'):
            game.move_right()
            if game.has_moves():
                game.change_free_cell()
        elif c in ('w', 'W'):
            game.move_up()
            if game.has_moves():
                game.change_free_cell()
        elif c in ('s', 'S'):
            game.move_down()
            if game.has_moves():
                game.change_free_cell()
        elif c in ('q', 'Q'):
            break

    print("Bye!")


if __name__ == '__main__':
    # main()
    curses.initscr()
    window = curses.newwin(17, 29, 0, 0)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border(0)

    # info_window = curses.newwin(12, 12, 0, 30)
    # info_window.keypad(1)
    # info_window.border(0)
    # info_window.clear()


    game = Game(4, window)
    # info_window.addstr(0, 5, game.score)

    while True:
        window.clear()
        window.border(0)

        # window.addstr(0, 5, "Score")
        for i in range(1, 16):
            window.addstr(i, 7, "│")
            window.addstr(i, 14, "│")
            window.addstr(i, 21, "│")
            if i in [4, 8, 12]:
                window.addstr(i, 1, "────── ────── ────── ──────")

        game.render()
        event = window.getch()

        if event in (27, 81, 113):
            break
        elif event == KEY_LEFT:
            game.move_left()
            if game.has_moves():
                game.change_free_cell()
        elif event == KEY_RIGHT:
            game.move_right()
            if game.has_moves():
                game.change_free_cell()
        elif event == KEY_UP:
            game.move_up()
            if game.has_moves():
                game.change_free_cell()
        elif event == KEY_DOWN:
            game.move_down()
            if game.has_moves():
                game.change_free_cell()

    curses.endwin()
