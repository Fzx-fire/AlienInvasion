class Setting:
    """存储设置"""

    def __init__(self):
        """初始化游戏静态设置"""
        self.screen_width = 1200
        self.screen_height = 800
        # 设置背景色
        self.bg_color = (230, 230, 230)

        self.ship_limit=3

        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)

        self.bullet_max=10

        self.fleet_drop_speed=10

        # 加快游戏速度
        self.speedup_scal=1.1
        # 随速度增加外星人分数
        self.score_scal=1.5

        self.alien_points=50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏变化的设置"""

        self.ship_speed=1.5
        self.bullet_speed=3.0
        self.alien_speed=1.0

        # fleet_direction 1:右移  -1:左移
        self.fleet_direction=1

    def increase_speed(self):
        self.ship_speed*=self.speedup_scal
        self.bullet_speed*=self.speedup_scal
        self.alien_speed*=self.speedup_scal

        self.alien_points=int(self.alien_points*self.score_scal)
        print(self.alien_points)