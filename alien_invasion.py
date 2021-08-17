import sys
import pygame
# 设置类
from Settings import Setting
# 飞船
from Ship import Ships
# 子弹
from Bullet import Bullets

class AlienInvasion:
    """管理游戏资源和行为"""
    def __init__(self):
        """初始化"""
        pygame.init()

        self.settings=Setting()

        # 设置游戏窗口
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship=Ships(self)
        # 存储子弹的编组
        self.bullets=pygame.sprite.Group()

    def run_game(self):

        while True:
            self._chect_events()
            self.ship.update()
            self._update_bullet()
            self._update_screen()


    def _chect_events(self):
        # 检测鼠标键盘事件
        for event in pygame.event.get():
            # 关闭窗口，退出游戏
            if (event.type == pygame.QUIT):
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._chect_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

    def _chect_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
        elif event.key==pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建子弹加入编组"""
        if len(self.bullets)<self.settings.bullet_max:
            new_bullet=Bullets(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        self.bullets.update()

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        # 每次循环重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 擦去旧屏幕，显示新屏幕
        pygame.display.flip();

if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()