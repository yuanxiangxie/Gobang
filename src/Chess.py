#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
#FileNmae  : Chess.py
#CreateTime: 2023/8/6 17:34
#Author    : Xie,Yuanxiang
#License  : (C)Copyright 2021, XieYuanxiang@163.com
"""

import os
import sys
import numpy as np

import pygame
import time
from enum import Enum
from Board import GoBoardSize


class GoChesColor(Enum):
    WHITE = 1
    BLACK = 2


class GoChessSize(object):
    # 设置棋子大小
    MaxCircleSize = 10
    MaxCircleDenominatorSize = 10
    MaxCircleNumeratorSize = MaxCircleSize * MaxCircleDenominatorSize

class GoChess(object):

    """
        Chess Object
    """
    def __init__(self):
        """
        """
        self.max_circle = GoChessSize.MaxCircleSize
        self.max_circle_denominator = GoChessSize.MaxCircleDenominatorSize
        self.max_circle_numerator = GoChessSize.MaxCircleNumeratorSize

    def calculate_position(self, x, y):
        """
        @param x_position:
        @param y_position:
        @return:
        """
        width_delta = 2 * GoBoardSize.FirstGapWidth + GoBoardSize.SecondGapWidth + GoBoardSize.ThirdGapWidth
        height_delta = 2 * GoBoardSize.FirstGapHeight + GoBoardSize.SecondGapHeight + GoBoardSize.ThirdGapHeight
        x_position = width_delta + x * GoBoardSize.MaxSquareSize
        y_position = height_delta + y * GoBoardSize.MaxSquareSize
        return x_position, y_position

    def draw_chess(self, screen, x_position, y_position):
        """
        @param x_position:
        @param y_position:
        @return:
        """

    def do(self, screen, x_position, y_position):
        """
        @param screen:
        @param x_position:
        @param y_position:
        @return:
        """
        x_position, y_position = self.calculate_position(x_position, y_position)
        self.draw_chess(screen, x_position, y_position)

class WhiteChess(GoChess):
    def draw_chess(self, screen, x_position, y_position):
        """
        @param screen:
        @param x_position:
        @param y_position:
        @return:
        """
        rgb_r = 200
        rgb_g = 200
        rgb_b = 200
        max_circle_denominator = self.max_circle_denominator
        for i in range(50):
            pygame.draw.circle(screen, (rgb_r, rgb_g, rgb_b), [x_position, y_position], self.max_circle_numerator / max_circle_denominator)
            rgb_r += 0.3
            rgb_g += 0.3
            rgb_b += 0.3
            max_circle_denominator += 0.2


class BlackChess(GoChess):
    def draw_chess(self, screen, x_position, y_position):
        """
        @param screen:
        @param x_position:
        @param y_position:
        @return:
        """
        rgb_r = 30
        rgb_g = 30
        rgb_b = 30
        max_circle_denominator = self.max_circle_denominator
        for i in range(50):
            pygame.draw.circle(screen, (rgb_r, rgb_g, rgb_b), [x_position, y_position], self.max_circle_numerator / max_circle_denominator)
            rgb_r += 0.3
            rgb_g += 0.3
            rgb_b += 0.3
            max_circle_denominator += 0.2




