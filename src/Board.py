#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
#FileNmae  : Board.py
#CreateTime: 2023/4/30 18:08
#Author    : Xie,Yuanxiang
#@License  : (C)Copyright 2021, XieYuanxiang@163.com
"""

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from enum import Enum


class GoBoardColor(Enum):
    ORANGE = "#DD954F"
    BLACK = "#121010"


class GoBoardSize(object):

    MaxSquareSize = 32
    MaxSquareGapSize = 1
    MaxCircleSize = 5
    # 设置每行每列最多有多少个棋子
    MaxRowChessNum = 35
    MaxColumnChessNum = 27

    FirstGapWidth = 10
    FirstGapHeight = 10
    SecondGapWidth = 4
    SecondGapHeight = 4
    ThirdGapWidth = 2
    ThirdGapHeight = 2

    MaxWindowWidth = (MaxRowChessNum - 1) * MaxSquareSize + 4 * FirstGapWidth + 2 * SecondGapWidth + 2 * ThirdGapWidth
    MaxWindowHeight = (MaxColumnChessNum - 1) * MaxSquareSize + 4 * FirstGapHeight + 2 * SecondGapHeight + 2 * ThirdGapHeight

    BlackViewWidth = MaxWindowWidth - 2 * FirstGapWidth
    BlackViewHeight = MaxWindowHeight - 2 * FirstGapHeight
    OrangeViewWidth = BlackViewWidth - 2 * FirstGapWidth
    OrangeViewHeight = BlackViewHeight - 2 * FirstGapHeight
    SecondBlackViewWidth = OrangeViewWidth - 2 * SecondGapWidth
    SecondBlackViewHeight = OrangeViewHeight - 2 * SecondGapHeight


class GoBoard(object):

    GoBoardTitle = "五子棋"

    @property
    def __title(self):
        """
        @return:
        """
        return GoBoard.GoBoardTitle

    def do(self, screen):
        """
        @return:
        """
        # 创建最底层的背景色
        screen.fill(GoBoardColor.ORANGE.value)
        # 创建倒数第二层的窗口
        a_surface = pygame.Surface((GoBoardSize.BlackViewWidth, GoBoardSize.BlackViewHeight), flags=pygame.HWSURFACE)
        a_surface.fill(GoBoardColor.BLACK.value)
        screen.blit(a_surface, (GoBoardSize.FirstGapWidth, GoBoardSize.FirstGapHeight))
        # 创建倒数第三层的窗口
        b_surface = pygame.Surface((GoBoardSize.OrangeViewWidth, GoBoardSize.OrangeViewHeight), flags=pygame.HWSURFACE)
        b_surface.fill(GoBoardColor.ORANGE.value)
        screen.blit(b_surface, (GoBoardSize.FirstGapWidth * 2, GoBoardSize.FirstGapHeight * 2))
        # 创建倒数第四层的窗口
        c_surface = pygame.Surface((GoBoardSize.SecondBlackViewWidth, GoBoardSize.SecondBlackViewHeight), flags=pygame.HWSURFACE)
        c_surface.fill(GoBoardColor.BLACK.value)
        screen.blit(c_surface, (GoBoardSize.FirstGapWidth * 2 + GoBoardSize.SecondGapWidth, GoBoardSize.FirstGapHeight * 2 + GoBoardSize.SecondGapHeight))
        # 创建最上层的窗口（即网格线）
        d_surface = pygame.Surface((GoBoardSize.MaxSquareSize - GoBoardSize.MaxSquareGapSize, GoBoardSize.MaxSquareSize - GoBoardSize.MaxSquareGapSize), flags=pygame.HWSURFACE)
        d_surface.fill(GoBoardColor.ORANGE.value)
        for i in range(GoBoardSize.MaxRowChessNum - 1):
            for j in range(GoBoardSize.MaxColumnChessNum - 1):
                screen.blit(d_surface, (
                    2 * GoBoardSize.FirstGapWidth + GoBoardSize.SecondGapWidth + GoBoardSize.ThirdGapWidth + GoBoardSize.MaxSquareSize * i,
                    2 * GoBoardSize.FirstGapWidth + GoBoardSize.SecondGapWidth + GoBoardSize.ThirdGapHeight + GoBoardSize.MaxSquareSize * j)
                )
        # 生成黑星，按照棋盘大小分别/2和/4生成位置
        width_delta = 2 * GoBoardSize.FirstGapWidth + GoBoardSize.SecondGapWidth + GoBoardSize.ThirdGapWidth
        height_delta = 2 * GoBoardSize.FirstGapWidth + GoBoardSize.SecondGapWidth + GoBoardSize.ThirdGapWidth
        width_center = width_delta + GoBoardSize.MaxSquareSize * (GoBoardSize.MaxRowChessNum // 2)
        height_center = height_delta + GoBoardSize.MaxSquareSize * (GoBoardSize.MaxColumnChessNum // 2)
        pygame.draw.circle(screen, GoBoardColor.BLACK.value, (width_center, height_center), GoBoardSize.MaxCircleSize)
        for x_position in [-1, 1]:
            x_position = height_center + x_position * GoBoardSize.MaxSquareSize * (GoBoardSize.MaxColumnChessNum // 4 + 1)
            for y_position in [-1, 1]:
                y_position = width_center + y_position * GoBoardSize.MaxSquareSize * (GoBoardSize.MaxRowChessNum // 4 + 1)
                pygame.draw.circle(screen, GoBoardColor.BLACK.value, (y_position, x_position), GoBoardSize.MaxCircleSize)