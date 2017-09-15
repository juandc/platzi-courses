#!/usr/bin/env python
# -*-coding:utf-8-*-
from time import sleep
import random

class Element:
    name = ''
    win = []
    win_verbs = []
    lost = []
    lost_verbs = []

    def name(self):
        return '{}'.format(self.name)


class Rock(Element):
    def __init__(self):
        self.name = 'piedra'
        self.win = [Scissors, Lizard]
        self.win_verbs = ['aplasta', 'aplasta']
        self.lost = [Paper, Spock]
        self.lost_verbs = ['tapa', 'vaporiza']


class Paper(Element):
    def __init__(self):
        self.name = 'papel'
        self.win = [Rock, Spock]
        self.win_verbs = ['tapa', 'desautoriza']
        self.lost = [Lizard, Scissors]
        self.lost_verbs = ['devora', 'corta']


class Scissors(Element):
    def __init__(self):
        self.name = 'tijeras'
        self.win = [Paper, Lizard]
        self.win_verbs = ['corta', 'decapita']
        self.lost = [Rock, Spock]
        self.lost_verbs = ['aplasta', 'rompe']


class Lizard(Element):
    def __init__(self):
        self.name = 'lagarto'
        self.win = [Spock, Paper]
        self.win_verbs = ['envenena', 'devora']
        self.lost = [Rock, Scissors]
        self.lost_verbs = ['aplasta', 'decapita']


class Spock(Element):
    def __init__(self):
        self.name = 'spock'
        self.win = [Scissors, Rock]
        self.win_verbs = ['rompe', 'vaporiza']
        self.lost = [Lizard, Paper]
        self.lost_verbs = ['envenena', 'desautoriza']


def compare(player, pc):
    print (player, '-', pc)
    piedra = Rock()
    papel = Paper()
    tijeras = Scissors()
    lagarto = Lizard()
    spock = Spock()
    options_list = [piedra, papel, tijeras, lagarto, spock]
    player_sel = None
    pc_sel = None

    for i in options_list:
        if player == i.name:
            player_sel = i
        if pc == i.name:
            pc_sel = i

    if player_sel == pc_sel:
        print(("\nEmpate.\n{}").format(sus))
    else:
        for index, c in enumerate(player_sel.win):
            if type(pc_sel) == c:
                print(("{}\nGanaste, {} {} {}\n{}").format(
                sus,player_sel.name,player_sel.win_verbs[index],pc_sel.name, sus))
        for index, c in enumerate(player_sel.lost):
            if type(pc_sel) == c:
                print(("{}\nPerdiste, {} {} {}\n{}").format(
                sus,pc_sel.name,player_sel.lost_verbs[index],player_sel.name, sus))


if __name__ == "__main__":
    sus = "*" * 35
    inputs = ['piedra', 'papel', 'tijeras', 'lagarto', 'spock']

    while True:
        player = input("""piedra, papel, tijera, lagarto, spock,
'salir' si quieres terminar: """)

        if player != 'salir' and player not in inputs:
            print ("No hagas trampa!, ingresa una opción valida")
            continue

        if player == 'salir':
            exit()

        pc = random.choice(inputs)
        sleep(0.5)
        compare(player, pc)
