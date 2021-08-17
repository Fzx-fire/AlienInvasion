class Setting:
    """存储设置"""

    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        # 设置背景色
        self.bg_color = (230, 230, 230)
        # 飞船速度
        self.ship_speed=1.5
        self.ship_limit=3

        self.bullet_speed=1.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)

        self.bullet_max=10

        self.alien_speed=2
        self.fleet_drop_speed=10
        # fleet_direction 1:右移  -1:左移
        self.fleet_direction=1