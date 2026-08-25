from settings import *

class Ball:
    def __init__(self):
        self.pixel_pre_meter = 37.5
        self.GRAVITY = 9.8 * self.pixel_pre_meter # pixels/s^2
        
        self.ball_size = pygame.Vector2(25, 25)
        self.ball_pos = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.ball_vel = pygame.Vector2(5 * self.pixel_pre_meter, 0)
        self.ball_accel = pygame.Vector2(0, 0)
        self.ball = pygame.Rect(self.ball_pos, self.ball_size)
        self.ball_mass = 5 #kg
        
    def draw_ball(self):
        pygame.draw.ellipse(screen, "red", self.ball)
    
    def ball_movement(self, dt):
        self.ball_accel.y = self.GRAVITY # until freefall
        
        self.ball_vel += self.ball_accel * dt
        
        self.ball_pos += self.ball_vel * dt
        
        # Bounds
            # sides
        if self.ball_pos.x <= 0:
            self.ball_pos.x += 1
            self.ball_vel.x *= -1
            self.ball_accel.x *= -1
        elif self.ball_pos.x >= SCREEN_WIDTH - self.ball.w:
            self.ball_pos.x = SCREEN_WIDTH - self.ball.w - 1
            self.ball_vel.x *= -1
            self.ball_accel.x *= -1
            # celings
        if self.ball_pos.y >= SCREEN_HEIGHT - self.ball.h:
            self.ball_pos.y = SCREEN_HEIGHT - self.ball.h - 1
            self.ball_vel.y *= -1
        elif self.ball_pos.y <= 0:
            ... # let it go out of screen from the top only.
            
        self.ball.topleft = self.ball_pos