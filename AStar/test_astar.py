# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2020-05-09 16:14:23
@UpdateDate: 2020-05-11 10:37:44
'''

from . import astar


def test1():
    w, h = 6, 3
    start, goal = (0, 0), (3, 2)
    walls = [(2, 1), (3, 1), (4, 1)]
    obj = astar.AStar(w, h, start, goal, walls, astar.MANHATTAN)
    print(obj.result)


if __name__ == "__main__":
    test1()
