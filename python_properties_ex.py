# We are improving our game and need to add an isAlive property, which returns True if the lives count is greater than 0.
# Complete the code by adding the isAlive property.
# The code uses a while loop to hit the Player, until its lives count becomes 0, using the isAlive property to make the condition.

class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1

    @property
    def isAlive(self):
        return self._lives > 0

p = Player("Cyberpunk77", int(input()))
i = 1

while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break
