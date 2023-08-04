import pygame

class Dragon():
    
    def __init__(self, ai_settings, screen):
        """初始化龙并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载龙龙图像并获取其外接矩形
        self.image = pygame.image.load('images/dragon_resized.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每只龙放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在巨龙的属性值center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # 速度
        self.speed_factor = ai_settings.dragon_speed_factor

    def update(self):
        """根据移动标志调整巨龙的位置"""
        # 更新巨龙的center值
        if self.moving_right and self.rect.right + self.speed_factor < self.screen_rect.right:
            self.center += self.speed_factor
        if self.moving_left and self.rect.left > self.speed_factor:
            self.center -= self.speed_factor
        
        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制龙"""
        self.screen.blit(self.image, self.rect)



