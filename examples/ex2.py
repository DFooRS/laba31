#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class DeskTable(Table):
    def square(self):
        return self.width * self.length


class ComputerTable(DeskTable):
    def square(self, monitor=0.0):
        return self.width * self.length - monitor


class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p


if __name__ == '__main__':
    t1 = Table(1.5, 1.8, 0.75)
    t2 = DeskTable(0.8, 0.6, 0.7)
    print(t2.square())
    t3 = ComputerTable(0.8, 0.6, 0.7)
    print(t3.square(0.3))
    t4 = KitchenTable(1.5, 2, 0.75, 6)