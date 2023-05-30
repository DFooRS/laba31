#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import math


class Container(ABC):
    @abstractmethod
    def sort(self):
        pass

    @abstractmethod
    def foreach(self):
        pass


class Bubble(Container):
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i, item in enumerate(self.data):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        return self.data

    def foreach(self):
        for i, item in enumerate(self.data):
            self.data[i] = math.sqrt(item)
        return self.data


class Choice(Container):
    def __init__(self, data):
        self.data = data

    def sort(self):
        for i, item in enumerate(self.data):
            mn = min(range(i, len(self.data)), key=self.data.__getitem__)
            self.data[i], self.data[mn] = self.data[mn], item
        return self.data

    def foreach(self):
        for i, item in enumerate(self.data):
            self.data[i] = math.log(item)
        return self.data


def print_container(container):
    print(f"Исходные данные: {container.data}")
    print(f"Сортированные данные: {container.sort()}")
    print(f"Обработанный список: {container.foreach()}")


if __name__ == '__main__':
    first_container = Bubble([9, 54, 7, 2, 1])
    print_container(first_container)

    second_container = Choice([22, 6, 7, 3, 8])
    print_container(second_container)
