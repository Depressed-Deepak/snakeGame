import pygame
from pygame.locals import *
import time

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500,500))
        self.snake = Snake(self.surface)
        self.snake.draw()
    
    def run(self):
        
        running = True

        while running:
            for event in pygame.event.get():

                
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if event.key == pygame.K_UP:
                        self.snake.move_up()
                    
                    if event.key == pygame.K_DOWN:
                        self.snake.move_down()
                    
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()
                    
                    if event.key == pygame.K_RIGHT:
                        self.snake.move_right()

                elif event.type == pygame.QUIT:
                    running = False
                    
            time.sleep(0.2)
                

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.block_x = 100
        self.block_y = 100

    def draw(self):  
        self.parent_screen.fill((52,235,195))  
        self.parent_screen.blit(self.block, (self.block_x,self.block_y))
        pygame.display.flip()
    
    def move_up(self):
        self.block_y = self.block_y -10
        self.draw()
        
    def move_down(self):
        self.block_y = self.block_y + 10
        self.draw()
        
    def move_left(self):
        self.block_x = self.block_x - 10
        self.draw()
        
    def move_right(self):
        self.block_x = self.block_x + 10
        self.draw()
        
    

if __name__ == "__main__":
    
    game = Game()
    game.run()
    
    
        
        
    
   