#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import option
import os


# 显示管理类 ，根据坐标显示一个n*n的矩阵
class Displayer:
    # init方法
    def __init__(self):
        # 装坐标点的列表 (x,y)元组
        self.__list = []

    # 导入需要显示的坐标点数据
    def extend_points(self, point_list):
        self.__list.extend(point_list)

    # 清空这一帧的数据
    def clear(self):
        self.__list.clear()

    # 打印点阵图
    def draw_graphics(self, score):
        # os.system("clear")  # 清屏，然后打印

        print("".center(option.size * 2, "="))
        print(("score:%d" % score).center(option.size * 2, " "))
        print("".center(option.size * 2, "="))

        for i in range(option.size):  # 行
            for j in range(option.size):  # 列
                if (i, j) in self.__list:
                    print("🌹️", end="")
                else:
                    print("  ", end="")
            print()

# d = Displayer()
# d.extend_points([(1, 1), (2, 6), (6, 7), (7, 4)])
# d.draw_graphics()
