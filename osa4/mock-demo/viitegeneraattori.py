import random
class Viitegeneraattori:
    def __init__(self):
        self._seuraava = 1

    def uusi(self):
        n = random.randint (1, 3)
        self._seuraava = self._seuraava + n

        return self._seuraava
