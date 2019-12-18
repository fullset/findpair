from model import Model


class Controller:
    def __init__(self):
        self._model = Model()

    def getUserRequest(self):
        card1 = int(input('Card 1: '))
        if card1 < 1 or card1 > 16:
            while card1 < 1 or card1 > 16:
                print('Incorrect. Card 1 must be between 1 and 16.Try again.')
                card1 = int(input(
                    'Card 1:'
                ))
        card2 = int(input('Card 2: '))
        if card2 < 1 or card2 > 16 or card2 == card1:
            while card2 < 1 or card2 > 16 or card2 == card1:
                print('Incorrect. Card 2 must be between 1 and 16')
                card2 = int(input(
                    'and not the same as Card 1. Try again.\nCard 2: '
                ))

        self._model.update(card1, card2)
