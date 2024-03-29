
import itertools, random
#createShoe will create a list object and populate it with the number of decks
#specified by Shoesize
def createShoe():
    #initial creation of the shoe
    shoe=list()
    deck = list(itertools.product(range(1, 14), ['Spades', 'Hearts', 'Clubs', 'Diamonds']))
    ctr = 0
    #loop to Shoesize
    #while (ctr<Shoesize):
    #   shoe.append(deck)
    #   ctr += 1
    return
       
def displayCard(card):
    if(card[0]==1):
        print("Ace of",card[1])
    elif(card[0]==11):
        print("Jack of",card[1])
    elif(card[0]==12):
        print("Queen of",card[1])
    elif(card[0]==13):
        print("King of",card[1])
    else:
        print(card[0]," of ",card[1])
    return


#random.shuffle(deck)
#main
#initialize global variables
#user enter the number of decks to use
#Shoes = input("Number of decks:")
Shoesize = 7
#user enter the number of hands to play
#TotalHands = input("Number of hands to play:")
TotalHands = 500
#user enter the bankroll to start with
#Bankroll = input("Bankroll:")
Bankroll = 250
#user enter the strategy to use


print("number of decks",Shoesize)
print("Total Hands",TotalHands)
print("Bankroll",Bankroll)


# start with all cards in the discard object
discard=list()
#discard=createShoe()
shoe=list()
deck = list(itertools.product(range(1, 14), ['Spades', 'Hearts', 'Clubs', 'Diamonds']))


ctr = 0
#load Shoesize number of decks into discard
while (ctr<Shoesize):
    discard.extend(deck)
    ctr += 1

print("Total Cards",len(discard))

#shuffle cards
# loop through the shuffle routine 3 times - this should be set as a parameter too
# outer loop from 25 to 0 
# inner loop will go from Shoesize * 2 - 1 to 0
# this will divide each deck into two halves as in regular shuffling
# each time pick a random number between 1 and 25
# pick the card at innerLoop * (outerLoop+1) + random number
# the first time through this would choose 13 * (25+1) + random number
# thus we skip over the first 13*26 cards and then pick the random card from the remaining 26 cards
# move the corresponding card to the Shoe
# then the innerLoop will go down to 12
# we would skip over the first 12*26 cards and then pick a random card from the next 25 cards
# move the corresponding card to the Shoe
# continue this looping until we are left with one card for each half deck
# in a 7 deck shoe this means there are 14 cards remaining

# after all loops are completed there should remain just Shoesize*2 number of cards
# move all of these cards to the shoe starting with the last one first
shuffleTimes = 3
while (shuffleTimes>0):
    print ("Shuffling...",shuffleTimes)
    #print ("Discard:",len(discard))
    cardsMoved = 0
    ctr = 25
    while (ctr>0):
        innerLoop = Shoesize * 2
        while (innerLoop>0):
            innerLoop -= 1
            randomCard = random.randint(0,ctr)
            cardNum = innerLoop*(ctr+1)+randomCard
            card = discard.pop(cardNum)
            shoe.append(card)
            cardsMoved += 1
        
        ctr -= 1


    # move the last cards to the shoe
    ctr = Shoesize*2
    while (ctr>0):
        ctr-=1
        card = discard.pop(ctr)
        shoe.append(card)
    
    #move cards back to discard
   # print("Shoe size:",len(shoe))
    
    if(shuffleTimes>1):
        ctr = len(shoe)
        while(ctr>0):
            card = shoe.pop(ctr-1)
            discard.append(card)
            ctr -= 1
            
    shuffleTimes -= 1
            


# display the cards in the shoe
ctr = 0
while (ctr<len(shoe)-1):
    card = shoe[ctr]
    displayCard(card)
    ctr+=1






                           




