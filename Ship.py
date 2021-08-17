import pygame

class Ships:
    """管理飞船的类"""

    def __init__(self,ai_game):
        """初始化飞船并设置初始位置"""
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        # 飞船位置底部中心
        self.rect.midbottom=self.screen_rect.midbottom

        self.x=float(self.rect.x)

        # 移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed

        # 根据self.x更新rect
        self.rect.x=self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船居中"""
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)