import pygame.font
from pygame.sprite import Group
from Ship import Ships

class Scoreboard:
    """显示得分信息"""
    def __init__(self,ai_game):
        self.ai_game=ai_game

        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings
        self.stats=ai_game.stats

        # 显示得分信息的字体设置
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        # 准备图像
        self.prep_score()

        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """得分转化为图像"""
        round_score=round(self.stats.score,-1)
        score_str="{:,}".format(round_score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        # 右上角显示得分
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """将最高得分转化为图像"""
        high_score=round(self.stats.high_score,-1)
        high_score_str="{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)

        # 最高分顶部中间
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.screen_rect.top

    def check_high_score(self):
        """检查是否出现最高分"""
        if self.stats.score>self.stats.high_score:
            self.stats.high_score=self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """等级图像"""
        level_str=str(self.stats.level)
        self.level_image=self.font.render(level_str,True,self.text_color,self.settings.bg_color)

        # 等级放在得分下方
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.screen_rect.right
        self.level_rect.top=self.score_rect.bottom+10

    def prep_ships(self):
        """显示余下多少艘飞船"""
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ships(self.ai_game)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y =10
            self.ships.add(ship)
