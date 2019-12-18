class Card:
    def __init__(self, face: str, cover: str):
        self._face = face
        self._cover = cover
        self._current = self._cover

    def turn(self):
        if self._current is self._face:
            self._current = self._cover
        else:
            self._current = self._face

    def getCurrentSide(self):
        return self._current
