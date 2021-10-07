""" 地图类文件 """

import random


# 真实地图类

class TrueMap:

    def __init__(self, level):
        self.level = level
        self.map_true = [[[0, (99, 99), (99, 99), (99, 99), (99, 99), (99, 99), (99, 99), (
            99, 99), (99, 99), 0] for j in range(level[0])] for i in range(level[0])]
        # 元素分别为[自身周围炸弹数（为9时表示本身为炸弹）  左上  中上  右上  左  右  左下  中下  右下  是否访问过（0为否，1为是）]

        self.digged = 0

    # 连接地图函数，计算出每个格点周围八个格点的坐标，超出范围的记为 99，99

    def link_map(self):
        for i in range(self.level[0]):
            for j in range(self.level[0]):

                self.map_true[i][j][1] = (i-1, j-1)
                self.map_true[i][j][2] = (i-1, j)
                self.map_true[i][j][3] = (i-1, j+1)
                self.map_true[i][j][4] = (i, j-1)
                self.map_true[i][j][5] = (i, j+1)
                self.map_true[i][j][6] = (i+1, j-1)
                self.map_true[i][j][7] = (i+1, j)
                self.map_true[i][j][8] = (i+1, j+1)

                for ix in range(1, 9):
                    for iy in range(2):
                        if self.map_true[i][j][ix][iy] < 0 or self.map_true[i][j][ix][iy] > self.level[0]-1:
                            self.map_true[i][j][ix] = (99, 99)

                            # 将范围外坐标统一重置为 99，99

    # 随机放置指定数量（counter）地雷函数，生成范围内的随机坐标将对应格点置为炸弹（9）

    def make_mine(self):

        self.counter = self.level[1]

        while self.counter > 0:
            x = random.randint(0, self.level[0]-1)
            y = random.randint(0, self.level[0]-1)

            if self.map_true[x][y][0] == 0:
                self.map_true[x][y][0] = 9
                self.counter -= 1

    # 计算炸弹函数，利用坐标组算出自身周围炸弹，若本身为炸弹则不做处置

    def count_mine(self):
        for i in range(self.level[0]):
            for j in range(self.level[0]):
                for k in range(1, 9):

                    xx, yy = self.map_true[i][j][k]

                    if xx != 99 and yy != 99 and self.map_true[xx][yy][0] == 9 and self.map_true[i][j][0] != 9:
                        self.map_true[i][j][0] += 1

    # 返回真实地图

    def get_true(self):

        return self.map_true

    # 检查函数一，输出真实地图

    def check_game(self):
        for i in range(self.level[0]):
            for j in range(self.level[0]):
                print(self.map_true[i][j][0], end=' ')

            print('')

        print('\n')

    # 检查函数二，输出所有坐标组值

    def check_game2(self):
        for i in range(self.level[0]):
            for j in range(self.level[0]):
                for k in range(1, 9):
                    print(self.map_true[i][j][k], end=', ')

                print('\n')

            print('\n')

    # 标记被挖开的格子

    def change_digged(self, cx, cy):
        self.map_true[cx][cy][9] = 1


# 展示地图类（玩家看到的地图）

