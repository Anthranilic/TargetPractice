class GameStats:
    """Track statistics for Target Practice."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.rocket_limit = 3
        self.reset_stats(self.rocket_limit)
    
    def reset_stats(self, rocket_limit):
        """Initialize statistics that can change during the game."""
        self.rockets_left = rocket_limit