"""
14-2. Target Practice: Create a rectangle at the right edge of the screen that
moves up and down at a steady rate. Then on the left side of the screen, create
a ship that the player can move up and down while firing bullets at the rectangular 
target. Add a Play button that starts the game, and when the player misses the 
target three times, end the game and make the Play button reappear. Let the player
restart the game with this Play button. 

14-3. Challenging Target Practice: Start with your work from Exercise 14-2 (page
283). Make the target move faster as the game progresses, and restart the target
at the original speed when the player clicks Play.

14-4. Make a set of buttons for Alien Invasion (will do it on Target Practice instead)
that allows the player to select an appropriate starting difficulty level for the game.
Each button should assign the appropriate values for the attributes in Settings needed
to create different difficulty levels.
"""

import sys, pygame
from rocket import Rocket
from bullets import Bullet
from button import Button
from play_button import PlayButton
from time import sleep
from game_stats import GameStats

class TargetPractice:
    """Overall calss to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Target Practice")

        self.clock = pygame.time.Clock()

        # set the background color.
        self.bg_color = (230, 230, 230)

        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()

        # make the target button
        self.elapsed_time_seconds = 0
        self.target_button = Button(self)

        # start Target Practice in an inactive state.
        self.game_active = False

        # make the Play button
        self.play_button = PlayButton(self, "Play (Default)", ((1200 / 2) - (250 / 2)), ((800 / 2) - (50 / 2)))

        # make the different difficulty levels
        self.easy_button = PlayButton(self, "Easy Mode", 100, 100)
        self.medium_button = PlayButton(self, "Medium Mode", 100, 200)
        self.hard_button = PlayButton(self, "Hard Mode", 100, 300)

        # create an instance to store game statistics.
        self.stats = GameStats(self)

        self.miss_target = 0

        # to keep track of time
        self.initial_time = pygame.time.get_ticks()

        # keep track of chosen difficulty
        self.chosen_difficulty = 1 # default difficulty
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                if self.miss_target >= 3:
                    self.game_active = False
                self.rocket.update()
                self._update_bullets()
                self._update_target()
                self._track_time()

            self._update_screen()
            self.clock.tick(60)
    
    def _track_time(self):
        """Keeps track of time."""
        self.current_time = pygame.time.get_ticks()
        self.elapsed_time = self.current_time - self.initial_time
        self.elapsed_time_seconds = self.elapsed_time / 1000.0
        self.target_button.target_speed_modifier = self.elapsed_time_seconds * self.chosen_difficulty

    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets."""
        # update bullet positions.
        self.bullets.update()

        # get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= 1200:
                self.bullets.remove(bullet)
                self.miss_target += 1
        
        # check for any bullets that have hit the target.
        # if so, get rid of the bullet
        collisions = pygame.sprite.spritecollide(self.target_button, self.bullets, True)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""

        button_difficulty_mapping = {
            self.play_button: 5,
            self.easy_button: 1,
            self.medium_button: 10,
            self.hard_button: 20
        }
        
        for button, difficulty in button_difficulty_mapping.items():
                if button.rect.collidepoint(mouse_pos):
                    # reset the game statistics
                    self.stats.reset_stats(self.stats.rocket_limit)
                    self.game_active = True

                    # get rid of any remaining bullets
                    self.bullets.empty()

                    # reset the position of the rocket and target
                    self.rocket.center_rocket()
                    self.miss_target = 0
                    del self.target_button
                    self.target_button = Button(self)

                    # reset the initial time
                    self.initial_time = pygame.time.get_ticks()

                    # set the difficulty based on button clicked / chosen
                    self.chosen_difficulty = difficulty

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blitme()
        self.target_button.draw_button()

        # draw the play buttons if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
        
        # make the most recently drawn screen visible.
        pygame.display.flip()
    
    def _update_target(self):
        """Update the position of the target box."""
        self._check_target_edges()
        self.target_button.update()
    
    def _check_target_edges(self):
        """Respond appropriately if the target reaches an edge."""
        if self.target_button.check_edges():
            self._change_target_direction()
    
    def _change_target_direction(self):
        """Change the target's direction."""
        self.target_button.target_direction *= -1

if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = TargetPractice()
    ai.run_game()