# class for the dealers cards
# the value and suit of each card will be added each time a card is added to the dealerHand
# total is calculated as soft or hard total
from ShuffleDeck import createShoe, displayCard

class dealer_Hand:
    #cards - array holding the cards
    cards = []
    HandValue = 0

    def __init__(self, card):
        self.cards = [card]

    def take_a_hit(self, card):
        self.cards.append(card)
        return

    def getCardcount(self):
        # return the number of cards in the cards[] array
        return len(self.cards)

    def displayhand(self):
        print("Dealer Hand:")
        for card in self.cards:
            displayCard(card)

        return

    def upCard(self):
        #return the value of the first card in list cards
        card = self.cards[0]
        return card[0]

    def removeCard(self):
        # needed for splits when one card is used to create a new hand
        card = None

        if (len(self.cards)>0):
            card = self.cards.pop()

        return card

    def showPlayerHand(self):
        print ("Dealer Hand")
        for card in self.cards:
            displayCard(card)
        print ("Total:", self.HandValue)

    def handValue(self):
        return self.HandValue

    def handTotal(self):
        handTotal = 0
        hasAces = 0

        # check for soft hands
        for card in self.cards:
            if card[0] > 1 and card[0] <= 10:
                handTotal += card[0]
            elif card[0] > 10:
                handTotal += 10
            elif card[0] == 1:
                handTotal += 1
                hasAces = 1

        if hasAces==1:
            if handTotal + 10 > 17 and handTotal + 10 < 22:
                handTotal += 10

        self.HandValue = handTotal

        return handTotal
