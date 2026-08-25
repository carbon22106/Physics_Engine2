from settings import *
from ball import *
from prints import *

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.ball = Ball()
        self.debug = PrintAndDebug()
    
    def run(self):
        while self.running:
            screen.fill("black")
            self.dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            self.ball.draw_ball()
            self.ball.ball_movement(self.dt)
            
            pygame.display.flip()
            self.debug.ball_prints(self.ball)
                    
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()