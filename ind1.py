#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Triad:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def increase(self):
        self.a += 1
        self.b += 1
        self.c += 1


class Time(Triad):
    def __init__(self, hour, minute, second):
        super().__init__(hour, minute, second)

    def increase(self):
        self.c += 1
        if self.c >= 60:
            self.c -= 60
            self.b += 1
        if self.b >= 60:
            self.b -= 60
            self.a += 1

    def increase_seconds(self, n):
        self.c += n
        if self.c >= 60:
            self.c %= 60
            self.b += 1
        if self.b >= 60:
            self.b %= 60
            self.a += 1

    def increase_minutes(self, n):
        self.b += n
        if self.b >= 60:
            self.b %= 60
            self.a += 1


if __name__ == '__main__':
    time = Time(11, 20, 35)
    print(f"Время: {time.a}:{time.b}:{time.c}")

    time.increase()
    print(f"Вряме через секунду: {time.a}:{time.b}:{time.c}")

    time.increase_seconds(80)
    print(f"Время ещё через 80 секунд: {time.a}:{time.b}:{time.c}")

    time.increase_minutes(30)
    print(f"Время ещё через полчаса: {time.a}:{time.b}:{time.c}")
