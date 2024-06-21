from enum import Enum
from collections import defaultdict

class Strength:
    FiveKind  = 6
    FourKind  = 5
    FullHouse = 4
    ThreeKind = 3
    TwoPair   = 2
    OnePair   = 1
    HighCard  = 0
    
    # count how many same card
    @staticmethod
    def count_same(s:str): # return a dictionary
        output = defaultdict(int)
        for k in s:
            output[k] += 1
        return output

    @classmethod
    def getEnum(self, s:str):
        # if s all the same
        same_dict  = self.count_same(s) 
        this_value = sorted(same_dict.values())

        if ( len(same_dict) == 1 and this_value[0] == 5):
            return Strength.FiveKind 
        if (len(same_dict) == 2):
            if (this_value[0] == 2 and this_value[1] == 3): # 2 3
                return Strength.FullHouse 
            if (this_value[0] == 1 and this_value[1] == 4): # 1 4
               return Strength.FourKind
        if (len(same_dict) == 3):
            if (this_value[0] == 1): # 1 1 3 or 1 2 2 
                if (this_value[2] == 3):
                    return Strength.ThreeKind
                if (this_value[2] == 2):
                    return Strength.TwoPair
        if (len(same_dict) == 4): # 1 1 1 4
            return Strength.OnePair

        return Strength.HighCard

class Card:
    CardDict = {
        '2':1,
        '3':2,
        '4':3,
        '5':4,
        '6':5,
        '7':6,
        '8':7,
        '9':8,
        'T':9,
        'J':10,
        'Q':11,
        'K':12,
        'A':13,
        }
                    

    def __init__(self, card:str)->None:
        self.card = card
        self.Type = Strength.getEnum(self.card)
        self.First = self.card_to_num(self.card[0])
        print(self.card, self.Type, self.First)

    def card_to_num(self,c):
        return self.CardDict[c]

    def __gt__(self, other):
        if (self.Type != other.Type):
            return self.Type > other.Type
        for k,u in zip(self.card,other.card):
            if ( self.card_to_num(k) != self.card_to_num(u)):
                return  self.card_to_num(k) > self.card_to_num(u)



















