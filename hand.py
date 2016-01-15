from card import Card
from deck import Deck

class Hand:
	
	'''number of cards in a hand'''
	NUM_HAND = 5
	
	def __init__(self, cards):
		if len(cards) != Hand.NUM_HAND:
			raise ValueError('number of cards should be ' + str(Hand.NUM_HAND))
		self._cards = cards
	
	def to_string(self):
		'''print the hand'''
		outstring = []
		for c in self._cards:
			outstring.append(c.to_string())		
		return ' '.join(outstring)

	def card_ranks(self):
		'''returns the list of ranks with descending order'''
		ranks = [card.rank for card in self._cards]
		# we need to convert T ->10, J -> 11, Q -> 12, K -> 13, A -> 14
		rank_map = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
		num_ranks = [rank_map[r] for r in ranks]
		num_ranks.sort(reverse=True)

		# we have to handle the low straight, A replaces 1.
		if num_ranks == [14,5,4,3,2]:
			return [5,4,3,2,1]
		else:
			return num_ranks
	
	def straight(self):
		'''returns Boolean, whether the 5 cards with the given ranks is a straight or not'''
		ranks = self.card_ranks()
		#max_card min_card difference should be 4 and all cards should be distinct
		if ((max(ranks) - min(ranks)) == 4) and len(set(ranks)) == 5:
			return True
		else:
			return False
			
	def flush(self):
		'''returns Boolean, whether all the cards in the hand have the same suit or not'''
		suits = [card.suit for card in self._cards]
		return len(set(suits)) == 1
		
	def kind(self, num, reverse=False):
		'''with reverse = False it returns the highest rank of which the ranks have exactly n. Otherwise return None. set reverse = True for returning the lowest rank instead.
		this can be used both to test if there exists n-of-a-kind, and what that rank is because 0 is not a possible rank, otherwise it wouldn't work.'''
		ranks = self.card_ranks()
		if reverse == True:
			ranks = ranks[::-1]
		for r in ranks:
			if ranks.count(r) == num: return r
		return None
		
	def two_pair(self):
		'''if there are two pairs in the ranks, returns the tuple (high_pair_rank,low_pair_rank), otherwise return None. Similar to kind function this is used both to test if there are two pairs and what the ranks of pairs are'''
		ranks = self.card_ranks()
		high_pair_rank = self.kind(2)
		if high_pair_rank == None:
			return None
		low_pair_rank = self.kind(2, reverse = True)
		if high_pair_rank != low_pair_rank:
			return (high_pair_rank, low_pair_rank)
		else:
			return None
	
	def hand_rank(self):
		'''returns the ranking of the hand. the high-level categories are:	https://en.wikipedia.org/wiki/List_of_poker_hands 
		this function returns a tuple, where the secondary ranking elements depend on the high level category itself:
		(high_level_category,[secondary_ranking])

		straight_flush  --> (9, high_card)
		four_of_a_kind  --> (8, four_of_a_kind_card, kicker) 
		full_house      --> (7, three_of_a_kind_card, pair_card)
		flush           --> (6, [ranks in descending order])
		straight        --> (5, high_card)
		three_of_a_kind --> (4, three_of_a_kind_card,[ranks])
		two_pair        --> (3, high_pair_card, low_pair_card, [ranks])
		one_pair        --> (2, pair_card, [ranks])
		high_card       --> (1, [ranks])
		
		for four_of_a_kind, kicker is actually not needed for a single deck, but adding it to allow for multiple decks if we want to do that later.
		'''
		ranks = self.card_ranks()
		if self.straight() and self.flush():
			return (9, max(ranks))
		elif self.kind(4):
			return (8, self.kind(4), self.kind(1))
		elif self.kind(3) and self.kind(2):
			return (7, self.kind(3), self.kind(2))
		elif self.flush():
			return (6, ranks)
		elif self.straight():
			return (5, max(ranks))
		elif self.kind(3):
			return(4, self.kind(3), ranks)
		elif self.two_pair():
			return(3, self.two_pair(), ranks)
		elif self.kind(2):
			return(2, self.kind(2), ranks)
		else:
			return(1, ranks)
			
