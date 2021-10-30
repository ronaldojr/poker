
def is_straight(hand, reverse=False):
    if reverse:
        hand_copy = hand.copy()
        hand_copy.reverse()
        hand = hand_copy

    size = len(hand)
    for index, card in enumerate(hand, start=0):

        if index + 1 < size:
            
            if (card[0]['value'] - hand[index+1][0]['value']) != 1:
                return False

    return True 


def has_four_of_kind(hand):

    if len(hand) > 2:
        return False

    if type(hand[1]) == type([])  and len(hand[1]) > 1:
        return False

    return True


def has_full_house(hand):
    if len(hand) > 2:
        return False

    if type(hand[1]) == type([])  and  len(hand[1]) < 2:
        return False

    return True

def has_straight(hand):
    return False

def has_three_of_kind(hand):
    if len(hand) == 3 and type(hand[1]) == type([]) and len(hand[0]) == 3:
        return True

    return False

def has_two_pair(hand):
    if type(hand[0]) == type([]) and type(hand[1]) == type([]):
        if len(hand[0]) == 2 and len(hand[1]) == 2:
            return True

    return False

def has_pair(hand):
    if type(hand[0]) == type([]):
        if len(hand[0]) == 2 and len(hand[1]) == 1:
            return True

    return False

def has_high_card(hand):
    if len(hand) == 5:
        return True

    return False