""" 扫雷主函数文件 """

import time
import os
import timer
import mine

# 初始化输入为空字符
in_key = '\0'


# 输出计分板函数

def print_board():
    player_list = []
    i = 1
    trans_line = 1

    print("\n======================== THIS IS A RANK BOARD ========================\n")
    path_now = os.getcwd()
    #path_now = os.getcwd()

    with open('D:\CodeField\Python\\test\games\mine\\board.txt') as board_file:
        # 打开计分板文件
        for line in board_file:
            # 按行读取文件内容

            line = line.rstrip()
            player_list.append(tuple(line.split(sep=' ')))
            # 内容依次为名称，用时，记录时间和游戏难度

    for player in player_list:
        if trans_line != int(player[3]):
            print()
            # 在不同游戏难度处空一行

        hour, minu, sec = time_cal(int(player[1]))
        trans_line = player[3]

        print(i, '   name: ', player[0], '   ',
              hour, 'h ', minu, 'min ', sec, 's   time:', player[2], 'level', player[3])

        i += 1


# 保存计分板函数

def save_board(name, timer, str_time, level_tag):
    player_list = []

    with open('D:\CodeField\Python\\test\games\mine\\board.txt') as board_file:
        for line in board_file:
            line = line.rstrip()
            player_list.append(tuple(line.split(sep=' ')))

    player_list.append((name, timer, str_time, level_tag))

    player_list.sort(key=lambda playerx: (
        int(playerx[3]), int(playerx[1])), reverse=False)
    # 以游戏难度为主关键字，用时为此关键字对计分板排序

    with open('D:\CodeField\Python\\test\games\mine\\board.txt', 'w') as board_file:
        for player in player_list:
            str_in = str(player[0] + ' ' +
                         str(player[1]) + ' ' + player[2] + ' ' + player[3] + '\n')
            board_file.write(str_in)


# 难度选择函数

def choose_level():

    in_key = 'K'
    while not in_key in {'1', '2', '3', '4'}:
        os.system("cls")
        print('\nchoose your level:\n easy game  (8 *8  10)     -1\nnormal game (12*12 25)     -2',
              '\n hard game  (20*20 40)     -3\ncheck board                -b\n quit game                 -q\n')
        in_key = input(">>")

        if in_key == 'b':
            # os.system("clear")
            os.system("cls")
            print_board()
            time.sleep(5)
            # os.system("clear")

        elif in_key == 'q':
            return (0, 0), '\0'

    leveln = int(in_key)

    if leveln == 1:
        return (8, 10), '1'

    elif leveln == 2:
        return (12, 30), '2'

    elif leveln == 3:
        return (16, 40), '3'


# 将计分板内秒数换成时分秒

def time_cal(time_in):
    hour = time_in // 3600
    minu = time_in % 3600 // 60
    sec = (time_in - minu) % 60
    return hour, minu, sec


# 游戏暂停

def game_pause(timer):
    print('\n\n\n-------GAME PAUSE-------\n\n\n\ninput anykey to continue...')
    if input('>>'):
        timer.conti()
        return True


# 主函数

def main():

    # os.system("clear")
    os.system("cls")
    print('\n\nPLAYER, WELCOME TO MINES!!')

    level, level_tag = choose_level()
    if level_tag == '\0':
        return

    game_timer = timer.MyTimer()
    true_map = mine.TrueMap(level)
    true_map.link_map()
    true_map.make_mine()
    true_map.count_mine()
    show_map = mine.ShowMap(level)
    # 数据初始化

    while show_map.digged != (level[0] ** 2 - level[1]):
        # 当已挖掘数未达到安全格子数时循环

        # os.system("clear")
        os.system("cls")

        # true_map.check_game()
        # true_map.check_game2()
        # print(show_map.digged)

        show_map.print_map()
        keyword = input('>>')

        if keyword == 'q':
            return

        elif keyword == 'd':
            show_map.dig(true_map, input('x='), input('y='))

            if show_map.digged > 0:
                # 玩家挖掘第一个格子后开始计时
                game_timer.start()

            if show_map.digged == -1:
                # 已挖掘被置负数时判负，游戏结束
                # os.system("clear")
                os.system("cls")
                show_map.is_lose(true_map.get_true())
                # 在地图中展示炸弹
                show_map.print_map()
                print('YOU LOSE, GOOD LUCK NEXT TIME.')

                return

        elif keyword == 'm':
            show_map.mark(int(input('x='))-1, int(input('y='))-1)

        elif keyword == 'p':
            if not game_timer.pause():
                # 若pause返回false则说明游戏尚未开始
                time.sleep(2)
                continue

            os.system('cls')
            # os.system('clear')
            game_pause(game_timer)

    # 循环结束，此时游戏胜利

    game_timer.stop()
    now_time = time.localtime()
    # 记录胜利时间

    str_time = str(now_time[0]) + '-' + str(now_time[1]) + '-' + str(now_time[2]) + \
        '-' + str(now_time[3]) + ':' + \
        str(now_time[4]) + ':' + str(now_time[5])
    time_spend = game_timer.get_time()
    hour, minu, sec = time_cal(time_spend)
    print('YOU WIN!!\nyour time : ', hour, 'h ', minu, 'min ', sec, 's')
    save_board(input('tell us your name : '),
               (time_spend), str_time, level_tag)
    # 将信息写入计分板

    return True


main()
