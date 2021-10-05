""" 格子类 """


from pygame import image
#import os

#path = os.getcwd()
class Blocks:
    # 初始化，所有格子图片置为undigged
    def __init__(self, screen, loc_x, loc_y):
        self.screen = screen
        self.image = image.load('resource/undigged.bmp')
        self.rect = self.image.get_rect()
        self.bx = loc_x
        self.by = loc_y
        self.rect.centerx = self.bx
        self.rect.centery = self.by

    # 根据map_show更改对应格子图片

    def change_image(self, ctrl_key):
        if ctrl_key == ' ':
            self.image = image.load('resource/zero.bmp')
        elif ctrl_key == 'O':
            self.image = image.load('resource/undigged.bmp')
        elif ctrl_key == 'M':
            self.image = image.load('resource/flag.bmp')
        elif ctrl_key == '1':
            self.image = image.load('resource/1.bmp')
        elif ctrl_key == '2':
            self.image = image.load('resource/2.bmp')
        elif ctrl_key == '3':
            self.image = image.load('resource/3.bmp')
        elif ctrl_key == '4':
            self.image = image.load('resource/4.bmp')
        elif ctrl_key == '5':
            self.image = image.load('resource/5.bmp')
        elif ctrl_key == '6':
            self.image = image.load('resource/6.bmp')
        elif ctrl_key == '7':
            self.image = image.load('resource/7.bmp')
        elif ctrl_key == '8':
            self.image = image.load('resource/8.bmp')
        elif ctrl_key == 'X':
            self.image = image.load('resource/bomb.bmp')

    # 打印格子图片

    def blitme(self):
        self.screen.blit(self.image, self.rect)
