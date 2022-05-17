import pygame
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("ZK")
clock = pygame.time.Clock()
test_font = pygame.font.Font('../cis106/FinalProject/Pixeltype.ttf', 50)
game_active = True

Black = (0, 0, 0)
score_surface = test_font.render('The Adventure of IT', False, Black)
score_rect = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('../cis106/FinalProject/snail1.png').convert_alpha()
sky_surface = pygame.image.load('../cis106/FinalProject/moon2.png').convert()
ground_surface = pygame.image.load('../cis106/FinalProject/floor.png').convert()
snail_rect = snail_surface.get_rect(topright= (600, 265))

player_surf = pygame.image.load('../cis106/FinalProject/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(topleft= (80, 215))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -22

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >=300:
                    player_gravity = -22

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
    
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        color = (0,163,108)
        pygame.draw.rect(screen, color, score_rect)
        pygame.draw.rect(screen, color, score_rect, 10)
        screen.blit(score_surface,(score_rect))

        #Snail
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surface,snail_rect)
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        die = (255, 87,51)
        screen.fill(die)
        
        
    pygame.display.update() 
    clock.tick(60) 