# Card Class
class Card(object):

    def __init__(self,value,suit):
         
        #Sutis adn Values
        globS = ['♥︎','♦︎','♣︎','♠︎']
        globV = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        
        # Determining whether or not valid
        if suit not in globS:
            raise ValueError("Not a valid suit.")
        else:
            self.suit = suit

        if value not in globV:
            raise ValueError("Not a valid value card.")
        else:
            self.value = value
    
    # Display output function 
    def display(self):
        print("\n",self.value,"of",self.suit)

spades_ace = Card('A','♠︎')
spades_ace.display()