#StratTester.py
import json, itertools, random

def createShoe():
    # create a deck object containing a single deck of cards 
    # then load the decks one at a time into the discard for the number of decks requested
	deck = list(itertools.product(range(1, 14), ['Spades', 'Hearts', 'Clubs', 'Diamonds']))
	ctr = 0
	
	#load the number of decks into the discard  
	while(ctr<shoeSize):
	    discard.extend(deck)
	    ctr+=1
	    
	return    

def shuffle(shuffleTimes):
    # shuffle the cards in the discard and return them to the shoe 
    #shuffleTimes = 3 
    while (shuffleTimes>0):
        # write to log "shuffling"
        print ("Shuffling...")
        
        cardsMoved = 0
        ctr = 25 
        while (ctr>0):
            innerLoop = shoeSize * 2
            while(innerLoop>0):
                innerLoop -= 1
                randomCard = random.randint(0,ctr)
                cardNum = innerLoop*(ctr+1)+randomCard
                card = discard.pop(cardNum)
                shoe.append(card)
                cardsMoved += 1
            ctr -= 1


        #move the last cards to the shoe
        ctr = shoeSize * 2 

        while (ctr>0):
                ctr -= 1
                card = discard.pop(ctr)
                shoe.append(card)

        
        # move cards back to discard until the number of shuffles is reached
        if(shuffleTimes>1):
           ctr = len(shoe)
           while(ctr>0):
             card = shoe.pop(ctr-1)
             discard.append(card)
             ctr -= 1

        
        shuffleTimes -= 1
    
    return

def getBet(step):
        for i in strat['strategy']:
                if (i["step"]=step):
                        bet=i["bet"]

return
                
def getNextStep(wlp):
        for i in strat['strategy']:
                if (i["step"]=step):
                  if (wlp='W'):

                  break
                
    
# initialize global variables
shoeSize = 7
discard = list()
shoe = list()
bankroll = 250
bet = 0
totalHands = 500
minBet = 10

strat = '{"strategy": [{"step": "1", "bet": "5.0", "win": "2", "lose": "1", "push": "1"}, {"step": "2", "bet": "10.0", "win": "1", "lose": "1", "push": "2"}]}'

createShoe()    # initialize and load the number of decks into discard 
nextStep = 1    # set the next step in the strategy

shuffle(3)      # shuffle the decks and load them into the shoe

#iterate through the number of hands or until bankroll < minBet
handCount = 0
while(handCount<totalHands):
    # make sure we have enough money to continue 
    if (bankroll<minBet*2):
        break

    # get the next bet in the strategy=
    

    #play a hand

    #analyze the results

    # write hand to log

    # check strategy for next step

    






        
