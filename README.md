# Overview:
This design is for a program that will apply gambling strategies to the games of Blackjack and Craps.  Strategies are comprised of changing bet sizes and blackjack strategies or bet sizes and craps strategies.  One part of the program will simulate the selected strategy and the other side will simulate game play.  The results will be saved to a database so they can be viewed in reports in Google Sheets.

Bankroll
Keeps track of the players bankroll, the size of each bet according to a strategy.  For example, in Blackjack we always bet $10 then if we win one hand the next bet is $15.  If we win that bet we go back to the $10 bet.  
If we lose a hand we just go back to the $10 bet.
The betting strategy should be able to simulate these bets and keep track of the win loss percentage and to be applied to different games.  

Game Play
The second part of the program should play the game whether it is craps or blackjack.  Blackjack is the simpler one because it will just be an array of 52 cards X the number of decks.  Simulate shuffling the cards and then dealing the hands.  Would be nice to run multiple strategies simultaneously so it should be a multi-player game.  That way different players can be running different strategies against the same deck.

Simulating the roll of random dice for craps will be easy but paying the wins and implementing the strategy of the changing bets on each roll will be the challenge.

Connecting the Game Play with the Bankroll will be completed in the main module.

Each bet in the game must be defined.
In Blackjack we must specify the base bet, double down and split.

In craps we must specify many many bets.  So there will be an array  that keeps track of each bet for the strategy.  Each bet contains an amount, a bet type (hand, double down, split, passline, dont pass, odds, field, come, dont come, place bet).  Bets have different properties.  In 
Reports
To make this useful we should be able to set up the game to play 100 hands according to a strategy and then review the results at the end.  
# of hands/rolls.  
# of wins  
# of losses 
Profit/Loss
