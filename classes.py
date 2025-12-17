import pygame
pygame.init()


class spinningOBS:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        
    def draw(self, screen):
        for i in range(4):
            pygame.draw.circle(screen, (34, 99, 163), (self.x - self.size // 2 + i*30, self.y - self.size//2,), (self.size))



class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 20, 40))
    
    def movement(self):
        keys = pygame.key.get_pressed()
        self.x += .55
        self.y += .55  
       # if keys[pygame.K_LEFT]:
         #   self.x -= .3
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.y -= .9
        #if keys[pygame.K_DOWN]:
            #self.y += .3
    
    def collision(self, obstacles):
        # if self.x > obstacles.x - 30 and self.x < obstacles.x + obstacles.size:
        #     if self.y > obstacles.y - 50 and self.y < obstacles.y + obstacles.size:
        #         #return True
        #         print("collision")
        if self.x >= 1200 and self.x <=0:
            self.x = 100
            print("collision")
        if self.y >= 720 and self.y <=0:
            self.y = 100
            print("collision")
        #return False
        
        
