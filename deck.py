from card import Card
from random import shuffle

class Deck:
	'''Standard deck of cards'''

	'''suits in a deck of cards'''
	SUITS = 'SHDC'

	'''cards in a suit, ordered. T stands for 10'''
	RANKS = '23456789TJQKA'

	'''number of cards in the deck'''
	CARD_COUNT = 52
	
	'''constructs a new deck of cards, unshuffled but ordered in a kinda weird way, the order doesn't matter much anyway, as we'll always use shuffled decks'''
	def __init__(self):
		self._top = 0
		self._cards = [Card(r,s) for r in Deck.RANKS for s in Deck.SUITS]

	'''random shuffle'''
	def shuffle(self):
		shuffle(self.cards)
	
	'''print the deck'''
	def to_string(self):
		outstring = []
		for c in self.cards:
			outstring.append(c.to_string())		
		return ' '.join(outstring)
		
	'''returns the top card, if no card is remaining returns None'''
	def deal(self):
		card_to_deal = None
		if (self._top < Deck.CARD_COUNT - 1):
			card_to_deal = self.cards[self._top]
			self._top += 1
		return card_to_deal
	
	'''returns the number of remaining cards in the deck'''
	def rem(self):
		return Deck.CARD_COUNT - self._top
		
	@property
	def cards(self):
		return self._cards
	