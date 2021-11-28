# -*- coding: utf-8 -*-
# @Time : 2021/11/21 10:33
# @Author : huix
# @File : 28脚本编写实战.py


class Game:
    hp = 1000
    power = 200

    def fight(self,enemy_hp,enemy_power):
        final_hp = self.hp - enemy_power
        enemy_finnal_hp = enemy_hp - self.power

        if final_hp > enemy_finnal_hp:
            print("我赢了")

        elif final_hp < enemy_finnal_hp:
            print("敌人赢了")

        else:
            print("平局")

# game = Game()
# game.fight(900,300)

class HouYi(Game):

    def __init__(self):
        # super.__init__(1000,200)
        self.defense = 100

    def houyi_fight(self, enemy_hp, enemy_power):

        final_hp = self.hp + self.defense - enemy_power
        # final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我赢了")

        elif final_hp < enemy_final_hp:
            print("敌人赢了")

        else:
            print("平局")

hp = 1000
power = 200
houyi = HouYi()
houyi.houyi_fight(hp,power)


