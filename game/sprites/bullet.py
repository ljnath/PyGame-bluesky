import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game_env, src_x, src_y):
        super(Bullet, self).__init__()
        self.__game_env = game_env
        self.__x = src_x
        self.__y = src_y
        self.surf = pygame.image.load(game_env.constants.bullet_image).convert()    # loading bullet image from file
        self.surf.set_colorkey((255,255,255), self.__game_env.RLEACCEL)             # setting the white color as the transperant area; RLEACCEL is used for better performance on non accelerated displays
        self.rect = self.surf.get_rect(center=(self.__x, self.__y))                 # setting the position of the bullet as the input (souce_x, src_y)

    def update(self):
        dx = self.__game_env.constants.screen_width - self.rect.x
        dy = 0
        angle = math.atan2(dy, dx)
        self.rect.x += 5 * math.cos(angle)
        self.rect.y += 5 * math.sin(angle)

        if self.rect.right > self.__game_env.constants.screen_width + self.rect.width:   # killing bullet if it crosses the screen completely
            self.kill()