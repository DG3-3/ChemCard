from abc import ABC, abstractmethod
class card(ABC):
    #Abstract base class for all cards in the game.
    def __init__(self, num, type):
        self.__num = num
        self.__type = type
        """
        type = 0: element cards
        type = 1: number cards
        type = 2: symbol cards
        type = 3: pink cards
        """
    
    def get_num(self):
        return self.__num

    @abstractmethod
    def play(self):
        # This method will be overridden in the subclasses
        pass

class elecard(card):
    #Class for element cards.
    def __init__(self, num, name, ph, type):
        super().__init__(num, type)
        self.__name = name
        self.__ph = ph

    def get_name(self):
        return self.__name
    
    def get_ph(self):
        return self.__ph
    
    def play(self):
        pass

class numcard(card):
    #Class for number cards.
    def __init__(self, num, chemnum, type):
        super().__init__(num, type)
        self.__chemnum = chemnum

    def get_chemnum(self):
        return self.__chemnum
    
    def play(self):
        pass

class symcard(card):
    #Class for symbol cards.
    def __init__(self, num, sym, type):
        super().__init__(num, type)
        self.__sym = sym

    def get_sym(self): 
        return self.__sym
    
    def play(self):
        pass

class pnkcard(card):
    #Class for pink cards.
    def __init__(self, num, type):
        super().__init__(num, type)
    
    def play(self):
        pass

