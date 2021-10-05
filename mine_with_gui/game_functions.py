""" 扫雷函数文件 """


import pygame
import sys


# 难度选择函数
def choose_level(button_levels):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 监听鼠标按下哪个难度对应按钮
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_levels[0].rect.collidepoint(mouse_x, mouse_y):
                return (8, 10)
            elif button_levels[1].rect.collidepoint(mouse_x, mouse_y):
                return (12, 30)
            elif button_levels[2].rect.collidepoint(mouse_x, mouse_y):
                return (15, 40)


# 按下左键时进入dig函数
def check_left(level, true_map, show_map, button_list, block_list, mouse_x, mouse_y):
    for i in range(level[0]):
        for j in range(level[0]):
            if button_list[i][j].rect.collidepoint(mouse_x, mouse_y):
                if show_map.dig(true_map, i, j, block_list):
                    # 若接收到正值说明游戏已失败，返回正值
                    return 1


# 按下右键时进入mark函数
def check_right(level, true_map, show_map, button_list, block_list, mouse_x, mouse_y):
    for i in range(level[0]):
        for j in range(level[0]):
            if button_list[i][j].rect.collidepoint(mouse_x, mouse_y):
                show_map.mark(i, j, block_list)


# 监听鼠标事件
def check_events(level, true_map, show_map, button_list, block_list):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 如果检测到鼠标按下
            if event.button == 1:
                # 若鼠标按下事件为左键
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if check_left(level, true_map, show_map,
                              button_list, block_list, mouse_x, mouse_y):
                    # 若接收到正值说明游戏已失败，返回正值
                    return 1
            elif event.button == 3:
                # 若为右键
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_right(level, true_map, show_map,
                            button_list, block_list, mouse_x, mouse_y)


# 检测是否在胜利后点击窗口中win按钮
def check_win(button_win):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_win.rect.collidepoint(mouse_x, mouse_y):
                sys.exit()


def check_lose(button_lose):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_lose.rect.collidepoint(mouse_x, mouse_y):
                sys.exit()
