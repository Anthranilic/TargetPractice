import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.color = (60, 60, 60)

        # create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midtop = ai_game.rocket.rect.midright

        # store the bullet's position as a float.
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the bullet up the screen."""
        # update the exact position of the bullet.
        self.x += 2.0
        # update the rect position
        self.rect.x = self.x
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
