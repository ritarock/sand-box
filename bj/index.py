import json
import random

MARK = ['Spade', 'Heart', 'Diamond', 'Club']
RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Deck:
    def __init__(self):
        self.deck = {}
        for m in MARK:
            self.deck[m] = RANK


    def draw(self):
        mark_no = MARK[random.randrange(4)]
        rank_no = RANK[random.randrange(len(self.deck[mark_no]))]
        self.deck[mark_no].remove(rank_no)
        return mark_no[:1:]+rank_no

class Player:
    def __init__(self, name):
        self.name = name
        self.hands = []

class Game:
    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck
        for i in range(0, 2):
            self.player1.hands.append(self.deck.draw())
        for i in range(0, 2):
            self.player2.hands.append(self.deck.draw())


    def check_sum(self, hands):
        self.sum_hands = 0
        for v in hands:
            if v[1::] == 'J' or v[1::] == 'Q' or v[1::] == 'K':
                self.sum_hands = self.sum_hands + 10
            elif v[1::] == 'A':
                self.sum_hands = self.sum_hands + 11
                if self.sum_hands > 21:
                    self.sum_hands = self.sum_hands - 10
            else:
                self.sum_hands = self.sum_hands + int(v[1::])

        return self.sum_hands


def main():
    deck = Deck()
    you = Player("You")
    dealer = Player("Dealer")
    game = Game(you, dealer, deck)
    flg = True

    print("===Your Card===")
    print(you.hands)

    while flg:
        print("Draw ? (y/n)")   #i1
        i1 = input()
        if i1 == "y":
            you.hands.append(deck.draw())
            print(game.check_sum(you.hands))
            if game.check_sum(you.hands) > 21:
                print(you.hands)
                print("BREAK")
                print("You Lose")
                flg = False
            else:
                print(you.hands)
        else:
            flg = False

    print("Your hand is {0}".format(you.hands))
    print("===finish===")


if __name__ == '__main__':
    main()
