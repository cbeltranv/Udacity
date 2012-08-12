# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    random.shuffle(mydeck)

    hands = []
    currenthand = []

    while len(hands) < numhands:
        currenthand.append(mydeck.pop(0))
        
        if len(currenthand) == n:
            hands.append(currenthand)
            currenthand = []
            
    return hands