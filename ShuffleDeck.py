import itertools, random

deck = list(itertools.product(range(1, 14), ['Spades', 'Hearts', 'Clubs', 'Diamonds']))

random.shuffle(deck)

print ("You got:")
for i in range(5):
        print (deck[i][0])
        if (deck[i][0]==1):
                print("Ace of",deck[i][1])
        elif (deck[i][0]<=10):
                print(deck[i][0],"of",deck[i][1])
        elif (deck[i][0]==11):
                print("Jack of",deck[i][1])
        elif (deck[i][0]==12):
                print("Queen of",deck[i][1])
        elif (deck[i][0]==13):
                print("King of",deck[i][1])
                
