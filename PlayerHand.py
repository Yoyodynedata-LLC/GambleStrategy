# class for each hand that is played 
# the value and suit of each card will be added each time a card is added to the PlayerHand 
class playerHand:
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

   def handValue():
      handValue = 0
      if (self.cards[0].value=10 && self.cards[1].value=1) handValue = 21
      if (self.cards[0].value=1 && self.cards[1].value=10) handValue = 21

      
   
   
 
   
