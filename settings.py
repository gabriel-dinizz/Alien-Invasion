class Settings:
    def __init__(self):
        # Game settings
        self.ship_speed = 1.5   
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 250)
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # limits player to 3 bullets
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 right -1 left
        self.fleet_direction = 1
    
