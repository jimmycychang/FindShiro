import pygame
from shiro import SHIRO
from shinchan import SHINCHAN

class MAIN_FUNC:
    def __init__(self):
        self.shiro = SHIRO()
        self.shinchan = SHINCHAN()
        self.cell_size = 40
        self.cell_number = 20 
        self.game_font = pygame.font.SysFont("monospace", 40)
        self.screen = pygame.display.set_mode((self.cell_size*self.cell_number,self.cell_size*self.cell_number))

    def update(self):
        self.shinchan.move_shinchan()
        self.check_collision()
        self.check_fail()
    
    def draw_element(self):
        self.draw_background()
        self.shiro.draw_shiro()
        self.shinchan.draw_shinchan()
        self.score()

    def check_collision(self):
        if self.shiro.pos == self.shinchan.body[0]:
            self.shiro.randomize()
            self.shinchan.add_block()
            self.shinchan.sound.play()


    def check_fail(self):
        if not 0 <= self.shinchan.body[0].x < self.cell_number or not 0 <= self.shinchan.body[0].y < self.cell_number:
            self.game_over()
        for block in self.shinchan.body[1:]:
            if block == self.shinchan.body[0]:
                self.game_over()
    
    def game_over(self):
        self.shinchan.reset()

    def draw_background(self):
        background_color = (167,209,61)
        for row in range(self.cell_number):
            if row % 2 == 0:
                for col in range(self.cell_number):
                    if col % 2 == 0:
                        background_rect = pygame.Rect(col*self.cell_size, row*self.cell_size,
                                                 self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen, background_color, background_rect)
            else:
                for col in range(self.cell_number):
                    if col % 2 != 0:
                        background_rect = pygame.Rect(col*self.cell_size, row*self.cell_size,
                                                 self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen, background_color, background_rect)


    def score(self):
        score_text = str(len(self.shinchan.body)-3) 
        score_surface = self.game_font.render(score_text, True, "white")
        score_x = int(self.cell_size*self.cell_number-60)
        score_y = int(self.cell_size*self.cell_number-40)
        score_rect = score_surface.get_rect(center=(score_x,score_y))
        shiro_rect = self.shiro.shiro.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(shiro_rect.left, shiro_rect.top, (shiro_rect.width+score_rect.width), shiro_rect.height)

        pygame.draw.rect(self.screen, "black", bg_rect)
        pygame.draw.rect(self.screen, "white", bg_rect, 2)
        
        self.screen.blit(score_surface, score_rect)
        self.screen.blit(self.shiro.shiro, shiro_rect)

