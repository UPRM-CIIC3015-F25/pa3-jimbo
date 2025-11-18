from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    suit_dict = {}
    rank_dict = {}
    for i in hand:
        if i.suit in ["hearts", "diamonds", "clubs", "spades"]:
            if i.suit not in suit_dict:  # Adds suit to dictionary
                suit_dict[i.suit] = 1
            else:
                suit_dict[i.suit] += 1

    for i in hand:  # adds rank a dictionary
        if i.rank in [TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE]:

            if i.rank not in rank_dict:
                rank_dict[i.rank] = 1

            else:
                rank_dict[i.rank] += 1



    if straight_flush(suit_dict, rank_dict) == "straight flush":
        return "straight flush"
    if four_of_a_kind(rank_dict) == "four of a kind":
        return "four of a kind"
    if full_house(rank_dict) == "full house":
        return "full house"
    if flush(suit_dict) == "flush":
        return "flush"
    if straight(rank_dict) == "straight":
        return "straight"
    if three_of_a_kind(rank_dict) == "three of a kind":
        return "three of a kind"
    if two_pair(rank_dict) == "two pair":
        return "two pair"
    if one_pair(rank_dict) == "one pair":
        return "one pair"
    else:
        return "high card"

def flush (suit): #def that takes a dict of suits to see if its a flush or not

    for i in suit:  # chacks for flush
        if suit[i] == 5:
            return "flush"

        else:
            pass

def straight (rank):
    new = []
    new_if_high = []

    original = 0
    count = 0
    for e in rank:
        new.append (e)
#
    new.sort()
    if 14 in new:
        for i in new:
            new_if_high.append (i)
        new_if_high.pop()
        new_if_high.insert(0, 1)
        new_if_high.sort()

    for i in new:
        if count == 0:
            count = i
            original = i

        elif i == count + 1:
            count += 1

    if count == original + 4:
        return "straight"

    else:
        new_count = 0
        new_original = 0

        for i in new_if_high:
            if new_count == 0:
                new_count = i
                new_original = i
            elif i == new_count + 1:
                new_count += 1

        if new_count == new_original + 4:
            return "straight"

def two_pair (rank):
    count = 0
    for i in rank:
        if rank[i] == 2:
            count += 1

    if count == 2:
        return "two pair"

    else:
        pass

def three_of_a_kind (rank):
    for i in rank:
        if rank[i] == 3:
            return "three of a kind"

    else:
        pass

def full_house (rank):
    count_for_3 = 0
    count_for_2 = 0

    for i in rank:
        if rank[i] == 3:
            count_for_3 += 1
        elif rank[i] >= 2:
            count_for_2 += 1
    if count_for_3 == count_for_2:
        return "full house"

def four_of_a_kind (rank):
    for i in rank:
        if rank[i] == 4:
            return "four of a kind"
    pass


def one_pair (rank):
    for i in rank:
        if rank[i] == 2:
            return "one pair"
    pass



def straight_flush (suit,rank):
    check_straight = straight(rank)
    check_flush = flush(suit)
    if check_straight == "straight" and check_flush == "flush":
        return "straight flush"

    else:
        pass

"""def high_card(rank):
    count = 0
    for i in rank:
        if i >= count:
            count = i

    return str(count)"""


hand = [
    Card("hearts", Rank.ACE),
    Card("hearts", Rank.KING),
    Card("hearts", Rank.QUEEN),
    Card("hearts", Rank.JACK),
    Card("hearts", Rank.TEN)]

print(evaluate_hand(hand))
