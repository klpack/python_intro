# Import random
import random 


# Deck Class
class Deck(object):
    globS = ['♥︎','♦︎','♣︎','♠︎']
    globV = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    
    # Initial
    def __init__(self):
        self.cards = []

    # Shuffle Function
    def shuffle(self):
        self.cards.clear()
        for suit in deck1.globS:
            for value in deck1.globV:
                self.cards.append(value+"-"+suit)
                random.shuffle(self.cards)

    # Dealing Function 
    def deal(self):
        if len(self.cards)>0:
            return self.cards.pop()
        else:
            raise ValueError("No more cards in the deck.")

    # Remaining Function
    def remaining(self):
        return "Cards remaining in the deck:" + str(len(self.cards))

deck1 = Deck()
deck1.shuffle()

for i in range(0,53):
    try:
        print(deck1.remaining(), " ", deck1.deal())
    except:
        ValueError
        print("No more cards in the deck.")