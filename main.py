import pygame, random
pygame.init()
from leveldesign import Player

screen = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("2 AM")
    

background = random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)

playerInv = []

player = Player(100, 100)


#running = True


obstacle = [
    
    #spinningOBS(200, 200, 20)
]


def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
                
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
            print(mousePos)
            
        
        
        screen.fill((20, 20, 160))
        pygame.display.flip()


def wave1():
    running = True
    pygame.time.wait(500)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        if player.x > 1200:
            player.x = 1
            screen.fill(background)
            #pygame.display.flip()sd
        if player.y > 720:
            pygame.time.wait(500)
            break
        if player.y < -40:
            pygame.time.wait(500)
            break
        
        
        
        #screen.fill((20, 20, 160))
        
        
        for x in obstacle:
            
            x.draw(screen)
            player.collision(x)
            
        player.draw(screen)
        player.movement()
    
        
        
            
        pygame.display.flip()
        
    pygame.quit()
    
    
    
main_menu()
wave1()
