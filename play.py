import pygame, sys
from main_func import MAIN_FUNC

pygame.init()
pygame.display.set_caption("Find Shiro!!")
icon = pygame.image.load("icon.ico")
pygame.display.set_icon(icon)

game = MAIN_FUNC()
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.shinchan.direction.y != 1:
                    game.shinchan.direction = pygame.math.Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if game.shinchan.direction.y != -1:  
                    game.shinchan.direction = pygame.math.Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if game.shinchan.direction.x != 1:  
                    game.shinchan.direction = pygame.math.Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if game.shinchan.direction.x != -1:
                    game.shinchan.direction = pygame.math.Vector2(1,0)

    game.screen.fill(pygame.Color("lightgreen"))
    game.draw_element()
    pygame.display.update()
    clock.tick(60)