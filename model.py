from card import Card
import random
import time
from view import View


cover = '''
###########
#         #
# @@@@@@@ #
# @@@@@@@ #
# @@@@@@@ #
# @@@@@@@ #
# @@@@@@@ #
#         #
###########
'''

face_1 = '''
###########
#         #
#    *    #
#   **    #
#  * *    #
#    *    #
#   ***   #
#         #
###########
'''


face_0 = '''
###########
#         #
#  *****  #
#  *   *  #
#  *   *  #
#  *   *  #
#  *****  #
#         #
###########
'''

face_2 = '''
###########
#         #
#   ***   #
#  *  *   #
#    *    #
#   *     #
#  ****   #
#         #
###########
'''

face_z = '''
###########
#         #
#  *****  #
#     *   #
#   ***   #
#   *     #
#  *****  #
#         #
###########
'''

face_u = '''
###########
#         #
#         #
#  *   *  #
#  *   *  #
#  *   *  #
#   ***   #
#         #
###########
'''

face_x = '''
###########
#         #
#  *   *  #
#   * *   #
#    *    #
#   * *   #
#  *   *  #
#         #
###########
'''

face_8 = '''
###########
#   ***   #
#  *   *  #
#   * *   #
#    *    #
#   * *   #
#  *   *  #
#   ***   #
###########
'''

face_l = '''
###########
#         #
#  *      #
#  *      #
#  *      #
#  *      #
#  *****  #
#         #
###########
'''

all_cards = {
    0: face_0,
    1: face_1,
    2: face_2,
    3: face_l,
    4: face_u,
    5: face_x,
    6: face_z,
    7: face_8,
    8: face_0,
    9: face_1,
    10: face_2,
    11: face_l,
    12: face_u,
    13: face_x,
    14: face_z,
    15: face_8,
}


class Model:

    def __init__(self):
        self._view = View()
        self._cards = []
        self._result = [0 for x in range(16)]
        r = list(range(16))
        random.shuffle(r)
        for i in r:
            self._cards.append(Card(all_cards[i], cover))


    def update(self, card1: int, card2: int):
        self._cards[card1 - 1].turn()
        self._cards[card2 - 1].turn()
        self._view.show(self._cards)

        s1 = self._cards[card1 - 1].getCurrentSide()
        s2 = self._cards[card2 - 1].getCurrentSide()
        if s1 is not s2:
            time.sleep(3)
            self._cards[card1 - 1].turn()
            self._cards[card2 - 1].turn()
            self._view.show(self._cards)
        else:
            self._result[card1 - 1] = 1
            self._result[card2 - 1] = 1
        if sum(self._result) == 16:
            self._view.finish()
