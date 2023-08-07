import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """表示单个敌人的类"""

    def __init__(self, ai_settings, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载敌人图像，并设置其rect属性
        self.image = pygame.image.load('images/monster_resized.bmp')
        self.rect = self.image.get_rect()

        # 每个敌人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储敌人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制敌人"""
        self.screen.blit(self.image, self.rect)




