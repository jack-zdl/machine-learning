import sys

import pygame

from settings import Settings

def run_game():
    # 初始化游戏并创建一个屏幕对象   添加注释
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_with,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (100,100,100)
    # 开始游戏的主循环
    while True:
        #让每次循环都重绘屏幕
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()