# class for each hand that is played 
# the value and suit of each card will be added each time a card is added to the PlayerHand 
class player_Hand:
   betAmt = 0
   cards = []
   HandValue = 0
   soft = 0

   def __init__(self, betAmt):
     self.bet = betAmt

   def card_count(self):
       # return the number of cards in the cards[] array
       return len(self.cards)

   def take_a_hit (self, card):
     self.cards.append(card)

   def check_card(self, cardNum):
       card = self.cards.pop(cardNum)
       return card[0]

   def softHand(self):
       return self.soft

   def removeCard(self):
       #remove the first card from the hand
       # used for splitting pairs
       card = self.cards.pop(0)
       return card

   def increaseBet(self, bet):
       self.betAmt = self.betAmt + bet

   def handTotal(self):
       # calculate the value of all cards in the hand
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

       if hasAces == 1:
           self.soft=1
           if handTotal + 10 > 17 and handTotal + 10 < 22:
                handTotal += 10

       self.HandValue = handTotal

       return handTotal

      
   
   
 
   
