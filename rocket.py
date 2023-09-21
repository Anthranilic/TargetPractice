import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, ai_game):
        """Initialize the rocket and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the rocket image and get its rect.
        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()

        # start each new ship at the middle left of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # store a float for the ship/s exact vertical position.
        self.y = float(self.rect.y)

        # movement flag; start with a ship that's not moving.
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # update the ship's y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= 1
        if self.moving_down and self.rect.bottom < 800:
            self.y += 1

        # update rect object from self.y
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_rocket(self):
        """Center the rocket on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)