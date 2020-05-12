# -*- coding:utf-8 -*-
'''
@Description: A*搜索
@Author: lamborghini1993
@Date: 2020-05-09 14:15:24
@UpdateDate: 2020-05-12 20:44:45
'''

import math

from typing import Tuple, List
from queue import PriorityQueue as PQuese
from functools import total_ordering

MANHATTAN = 0       # manhattan distance
DIAGONAL_STEP = 10  # diagonal step
DIAGONAL_DIS = 11   # diagonal distance

MAN_DIS = [(0, -1), (-1, 0), (1, 0), (0, 1)]
DIA_DIS = {
    (-1, -1): ((0, -1), (-1, 0)),
    (1, -1): ((0, -1), (1, 0)),
    (-1, 1): ((0, 1), (-1, 0)),
    (1, 1): ((0, 1), (1, 0)),
}


@ total_ordering
class Node:
    def __init__(self, pos: Tuple[int, int], cost: int, step: int = 0, pre: "Node" = None):
        self._pos = pos
        self._cost = cost   # 预估花费
        self._pre = pre
        self._step = step   # 真实已经花费的

    def __lt__(self, other: "Node"):
        return self._cost < other._cost

    def __eq__(self, other: "Node"):
        return self._cost == other._cost

    @property
    def pos(self):
        return self._pos

    @property
    def step(self):
        return self._step

    @property
    def pre(self):
        return self._pre


def _add(pos1, pos2):
    return (pos1[0]+pos2[0], pos1[1]+pos2[1])


class AStar:
    def __init__(self, w: int, h: int, start: Tuple[int, int], goal: Tuple[int, int], walls: List[Tuple[int, int]],
                 _type: int = MANHATTAN):
        """A*参数

        Args:
            w (int): 长
            h (int): 宽
            start (Tuple[int, int]): 起始点
            goal (Tuple[int, int]): 终点
            walls (List[Tuple[int, int]]): 墙壁坐标列表
            type (int, optional): 寻路类型. Defaults to MANHATTAN.

        Raises:
            Exception: [description]
        """

        if _type in (MANHATTAN, DIAGONAL_STEP):
            self._one_diag_cost = 1
        elif _type == DIAGONAL_DIS:
            self._one_diag_cost = math.sqrt(2)
        else:
            raise Exception("Illegal type")

        self._w = w
        self._h = h
        if not (self._legitimate(start) and self._legitimate(goal)):
            raise Exception("Illegal coordinates")
        self._type = _type
        self._pq = PQuese()
        self._start = start
        self._goal = goal
        self._land = {}
        self._visit = {}
        for pos in walls:
            if self._legitimate(pos):
                self._land[pos] = False
        self._result = []
        self._total_cost = 0
        self._start_astar()

    def _legitimate(self, pos: Tuple[int, int]) -> bool:
        if pos[0] >= self._w or pos[0] < 0:
            return False
        if pos[1] >= self._h or pos[1] < 0:
            return False
        return True

    def _get_cos(self, pos: Tuple[int, int]):
        x0, y0 = pos
        x1, y1 = self._goal
        if self._type == DIAGONAL_STEP:
            return max(abs(x0-x1), abs(y0-y1))
        if self._type == DIAGONAL_DIS:
            x = abs(x0-x1)
            y = abs(y0-y1)
            if x > y:
                x, y = y, x
            return x * math.sqrt(2) + y - x
        return abs(x0-x1) + abs(y0-y1)

    def _meet_my_judge(self, _pos):
        if not self._legitimate(_pos):
            return False
        if self._visit.get(_pos, False):
            return False
        if not self._land.get(_pos, True):
            return False
        return True

    def _next_pos(self, pos):
        for p in MAN_DIS:
            _next = _add(pos, p)
            if not self._meet_my_judge(_next):
                continue
            yield _next, 1

        if self._type == MANHATTAN:
            return

        for p, (con1, con2) in DIA_DIS.items():
            _next = _add(pos, p)
            if not self._meet_my_judge(_next):
                continue
            con1 = _add(pos, con1)
            con2 = _add(pos, con2)
            if self._land.get(con1, True) or self._land.get(con2, True):
                yield _next, self._one_diag_cost

    def _start_astar(self):
        self._pq.put(Node(self._start, 0))
        self._visit[self._start] = True
        while not self._pq.empty():
            head = self._pq.get()
            if head.pos == self._goal:
                self._count_result(head)
                return
            for _next, _one_cost in self._next_pos(head.pos):
                self._visit[_next] = True
                cost = head.step + _one_cost + self._get_cos(_next)
                self._pq.put(Node(_next, cost, head.step + _one_cost, head))

    def _count_result(self, tail: Node):
        self._total_cost = tail.step
        tmp = tail
        while tmp.pre:
            self._result.insert(0, tmp.pos)
            tmp = tmp.pre

    @property
    def result(self):
        return self._total_cost, self._result
