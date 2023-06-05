import pygame

class SHINCHAN:
    def __init__(self):
        self.body = [pygame.math.Vector2(5,10),pygame.math.Vector2(4,10),pygame.math.Vector2(3,10)]
        self.cell_size = 40
        self.cell_number = 20
        self.screen = pygame.display.set_mode((self.cell_size*self.cell_number,self.cell_size*self.cell_number))
        self.direction = pygame.math.Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load("images/shinchan_h_u.png").convert_alpha()
        self.head_down = pygame.image.load("images/shinchan_h_d.png").convert_alpha()
        self.head_right = pygame.image.load("images/shinchan_h_r.png").convert_alpha()
        self.head_left = pygame.image.load("images/shinchan_h_l.png").convert_alpha()

        self.tail_up = pygame.image.load("images/shinchan_b_u.png").convert_alpha()
        self.tail_down = pygame.image.load("images/shinchan_b_d.png").convert_alpha()
        self.tail_right = pygame.image.load("images/shinchan_b_r.png").convert_alpha()
        self.tail_left = pygame.image.load("images/shinchan_b_l.png").convert_alpha()

        self.body_horizontal = pygame.image.load("images/shinchan_b_l.png").convert_alpha()
        self.body_vertical = pygame.image.load("images/shinchan_b_d.png").convert_alpha()

        self.body_tr = pygame.image.load("images/shinchan_b_r.png").convert_alpha()
        self.body_tl = pygame.image.load("images/shinchan_b_l.png").convert_alpha()
        self.body_br = pygame.image.load("images/shinchan_b_r.png").convert_alpha()
        self.body_bl = pygame.image.load("images/shinchan_b_l.png").convert_alpha()

        self.sound = pygame.mixer.Sound("sounds/hehe.wav")

    def draw_shinchan(self):
        self.update_head_graphic()
        self.update_tail_graphic()

        for index, block in enumerate(self.body):
            x = int(block.x*self.cell_size)
            y = int(block.y*self.cell_size)
            block_rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
        
            if index == 0:
                self.screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                self.screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    self.screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    self.screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        self.screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        self.screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        self.screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        self.screen.blit(self.body_br, block_rect)

    def update_head_graphic(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == pygame.math.Vector2(1,0): self.head = self.head_left
        elif head_relation == pygame.math.Vector2(-1,0): self.head = self.head_right
        elif head_relation == pygame.math.Vector2(0,1): self.head = self.head_up
        elif head_relation == pygame.math.Vector2(0,-1): self.head = self.head_down

    def update_tail_graphic(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == pygame.math.Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == pygame.math.Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == pygame.math.Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == pygame.math.Vector2(0,-1): self.tail = self.tail_down
        
    def move_shinchan(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
            self.new_block = False

        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_sound(self):
        self.sound.play()
        
    def reset(self):
        self.body = [pygame.math.Vector2(5,10),pygame.math.Vector2(4,10),pygame.math.Vector2(3,10)]
        self.direction = pygame.math.Vector2(0,0)
