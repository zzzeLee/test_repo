""" 程序运行文件 """


import pygame
import time

import game_maps as maps
import mouse_click
from game_blocks import Blocks
from window_settings import Settings
from game_functions import check_win
from game_functions import check_lose
from game_functions import check_events
from game_functions import choose_level


# 打印所有格子
def print_blocks(block_list):
    for blocks_x in block_list:
        for block_i in blocks_x:
            block_i.blitme()


# 运行程序
def run_game():

    # 部分数据初始化
    level = 0
    win = 0
    gm_set = Settings()
    pygame.init()

    # 初始化窗口标题与图标
    pygame.display.set_caption("Mines")
    pygame.display.set_icon(pygame.image.load('resource/bomb.bmp'))

    # 设置窗口
    screen = pygame.display.set_mode(
        (gm_set.screen_width, gm_set.screen_height))

    # 难度选择部分
    levels = [mouse_click.Button_level(
        screen, 'level '+str(i+1), 300, 150+i*100) for i in range(3)]
    # 生成三种难度的按钮

    # 难度选择，监听鼠标事件循环
    while True:
        screen.fill(gm_set.bg_color)
        for button in levels:
            button.draw_button(screen)
        pygame.display.flip()
        level = choose_level(levels)
        if level:
            # level得到赋值后退出循环
            break

    # 根据难度更改窗口大小
    gm_set.change_set(level[0])
    screen = pygame.display.set_mode(
        (gm_set.screen_width, gm_set.screen_height))

    # 生成游戏地图（分为真实与标记两幅）
    true_map = maps.TrueMap(level)

    # 真实地图链接与处理
    true_map.link_map()
    true_map.make_mine()
    true_map.count_mine()

    show_map = maps.ShowMap(level)

    # 生成游戏雷区按钮矩阵
    block_list = [[Blocks(screen, 1+27+i*54, 1+27+j*54)
                   for i in range(level[0])] for j in range(level[0])]
    button_list = [[mouse_click.Click_block(1+27+i*54, 1+27+j*54)
                   for i in range(level[0])] for j in range(level[0])]

    # 生成胜利后点击退出按钮
    button_win = mouse_click.Button_win(screen, "YOU WIN", gm_set)

    # 当已挖掘数小于总安全格子数时循环，当二者相等时说明已经挖掘完所有格子，游戏胜利
    while show_map.digged != level[0] ** 2 - level[1]:

        # 每次循环开始时将win置为0
        win = 0

        # 监听事件
        if check_events(level, true_map, show_map, button_list,
                        block_list):
            # 若接收到正值说明游戏已失败，游戏判负后退出循环，此时win为0
            break

        # 输出背景与按钮及雷区图片
        screen.fill(gm_set.bg_color)
        print_blocks(block_list)
        pygame.display.flip()

        # 循环结束时置为1
        win = 1

    if not win:
        # 若游戏被判负，生成失败按钮
        button_lose = mouse_click.Button_lose(screen, gm_set)
        while True:
            check_lose(button_lose)
            screen.fill(gm_set.bg_color)
            print_blocks(block_list)
            pygame.display.flip()

    # 胜利后短暂停留
    time.sleep(1)
    # 游戏胜利循环
    while win:
        check_win(button_win)
        screen.fill(gm_set.bg_color)
        button_win.draw_button(screen)
        pygame.display.flip()


run_game()