class ShowMap():

    def __init__(self, level):
        self.level = level
        self.digged = 0
        self.win = False

        self.map_show = [['O' for j in range(level[0])]
                         for i in range(level[0])]
        # 与真实地图等大的字符矩阵，'O'表示待挖掘，'M'表示标记为地雷，' '表示为空，'X'表示为炸弹

    # 标记函数，用以标记玩家推测的地雷

    def mark(self, mx, my, block_list):

        if mx in range(self.level[0]) and my in range(self.level[0]):

            if self.map_show[mx][my] == 'O':
                self.map_show[mx][my] = 'M'
                block_list[mx][my].change_image('M')

            elif self.map_show[mx][my] == 'M':
                self.map_show[mx][my] = 'O'
                block_list[mx][my].change_image('O')

    # 更新零值格子函数，若格子为零值则需要翻开它周围的非零值格子

    def update_zero(self, true_map, ux, uy, block_list):
        map_true = true_map.get_true()
        if ux != -1 and uy != -1 and map_true[ux][uy][0] == 0:
            # 若格子为零值
            self.map_show[ux][uy] = ' '
            block_list[ux][uy].change_image(' ')
            true_map.change_digged(ux, uy)
            self.digged += 1
            # 已翻开格子数加一

            for i in range(1, 9):
                # 检查当前格子周围八个格子
                xx, yy = map_true[ux][uy][i]

                if xx != 99 and yy != 99:
                    # 排除超出范围情况

                    if i in (2, 4, 5, 7) and map_true[xx][yy][i] != [99, 99] and map_true[xx][yy][9] != 1 and map_true[xx][yy][0] == 0:
                        # 若仍有零值，则递归调用此函数
                        self.update_zero(true_map, xx, yy, block_list)

                    elif map_true[xx][yy][i] != [99, 99] and map_true[xx][yy][9] != 1 and map_true[xx][yy][0] != 0:
                        # 若非零值，则进入更新数值格子函数
                        self.update_num(true_map, xx, yy, block_list)

    # 更新数值格子函数

    def update_num(self, true_map, ux, uy, block_list):
        map_true = true_map.get_true()
        if ux != -1 and uy != -1 and map_true[ux][uy][0] != 0:

            self.map_show[ux][uy] = str(map_true[ux][uy][0])
            block_list[ux][uy].change_image(self.map_show[ux][uy])
            true_map.change_digged(ux, uy)
            self.digged += 1
            # 此函数只需翻开自身即可

    # 挖掘函数

    def dig(self, true_map, dx, dy, block_list):
        if dx in range(self.level[0]) and dy in range(self.level[0]):
            # 若输入在范围内
            map_true = true_map.get_true()
            if map_true[dx][dy][9] == 0:
            
                if map_true[dx][dy][0] == 9:
                    # 若挖到炸弹
                    self.is_lose(map_true, block_list)
                    # 失败时返回正值
                    return 1

                elif map_true[dx][dy][0] == 0 and map_true[dx][dy][9] == 0:
                    # 当前为零格
                    self.map_show[dx][dy] = ' '
                    block_list[dx][dy].change_image(self.map_show[dx][dy])
                    true_map.change_digged(dx, dy)
                    self.digged += 1
                    # 挖开当前格
                    for i in range(1, 9):
                        xx, yy = map_true[dx][dy][i]

                        if xx != 99 and yy != 99:
                            if map_true[xx][yy][i] != [99, 99] and map_true[xx][yy][9] != 1 and map_true[xx][yy][0] == 0:
                                # 更新零值格
                                self.update_zero(true_map, xx, yy, block_list)

                            elif map_true[xx][yy][i] != [99, 99] and map_true[xx][yy][9] != 1 and map_true[xx][yy][0] != 0:
                                # 更新数值格
                                self.update_num(true_map, xx, yy, block_list)

                elif map_true[dx][dy][0] != 0:
                    # 当前为数格
                    self.map_show[dx][dy] = str(map_true[dx][dy][0])
                    block_list[dx][dy].change_image(self.map_show[dx][dy])
                    true_map.change_digged(dx, dy)
                    self.digged += 1

                    for i in (2, 4, 5, 7):
                        # 只需检索上下左右
                        xx, yy = map_true[dx][dy][i]

                        if xx != 99 and yy != 99 and map_true[xx][yy][i] != [99, 99] and map_true[xx][yy][9] != 1 and map_true[xx][yy][0] == 0:
                            # 若上下左右有零格
                            self.update_zero(true_map, xx, yy, block_list)

    # 失败时为玩家显示地雷位置

    def is_lose(self, map_true, block_list):
        for i in range(self.level[0]):
            for j in range(self.level[0]):
                if map_true[i][j][0] == 9:

                    self.map_show[i][j] = 'X'
                    block_list[i][j].change_image(self.map_show[i][j])

