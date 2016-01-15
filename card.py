class Card:

	'''for pretty printing'''
	PRETTY_SUITS = {
		'S' : u"\u2660".encode('utf-8'), # spades
		'H' : u"\u2764".encode('utf-8'), # hearts
		'D' : u"\u2666".encode('utf-8'), # diamonds
		'C' : u"\u2663".encode('utf-8') # clubs
	}

	'''creates a new card given a rank and a suit'''
	def __init__(self, rank = None, suit = None):
		if (None != rank and None != suit):
			self._rank = rank
			self._suit = suit
	
	'''prints the card'''
	def to_string(self):
		return self.rank + self.suit

	'''prettyprints the card'''
	def to_pretty_string(self):
		return self.rank + Card.PRETTY_SUITS[self.suit]

	@property
	def rank(self):
		return self._rank
	
	@property
	def suit(self):
		return self._suit