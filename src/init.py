import deckclass
import cardclass
import playerclass
import marketclass

def deal(edeck, ndeck, sdeck, player):
    """
    Deals a card from the deck to the player.
    """
    for p in player:
        if edeck.getcards() == []:
            raise ValueError("Deck is empty")
        for i in range(5):
            p.takedeckc(edeck)
        if ndeck.getcards() == []:
            raise ValueError("Deck is empty")
        for i in range(3):
            p.takedeckc(ndeck)
        if sdeck.getcards() == []:
            raise ValueError("Deck is empty")
        for i in range(2):
            p.takedeckc(sdeck)
        
    