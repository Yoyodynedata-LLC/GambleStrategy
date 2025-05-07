#StratTester.py
import json, itertools, random
from Player_Hand import player_Hand
from Dealer_Hand import dealer_Hand

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
    # innerLoop goes to shoeSize * 2 which is breaking each 52 card deck into 2 groups of 26 cards each 
    # for every deck in the shoe 
    # then pick a random card from each group of 26 cards and place it as the next card in the shoe
    # each time a card is picked the pile of remaining cards is reduced by 1 so the next random number will 
    # pick only from the remaining cards 

    # repeat until all cards are randomly picked and added to the shoe
    
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

def checkForSplit(ph, upCard):
    split = 0
    card1 = ph.check_card(0)
    card2 = ph.check_card(1)
    if card1==card2:
        match card1:
            case 1:
                split += 1
            case 8:
                split += 1
            case 9:
                if 1 < upCard < 7:
                    split += 1
                elif 8 <= upCard <= 9:
                    split += 1
            case 7:
                if 1 < upCard <= 7:
                    split += 1
            case 6:
                if 1 < upCard <= 6:
                    split += 1
            case 4:
                if 5 <= upCard <= 6:
                    split += 1
            case 3:
                if 1 < upCard <= 6:
                    split += 1
            case 2:
                if 1 < upCard <= 6:
                    split += 1

    return split

def checkDoublDown(ph, upCard):
    dd = 0
    match ph.handTotal():
        case 2:
            dd+=1
        case 10:
            if upCard<10:
                dd+=1
        case 9:
            if 3 <= upCard <= 6:
                dd+=1
        case 3:
            # dd on 5 or 6
            if 5 <= upCard <= 6 and ph.softHand==1:
                dd+=1
        case 4:
            # dd on 5 or 6 for A, 3
            if 5 <= upCard <= 6 and ph.softHand==1:
                dd+=1
        case 5:
            # dd on 4, 5 or 6 for A, 4
            if 4 <= upCard <= 6 and ph.softHand==1:
                dd+=1
        case 6:
            # dd on 4, 5 or 6 for A, 5
            if 4 <= upCard <= 6 and ph.softHand==1:
                dd+=1
        case 7:
            # dd on 3-6 for A, 6
            if 3 <= upCard <= 6 and ph.softHand==1:
                dd+=1
        case 8:
            # dd on 2-6 for A, 7
            if 2 <= upCard <= 6 and ph.softHand==1:
                dd+=1
        case 9:
            # dd on 6 for A, 8
            if upCard==6 and ph.softHand==1:
                dd+=1
    return dd


def playhand(ph, upCard):
    #check for splits
    if checkForSplit(ph, upCard)>0:
        # create a second hand and call playHand for each hand again
        ph2 = player_Hand(ph.betAmt())
        playerHands.append(ph2)

        card = ph.removeCard()
        ph2.take_a_hit(card)

        # deal a new card to the first hand
        card = shoe.pop(0)
        ph.take_a_hit(card)
        playhand(ph, upCard)

        card = shoe.pop(0)
        ph2.take_a_hit(card)
        playhand(ph2, upCard)

        # check for double downs
    elif checkDoublDown(ph, upCard)>0:
        # take one hit
        card = shoe.pop(0)
        ph.take_a_hit(card)
    else:
        # play the hand normally
        while ph.handTotal()<12:
            card = shoe.pop(0)
            ph.take_a_hit(card)

        if ph.handTotal()==12 and upCard>1 and upCard<=3:
            card = shoe.pop(0)
            ph.take_a_hit(card)

        if upCard==1 or upCard>6:
            while ph.handTotal()>=12 and ph.handTotal()<=16:
                card = shoe.pop(0)
                ph.take_a_hit(card)

    return

def calculate_result(dh):
    winTotal = 0
    for ph in playerHands:
        amtbet = ph.getBetamt()

        if ph.handTotal()==21 and ph.card_count()==2:
            if dh.handTotal()==21 and dh.card_count()==2:

                if dh.upCard()==1: #on dealer Ace the player will take even money
                    winTotal += amtbet
            else:
                winTotal += amtbet*1.5

        elif dh.handTotal()==21:
            winTotal += amtbet*-1

        else:
            if ph.handTotal()>dh.handTotal():
                winTotal += amtbet
            elif ph.handTotal()<dh.handTotal():
                winTotal += amtbet*-1

    print ("Total Amt Won: ", winTotal)


    return winTotal


# start of main program here
# initialize global variables
shoeSize = 7
discard = list()
shoe = list()

bankroll = 250
bet = 0
totalHands = 500
minBet = 10
winStreak = 0
playerHands= list()

strat = '{"strategy": [{"step": "1", "bet": "5.0", "win": "2", "lose": "1", "push": "1"}, {"step": "2", "bet": "10.0", "win": "1", "lose": "1", "push": "2"}]}'

createShoe()    # initialize and load the number of decks into discard 
nextStep = 1    # set the next step in the strategy

shuffle(3)      # shuffle the decks and load them into the shoe

#iterate through the number of hands or until bankroll < minBet
handCount = 0
while(handCount<totalHands):
    print ("$$$$$$$$$$ Bankroll:", bankroll, " $$$$$$$$$$")
    playerHands = list()

    # make sure we have enough money to continue 
    if (bankroll<minBet*2):
        break

    # get the next bet in the strategy=
    ph = player_Hand(minBet)
    playerHands.append(ph)

    handCount += 1

    # deal 1 card to the player
    card = shoe.pop(0)
    ph.take_a_hit (card)

    # deal next card to the dealer - do not display
    card = shoe.pop(0)
    dh = dealer_Hand(card)

    # deal second card to the player
    card = shoe.pop(0)
    ph.take_a_hit(card)

    # deal up card to the dealer
    card = shoe.pop(0)
    dh.take_a_hit(card)

    result = 0

    # bjDealer = check for dealer blackjack
    if dh.handTotal()<21 and ph.handTotal()<21:
        playhand(ph, dh.upCard())


    # hit the dealer hand until the total >= 17
    while dh.handTotal()<17:
        card = shoe.pop(0)
        dh.take_a_hit(card)

    #analyze the results
    bankroll += calculate_result(dh)

    for ph in playerHands:
        ph.displayhand()

    dh.displayhand()

    # move all cards used to the discard
    for ph in playerHands:
        while ph.getCardcount()>0:

            card = ph.removeCard()
            discard.append(card)

    while dh.getCardcount()>0:
        card = dh.removeCard()
        discard.append(card)

    input ("Press any key to continue")

    # determine next step in strategy




    



          

       # Split Routine (currentHand)
       # this routine will check the currentHand for a split condition.  
       # If it splits: 
             # increment PlayerHands and assign to local variable NewHand
             # put one card on each hand and deal a second card to the currenthand 
             # call Split Routine for check for another split on the currentHand 
             # deal a second card to the newHand and check for another Split on that hand 
             
          # check hand for Player Split 
               # NewHand = PlayerHands ++
               # split cards 
               # deal additional card to each hand 
               # Split Routine (currentHand)
               # Split Routine (NewHand)
         #return to main with PlayerHands indicating the total number of hands to play 
               
     # PLAYER HAND (ph)
       # check strategy for PlayerHand(ph)  -- not a double down or split
            # hit until stand 

        # total Players Hand 
        # return total 

     # DEALER HAND 
        # while dealer Hand total < 17 
            # hit 

        # total dealers hand 
        # return total 





        
