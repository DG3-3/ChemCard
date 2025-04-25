import cardclass
import deckclass

class player:
    def __init__(self, name):
        self.__name = name
        self.__elecards = [5]
        self.__numcards = [3]
        self.__symcards = [2]
        self.ph = 0

    def get_name(self):
        return self.__name
    
    def __takecards(self, card):
        if isinstance(card, cardclass.elecard):
            self.__elecards.append(card)
        elif isinstance(card, cardclass.numcard):
            self.__numcards.append(card)
        elif isinstance(card, cardclass.symcard):
            self.__symcards.append(card)
        else:
            raise ValueError("Invalid card type")
    
    def deal(self, deck):
        pass

    def playc(self, card):
        if isinstance(card, cardclass.elecard):
            self.__elecards.remove(card)
        elif isinstance(card, cardclass.numcard):
            self.__numcards.remove(card)
        elif isinstance(card, cardclass.symcard):
            self.__symcards.remove(card)
        else:
            raise ValueError("Invalid card type")
        
    def borrowc(self, market):
        pass

    def eatph(self, ph):
        self.ph += ph

    def discard(self, card):
        if isinstance(card, cardclass.elecard):
            self.__elecards.remove(card)
        elif isinstance(card, cardclass.numcard):
            self.__numcards.remove(card)
        elif isinstance(card, cardclass.symcard):
            self.__symcards.remove(card)
        else:
            raise ValueError("Invalid card type")
        return card

    def takedeckc(self, deck):
        if deck.get_type() == 0:
            self.__elecards.append(deck.giveaway())
        elif deck.get_type() == 1:
            self.__numcards.append(deck.giveaway())
        elif deck.get_type() == 2:
            self.__symcards.append(deck.giveaway())
        else:
            raise ValueError("Invalid deck type")

    def takeplayerc(self, player, card):
        if isinstance(card, cardclass.elecard):
            self.__elecards.append(player.discard(card))
        elif isinstance(card, cardclass.numcard):
            self.__numcards.append(player.discard(card))
        elif isinstance(card, cardclass.symcard):
            self.__symcards.append(player.discard(card))
        else:
            raise ValueError("Invalid card type")
    