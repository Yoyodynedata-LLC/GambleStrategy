# class for the dealers cards 
# the value and suit of each card will be added each time a card is added to the dealerHand
# total is calculated as soft or hard total
class dealer_Hand:
   cards - array holding the cards 
   
   def __init__(self, card):
     self.cards = [card]

   def take_a_hit (self, card):
     self.cards.append(card)

   def handTotal(self):
      if (self.cards[0].value=10 && self.cards[1].value=1) handValue = 21
      if (self.cards[0].value=1 && self.cards[1].value=10) handValue = 21
      
      for c in self.cards:
            total += c.value
   

      
   
   
 
   
