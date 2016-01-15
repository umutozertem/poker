from card import Card
from deck import Deck
from hand import Hand

class Game:
	
	'''maximum number of players in the game, just because we are using a single deck in the initialization function. allows passing as many hands as desired by providing a hand list explicitly though'''
	MAX_NUM_PLAYERS = 10
	
	def __init__(self, num_players = 2, hand_list = None):
		'''initialize the game by randomly shuffling a deck, unless the list of hands is explicitly provided. hand_list shouldn't be needed for the real game but it makes testing all test cases a lot easier.'''
		if hand_list == None:
			if num_players > Game.MAX_NUM_PLAYERS:
				raise ValueError("maximum number of players in a game is "+str(Game.MAX_NUM_PLAYERS))
		
			#assuming that we are playing with a single deck. This can be changed easily, as the Hand class is not implemented as a set of cards, so it allows duplicates.
			d = Deck()
			d.shuffle()
			self._hands = []
			for player in range(num_players):
				self._hands.append(Hand([d.deal() for i in range(5)]))
		else:
			self._hands = hand_list[:]
			
	@property
	def hands(self):
		return self._hands
	
	def evaluate(self):
		'''given a game, returns the winning hand(s) over the list of hands in the game. The output is also a list, given that there may be ties.'''
		input_list = self.hands
		output_list = []
		maxvalue = None
		
		# instead of finding the max and iterating again to find items equal to it, we can do it with a single pass.
		for item in input_list:
			value = item.hand_rank()
			if len(output_list) == 0 or value > maxvalue:
				output_list = [item]
				maxvalue = value
			elif value == maxvalue:
				output_list.append(item)
		return output_list		
