# We are working on a game. Our Player class has name and private _lives attributes.
# The hit() method should decrease the lives of the player by 1. In case the lives equal to 0, it should output "Game Over".
# Complete the hit() method to make the program work as expected.
# The code creates a Player object and calls its hit() method multiple times.

class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
        if self._lives == 0:
            print("Game Over")

# Create a Player object
p = Player("Cyberpunk77", 3)

# Call the hit() method multiple times
p.hit()
p.hit()
p.hit()
