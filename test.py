from card import Card
from deck import Deck
from hand import Hand
from game import Game

def tests():

	#deal cards randomly
	g = Game()
	print("dealing cards")
	for i,hand in enumerate(g.hands):
		print("player"+str(i) +  	": " +hand.to_string())

	#define some hands to be used in testing
	straight_flush = Hand( [Card('4','S'), 
						Card('5','S'), 
						Card('6','S'), 
						Card('7','S'), 
						Card('8','S')
						])
	four_of_a_kind = Hand( [Card('T','S'), 
						Card('T','C'), 
						Card('T','D'), 
						Card('T','H'), 
						Card('3','S')
						])
	full_house 	   = Hand( [Card('K','S'), 
						Card('K','D'), 
						Card('K','C'), 
						Card('8','H'), 
						Card('8','S')
						])
	two_pairs 	   = Hand( [Card('K','S'), 
						Card('K','D'), 
						Card('9','C'), 
						Card('9','H'), 
						Card('8','S')
						])
	straight 	   = Hand( [Card('7','S'), 
						Card('6','D'), 
						Card('5','C'), 
						Card('4','H'), 
						Card('3','S')
						])
	low_straight  = Hand( [Card('A','S'), 
						Card('2','D'), 
						Card('3','C'), 
						Card('4','H'), 
						Card('5','S')
						])

	three_of_a_kind = Hand( [Card('K','S'), 
						Card('K','D'), 
						Card('K','C'), 
						Card('9','H'), 
						Card('8','S')
						])
						
	two_of_a_kind   = Hand( [Card('K','S'), 
						Card('K','D'), 
						Card('9','C'), 
						Card('A','H'), 
						Card('8','S')
						])
						
	high_card 	   = Hand( [Card('K','S'), 
						Card('K','D'), 
						Card('9','C'), 
						Card('9','H'), 
						Card('8','S')
						])

	#testing the helper functions for hand_rank
	assert straight_flush.card_ranks() == [8,7,6,5,4]
	assert four_of_a_kind.card_ranks() == [10,10,10,10,3]
	assert full_house.card_ranks() == [13,13,13,8,8]
	print "passed card_ranks"
	assert straight_flush.straight() == True
	assert two_of_a_kind.straight() == False
	print "passed straight"
	assert straight_flush.flush() == True
	assert four_of_a_kind.flush() == False
	print "passed flush"
	
	assert four_of_a_kind.kind(4) == 10
	assert four_of_a_kind.kind(3) == None
	assert four_of_a_kind.kind(2) == None
	assert four_of_a_kind.kind(1) == 3
	
	print "passed kind"
	assert four_of_a_kind.two_pair() == None
	assert two_pairs.two_pair() == (13,9)
	print "passed two_pair"

	#testing hand_rank
	assert straight_flush.hand_rank() == (9,8)
	assert four_of_a_kind.hand_rank() == (8,10,3)
	assert full_house.hand_rank() == (7,13,8)

	# the output of evaluate is a list, so write assertions accordingly
	g = Game(0,[straight_flush,four_of_a_kind,full_house])
	assert g.evaluate() == [straight_flush]
	g = Game(0, [four_of_a_kind,full_house])
	assert g.evaluate() == [four_of_a_kind]
	g = Game(0, [four_of_a_kind,four_of_a_kind,full_house])
	assert g.evaluate() == [four_of_a_kind,four_of_a_kind]
	g = Game(15)
	
	return "passed all tests"
	
print(tests())