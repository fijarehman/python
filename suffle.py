import random
def create_deck():
    '''creates a standard 52-card deck.'''
    suits =['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['2', '3','4','5','6','7','8','9','10','jack','queen','king','ace']
    deck =[]
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")
    return  deck

def shuffle_deck(deck):
    '''shuffles the given deck of cards in place.'''
    random.shuffle(deck)

#   create a new deck
my_deck = create_deck()
print("orignal deck(first 5 cards):")
print(my_deck[:5])
    #  print first 5 card to show its orderd
    #  shuffle the deck
shuffle_deck(my_deck)
print("\nfull shuffled deck(showing all cards):") 
    # "you can uncomment the line below to see the entire shuffled deck
for card in my_deck:
    print(card)
