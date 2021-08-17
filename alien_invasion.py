import sys
import pygame
# 设置类
from Settings import Setting
# 飞船
from Ship import Ships
# 子弹
from Bullet import Bullets
# 外星人
from alien import Alien
from time import sleep

from game_status import GameStatus


class AlienInvasion:
    """管理游戏资源和行为"""
    def __init__(self):
        """初始化"""
        pygame.init()

        self.settings=Setting()

        # 设置游戏窗口
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.stats=GameStatus(self)

        self.ship=Ships(self)
        # 存储子弹的编组
        self.bullets=pygame.sprite.Group()

        self.aliens=pygame.sprite.Group()
        self._creat_fleet()

    def run_game(self):

        while True:
            self._chect_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()
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

    def _creat_fleet(self):
        """创建外星人群"""

        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        available_space_x=self.settings.screen_width-(2*alien_width)
        number_aliens_x=available_space_x // (2*alien_width)

        # 计算容纳多少行外星人
        ship_height=self.ship.rect.height
        available_space_y=self.settings.screen_height-(3*alien_height)-ship_height
        number_rows=available_space_y//(2*alien_height)

        # 创建外星人群
        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._creat_alien(alien_number,row)


    def _creat_alien(self,alien_number,row):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row
        self.aliens.add(alien)

    def _check_fleetion_edge(self):
        """有外星人到达边缘时"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """外星人下移，并改变方向"""
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1

    def _check_bullet_alien_collision(self):
        # 检测是否有子弹击中外星人，是就删除
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # 新建外星人
            self._creat_fleet()

    def _update_aliens(self):
        """更新外星人的位置"""
        self._check_fleetion_edge()
        self.aliens.update()

        # 如果外星人飞船碰撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self.ship_hit()

        self._check_alien_bottom()


    def _update_bullet(self):
        self.bullets.update()

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _update_screen(self):
        # 每次循环重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # 擦去旧屏幕，显示新屏幕
        pygame.display.flip()

    def _check_alien_bottom(self):
        """检查是否有外星人到达屏幕底端"""
        screen_rect=self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    def ship_hit(self):
        """飞船被撞"""
        if self.stats.ships_left>0:
            self.stats.ships_left-=1

            self.aliens.empty()
            self.bullets.empty()

            self._creat_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else :
            self.stats.game_active=False




if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()