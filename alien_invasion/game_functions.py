import sys, pygame
from fireball import Fireball

def check_keydown_events(event, ai_settings, dragon, screen, fireballs):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        dragon.moving_right = True
    elif event.key == pygame.K_LEFT:
        dragon.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_fireball(ai_settings, dragon, screen, fireballs)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ai_settings, dragon, fireballs):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        dragon.moving_right = False
    elif event.key == pygame.K_LEFT:
        dragon.moving_left = False

def check_events(ai_settings, screen, dragon, fireballs):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, dragon, screen, fireballs)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, dragon, fireballs)

def update_screen(ai_settings, screen, dragon, fireballs):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    dragon.blitme()
    for fireball in fireballs:
        fireball.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_fireballs(fireballs):
    """更新火球的位置，并删除已消失的火球"""
    # 更新火球的位置
    fireballs.update()

    # 删除已消失的火球
    for fireball in fireballs.copy():
        if fireball.rect.bottom <= 0:
            fireballs.remove(fireball)

def fire_fireball(ai_settings, dragon, screen, fireballs):
    """如果还没有达到限制，就发射一枚火球。"""
    # 创建新火球，并将其加入到编组fireballs中
    if len(fireballs) < ai_settings.fireball_allowed:
        new_fireball = Fireball(ai_settings, screen, dragon)
        fireballs.add(new_fireball)







