import random

cardRepartition = {
        1 : 5,
        2 : 3,
        3 : 4,
        4 : 3,
        5 : 3,
        6 : 2,
        7 : 3,
        8 : 3,
        9 : 3,
        10: 2,
        11: 3,
        12: 3,
        13: 3,
        14: 2,
        15: 5,
        16: 4,
        17: 3,
        18: 1,
        19: 2,
        20: 1,
        21: 1,
        22: 1,
        23: 1,
        24: 1,
        25: 1,
        26: 1,
        27: 1,
        28: 1,
        29: 1,
        30: 1
        }

# Create the deck by appending each district's ID to a list and shuffle it
deck = []
for card in cardRepartition:
    for i in range(cardRepartition[card]):
        deck.append(card)
random.shuffle(deck)

# Function to draw n cards
def draw(n):
    global deck
    if n > len(deck):
        cards = deck
        deck = []
        return cards
    cards = deck[:n]
    deck = deck[n:]
    return cards

# Function to discard a card
def discard(cards):
    global deck
    deck.extend(cards)
