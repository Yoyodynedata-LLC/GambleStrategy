# class for each hand that is played 
# the value and suit of each card will be added each time a card is added to the PlayerHand 
class PlayerHand:
   def __init__(self, betAmt):
     self.bet = betAmt
     self.cards = []

   def take_a_hit (self, card):
     self.cards.append(card)

   def handTotal():
     for c in self.cards:
        total += c.value;

   def doubleDown():
      betAmt += betAmt

   
   
 
   
