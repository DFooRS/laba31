#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Unit:
    def __init__(self, number, name):
        self.__id = number
        self.__team = name

    @property
    def id(self):
        return self.__id

    @property
    def team(self):
        return self.__team


class Soldier(Unit):
    def follow_hero(self, hero):
        print(f"Солдат №{self.id} следует за героем №{hero.id}")


class Hero(Unit):
    def __init__(self, number):
        super().__init__(number, "Hero")
        self.level = 1

    def increase_level(self):
        self.level += 1


if __name__ == '__main__':
    team1_hero = Hero(1)
    team2_hero = Hero(2)

    soldiers_1 = []
    soldiers_2 = []

    for i in range(10):
        team = random.choice([1, 2])
        soldier = Soldier(i + 1, team)

        if team == 1:
            soldiers_1.append(soldier)
        else:
            soldiers_2.append(soldier)

    print(f"Количество солдат в команде 1: {len(soldiers_1)}")
    print(f"Количество солдат в команде 2: {len(soldiers_2)}")

    if len(soldiers_1) > len(soldiers_2):
        team1_hero.increase_level()
    elif len(soldiers_2) > len(soldiers_1):
        team2_hero.increase_level()

    print(f"Уровень героя 1 команды: {team1_hero.level}")
    print(f"Уровень героя 2 команды: {team2_hero.level}")

    soldiers_1[1].follow_hero(team1_hero)
