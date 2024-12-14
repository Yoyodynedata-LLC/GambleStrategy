# class for each hand that is played 
# the value and suit of each card will be added each time a card is added to the PlayerHand 
class player_Hand:
   betAmt = 0
   cards = []
   
   def __init__(self, betAmt, card):
     self.bet = betAmt
     self.cards.append(card)

   def take_a_hit (self, card):
     self.cards.append(card)

   def handTotal(self):
     for c in self.cards:
        total += c.value;

   def increaseBet(self, bet)
       self.betAmt = self.betAmt + bet 

   def handValue(self):
      handValue = 0
      if (self.cards[0].value=10 && self.cards[1].value=1) handValue = 21
      if (self.cards[0].value=1 && self.cards[1].value=10) handValue = 21

      
   
   
 
   
