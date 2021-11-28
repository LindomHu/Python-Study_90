# -*- coding: utf-8 -*-
# @Time : 2021/11/21 11:26
# @Author : huix
# @File : game.py


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