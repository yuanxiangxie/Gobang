#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
#FileNmae  : Temp.py
#CreateTime: 2023/8/6 18:33
#Author    : Xie,Yuanxiang
#License  : (C)Copyright 2021, XieYuanxiang@163.com
"""

import os
import sys
import numpy as np


import os
import sys
import numpy as np

from Chess import Chess

from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((615, 615))
    pygame.display.set_caption('五子棋')
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     chess = Chess()
            #     chess.draw(screen, 0, 0)
        screen.fill("#DD954F")
        a = pygame.Surface((603, 603), flags=pygame.HWSURFACE)
        a.fill(color='#121010')
        b = pygame.Surface((585, 585), flags=pygame.HWSURFACE)
        b.fill(color="#DD954F")
        c = pygame.Surface((579, 579), flags=pygame.HWSURFACE)
        c.fill(color='#121010')
        # d = pygame.Surface((576, 576), flags=pygame.HWSURFACE)
        # d.fill(color="#DD954F")
        e = pygame.Surface((31, 31), flags=pygame.HWSURFACE)
        e.fill(color="#DD954F")
        screen.blit(a, (6.5, 6.5))
        screen.blit(b, (15, 15))
        screen.blit(c, (18, 18))
        for j in range(18):
            for i in range(18):
                screen.blit(e, (20 + 32 * i, 20 + 32 * j))
        alist = []
        for j in range(19):
            alistone = []
            for i in range(19):
                alistone.append(0)
            alist.append(alistone)
        pygame.draw.circle(screen, '#121010', [307.5, 307.5], 5)
        pygame.draw.circle(screen, '#121010', [115.5, 307.5], 5)
        pygame.draw.circle(screen, '#121010', [499.5, 307.5], 5)
        pygame.draw.circle(screen, '#121010', [115.5, 499.5], 5)
        pygame.draw.circle(screen, '#121010', [499.5, 499.5], 5)
        pygame.draw.circle(screen, '#121010', [115.5, 115.5], 5)
        pygame.draw.circle(screen, '#121010', [499.5, 115.5], 5)
        pygame.draw.circle(screen, '#121010', [307.5, 499.5], 5)
        pygame.draw.circle(screen, '#121010', [307.5, 115.5], 5)
        pygame.display.flip()