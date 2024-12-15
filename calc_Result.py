from Player_Hand import playerHand
from Dealer_Hand import dealerHand

calculate_Result (bankroll, hands, dealerHand)
  # loop through the playerHands in the array hands 
  # add up the total of wins and subtract the total losses and return the amount 
  totalWin = 0 
  foreach playerHand in hands
     if playerHand.result = '' 
           if playerHand.total = dealerHand.total 
			playerHand.result = 'P'
           if playerHand.total > dealerHand.total 
                        playerHand.result = 'W'
           else 
               playerHand.result = 'L'

      if playerHand.result = 'L'
           totalWin = totalWin - playerHand.betAmt 
      if playerHand.result = 'W'
           totalWin = totalWin + playerHand.betAmt

return totalWin
