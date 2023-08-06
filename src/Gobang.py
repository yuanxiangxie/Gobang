#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
#FileNmae  : Gobang.py
#CreateTime: 2023/8/6 18:14
#Author    : Xie,Yuanxiang
#License  : (C)Copyright 2021, XieYuanxiang@163.com
"""

import os
import random
import sys
import numpy as np

import pygame

from Board import GoBoard
from Board import GoBoardSize
from Chess import GoChess
from Chess import GoChesColor
from Chess import WhiteChess
from Chess import BlackChess


class GobangGame(object):
    """
    """

    def __init__(self):
        """
        """
        pygame.init()
        # 设置标题
        pygame.display.set_caption(GoBoard.GoBoardTitle)
        # 设置窗口大小
        self.screen = pygame.display.set_mode((GoBoardSize.MaxWindowWidth, GoBoardSize.MaxWindowHeight))
        # 设置棋子的映射关系
        self.chess_matrix = [[random.randint(0, 2) for i in range(GoBoardSize.MaxRowChessNum)] for j in range(GoBoardSize.MaxColumnChessNum)]

    def draw_board(self):
        """
        @return:
        """
        # 绘制棋盘
        go_board = GoBoard()
        go_board.do(self.screen)

    def draw_chess(self):
        """
        @return:
        """
        # 绘制棋子
        row_index = len(self.chess_matrix)
        column_index = len(self.chess_matrix[0])
        for y_position in range(row_index):
            for x_position in range(column_index):
                if self.chess_matrix[y_position][x_position] == GoChesColor.WHITE.value:
                    chess = WhiteChess()
                else:
                    chess = BlackChess()
                chess.do(self.screen, x_position, y_position)

    def run(self):
        """
        @return:
        """
        game_running = True
        while game_running:
            for event in pygame.event.get():
                # 如果点击退出按钮，则游戏结束
                if event.type == pygame.QUIT:
                    game_running = False
                    # pygame.quit()
                    # sys.exit()
                # 如果点击按钮，则开始下棋
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    continue
            self.draw_board()
            self.draw_chess()
            pygame.display.update()
            pygame.display.flip()


if __name__ == "__main__":
    gobangGame = GobangGame()
    gobangGame.run()
