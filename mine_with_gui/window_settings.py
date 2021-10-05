""" 游戏窗口设置 """


class Settings:

    # 初始化窗口数据

    def __init__(self):

        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (210, 210, 210)

    # 重设窗口大小

    def change_set(self, level):
        if level == 8:
            self.screen_width = 434
            self.screen_height = 434
        elif level == 12:
            self.screen_width = 650
            self.screen_height = 650
        elif level == 15:
            self.screen_width = 812
            self.screen_height = 812
