import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimensions and properties of the button.
        self.width, self.height = 50, 200
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build the button's rect object and place it
        self.rect = pygame.Rect(1100, 300, self.width, self.height)
        
        # start the box in the right middle of the screen
        self.rect.y = 275
        self.y = float(self.rect.y)

        # direction settings: 1 represents down, -1 represents up
        self.target_direction = 1
        self.target_speed_modifier = 1

        self.target_speed_modifier = 0
    
    def draw_button(self):
        """Draw a blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)

    def update(self):
        """Move the button up."""
        # update the ship's y value, not the rect.
        self.y += 1 * self.target_direction * (1.01 ** self.target_speed_modifier)
        self.rect.y = self.y
    
    def check_edges(self):
        """Return true if the target is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top < 0)