import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (52, 235, 195)

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()  
        self.parent_screen = parent_screen     
        self.x = SIZE * 3
        self.y = SIZE * 3
    
    def draw(self): 
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
                 
    def move(self):
        self.x = random.randint(0, 24) * SIZE
        self.y = random.randint(0, 19) * SIZE

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.play_background()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.eat = pygame.mixer.Sound("resources/ding.mp3")
        self.crash = pygame.mixer.Sound("resources/crash.mp3")
        self.pause = False
        
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
            
        return False      
    
    
    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))  
        self.surface.blit(score, (800, 10))   
    
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        
        # Snake colliding with apple
        if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.apple.x, self.apple.y):
            pygame.mixer.Sound.play(self.eat)
            self.snake.increase_length()
            self.apple.move()
            
        # Snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.snake.block_x[i], self.snake.block_y[i]):
                self.pause = True
                pygame.mixer.Sound.play(self.crash)
                self.show_game_over()
    
    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game Over! Your Score: {self.snake.length}", True, (255, 255, 255))  
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again, press Enter. To exit, press Escape.", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()
        
        
    def reset(self):
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)
        
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        self.pause = False
                        self.reset()
                        
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
            
            if not self.pause:      
                self.play() 
                
            time.sleep(0.2)

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.block_x = [SIZE] * length
        self.block_y = [SIZE] * length
        self.direction = 'down'
        for i in range(length):
            self.block_x[i] = SIZE * (length - i)
            self.block_y[i] = SIZE * (length - i)

    def draw(self):  
        self.parent_screen.fill(BACKGROUND_COLOR)  
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.block_x[i], self.block_y[i]))
        pygame.display.flip()
    
    def increase_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)
    
    def move_up(self):
        if self.direction != 'down':
            self.direction = 'up'
        
    def move_down(self):
        if self.direction != 'up':
            self.direction = 'down'
        
    def move_left(self):
        if self.direction != 'right':
            self.direction = 'left'
        
    def move_right(self):
        if self.direction != 'left':
            self.direction = 'right'
    
    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]    
        
        # Update head position
        if self.direction == 'up':
            self.block_y[0] -= SIZE
        if self.direction == 'down':
            self.block_y[0] += SIZE
        if self.direction == 'left':
            self.block_x[0] -= SIZE
        if self.direction == 'right':
            self.block_x[0] += SIZE    
            
        self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()
