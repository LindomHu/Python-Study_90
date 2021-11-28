# -*- coding: utf-8 -*-
# @Time : 2021/11/21 11:27
# @Author : huix
# @File : houyi.py
import self as self

from OldBoyStudy.NewStudy.Game.game import Game


class HouYi(Game):

    def __init__(self):
        # super.__init__(1000,200)
        self.defense = 100

    def houyi_fight(self, enemy_hp, enemy_power):
        """

        :param enemy_hp:
        :param enemy_power:
        :return:

        final_hp = self.hp + self.defense - enemy_power
        # final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我赢了")

        elif final_hp < enemy_final_hp:
            print("敌人赢了")

        else:
            raise Exception("没有平局！")
            # print("平局")
        """

# 优化代码
        while True:

            self.hp = self.hp + self.defense - enemy_power
            # final_hp = self.hp - enemy_power
            enemy_hp = enemy_hp - self.power
            print(self.hp)
            print(enemy_hp)

            if self.hp <= 0:
                print("敌人赢了")
                break

            elif enemy_hp <= 0:
                print("我赢了")
                break
hp = 800
power = 200
houyi = HouYi()
houyi.houyi_fight(hp,power)