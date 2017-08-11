# Make a class called Deck that will contain a full deck of 52 cards
# make an init method that makes a new deck of 52 playing cards
# make a shuffle method that will shuffle the cards (hint: use a function from the random module to do this!!!)
# make any other methods you think of!




import random

class Card():

	suit = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
	rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', 
			'9', '10', 'Jack', 'Queen', 'King']

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '{0} of {1}'.format(Card.rank[self.rank], Card.suit[self.suit])

class Deck():
    cards = []
    def __init__(self):
        for suit in range(len(Card.suit)):
        	for rank in range(len(Card.rank)):
        		self.cards.append(Card(suit, rank))

    def __str__(self):
    	return '\n'.join((str(card)) for card in self.cards)

    def shuffle(self):
    	random.shuffle(self.cards)