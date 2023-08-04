from settings import Settings
from dragon import Dragon
import game_functions as gf
from pygame.sprite import Group

import sys, pygame

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储火球的编组
    fireballs = Group()

    # 设置背景色
    bg_color = (230, 230, 230)

    # 创建一只巨龙
    dragon = Dragon(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, dragon, fireballs)
        dragon.update()
        gf.update_fireballs(fireballs)
        gf.update_screen(ai_settings, screen, dragon, fireballs)

run_game()
