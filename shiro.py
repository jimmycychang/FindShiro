import pygame, random

class SHIRO:
    def __init__(self):
        self.cell_size = 40
        self.cell_number = 20
        self.x = random.randint(0, self.cell_number-1)
        self.y = random.randint(0, self.cell_number-1)
        self.screen = pygame.display.set_mode((self.cell_size*self.cell_number,self.cell_size*self.cell_number))
        self.pos = pygame.math.Vector2(self.x,self.y)
        self.shiro = pygame.image.load("images/shiro.png").convert_alpha()

    def draw_shiro(self):
        shiro_rect = pygame.Rect(int(self.pos.x*self.cell_size),int(self.y*self.cell_size), self.cell_size, self.cell_size)
        self.screen.blit(self.shiro, shiro_rect)

    def randomize(self):
        self.x = random.randint(0, self.cell_number-1)
        self.y = random.randint(0, self.cell_number-1)
        self.screen = pygame.display.set_mode((self.cell_size*self.cell_number,self.cell_size*self.cell_number))
        self.pos = pygame.math.Vector2(self.x,self.y)
