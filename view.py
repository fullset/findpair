from card import Card


class Finish(Exception):
    pass


class View:
    def show(self, cards: list):
        print('\n' * 100)
        for i in range(0, 4):
            n_lines = cards[0].getCurrentSide().count('\n')
            lines0 = cards[i * 4].getCurrentSide().splitlines()
            lines1 = cards[i * 4 + 1].getCurrentSide().splitlines()
            lines2 = cards[i * 4 + 2].getCurrentSide().splitlines()
            lines3 = cards[i * 4 + 3].getCurrentSide().splitlines()
            for j in range(n_lines):
                line0 = lines0[j]
                line1 = lines1[j]
                line2 = lines2[j]
                line3 = lines3[j]
                print(f'{line0}{line1}{line2}{line3}')

    def finish(self):        
        raise Finish()
