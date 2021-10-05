""" 鼠标按钮文件，此文件定义按钮类 """


import pygame


# 雷区格子类
class Click_block():
    def __init__(self, x_in, y_in):

        self.width, self.height = 54, 54
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x_in, y_in)


# 难度按钮类
class Button_level:
    def __init__(self, screen, msg, x_in, y_in):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 600, 100
        self.button_color = (210, 210, 210)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 60)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x_in, y_in)
        self.prep_msg(msg)

    # 生成按钮文字
    def prep_msg(self, msg):
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    # 渲染按钮函数
    def draw_button(self, screen):

        self.screen = screen
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


# 胜利按钮类，此按钮用于使玩家单击窗口以退出
class Button_win:
    def __init__(self, screen, msg, gm_set):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = gm_set.screen_width, gm_set.screen_height
        # 按钮充满整个窗口

        self.button_color = (210, 210, 210)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 100)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, screen):

        self.screen = screen
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


# 失败按钮类
class Button_lose():
    def __init__(self, screen, gm_set):
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, gm_set.screen_width, gm_set.screen_height)
        self.rect.center = self.screen_rect.center
