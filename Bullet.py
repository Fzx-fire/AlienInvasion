import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """管理发射的子弹"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color

        # 在(0,0)处创建子弹，在设置正确的位置
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        # 子弹从飞船顶部发射
        self.rect.midtop=ai_game.ship.rect.midtop

        self.y=float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        self.y-=self.settings.bullet_speed
        # 更新子弹位置
        self.rect.y=self.y

    def draw_bullet(self):

        pygame.draw.rect(self.screen,self.color,self.rect)
