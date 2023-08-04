import pygame, random, json
from pygame.sprite import Sprite

class Fireball(Sprite):
    """管理巨龙发射的火球的类"""
    
    def __init__(self, ai_settings, screen, dragon):
        super(Fireball, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载火球图像并获取其外接矩形
        with open('infomation.txt', 'r') as info:
            self.images = json.load(info)['fireballs']
            self.images = [pygame.image.load(x) for x in self.images]
            self.image = random.choice(self.images)

        # 将每个火球从龙嘴中发出
        self.rect = self.image.get_rect()
        self.rect.centerx = dragon.rect.centerx
        self.rect.top = dragon.rect.top

        # 在火球的属性值center中存储小数值
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.fireball_speed_factor

    def update(self):
        """向上移动火球"""
        # 更新火球纵坐标
        self.y -= self.speed_factor
        self.rect.y = self.y
        self.image = random.choice(self.images)

    def blitme(self):
        """在指定位置绘制火球"""
        self.screen.blit(self.image, self.rect)



