import cardclass
import random

class deck:
    def __init__(self, type):
        self.__deck = []
        self.__type = type
        """
        type = 0: element cards
        type = 1: number cards
        type = 2: symbol cards
        type = 3: pink cards
        """
    
    def shuffle(self):
        random.shuffle(self.__deck)
    
    def giveaway(self):
        if len(self.__deck) == 0:
            raise ValueError("Deck is empty")
        return self.__deck.pop(0)
    
    def gettype(self):
        return self.__type
    
