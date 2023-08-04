class Settings():
    """存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # 巨龙设置
        self.dragon_speed_factor = 1.5

        # 火球设置
        self.fireball_speed_factor = 1
        self.fireball_allowed = 5




