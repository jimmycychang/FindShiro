import pygame, random
import base

class SHIRO:
    def __init__(self):
        self.x = random.randint(0, base.cell_number-1)
        self.y = random.randint(0, base.cell_number-1)
        self.pos = pygame.math.Vector2(self.x,self.y)
        self.shiro = pygame.image.load("images/shiro.png").convert_alpha()

    def draw_shiro(self):
        shiro_rect = pygame.Rect(int(self.pos.x*base.cell_size),int(self.y*base.cell_size), base.cell_size, base.cell_size)
        base.screen.blit(self.shiro, shiro_rect)

    def randomize(self):
        self.x = random.randint(0, base.cell_number-1)
        self.y = random.randint(0, base.cell_number-1)
        self.pos = pygame.math.Vector2(self.x,self.y)


