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
        if i.suit not in suit_dict:  # Adds suit to dictionary
             suit_dict[i.suit] = 1
        else:
            suit_dict[i.suit] += 1

    for i in hand:  # adds rank a dictionary

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

def straight (rank):
     unique_ranks = list(set(rank))
     unique_ranks = sorted(unique_ranks, key=lambda f: f.value)
     original = 0
     count = 0



     for i in unique_ranks:
        if  count == 0:
            count += i.value
            original += i.value

        elif i.value == count + 1:
            count += 1

     if count == original + 4:
           return "straight"

     else:
         if Rank.ACE in unique_ranks:
             new_unique_ranks = []
             for i in unique_ranks:
                 new_unique_ranks.append(i.value)

             new_unique_ranks.pop()
             new_unique_ranks.insert(0, 1)
             new_unique_ranks.sort()


             count = 0
             original = 0
             for i in new_unique_ranks:
                if count == 0:
                    count = i
                    original = i
                elif i == count + 1:
                     count += 1

         if count == original + 4:
             return "straight"




def two_pair (rank):
    count = 0
    for i in rank:
        if rank[i] == 2:
            count += 1

    if count == 2:
        return "two pair"


def three_of_a_kind (rank):
    for i in rank:
        if rank[i] == 3:
            return "three of a kind"

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


def one_pair (rank):
    for i in rank:
        if rank[i] == 2:
            return "one pair"



def straight_flush (suit,rank):
    check_straight = straight(rank)
    check_flush = flush(suit)
    if check_straight == "straight" and check_flush == "flush":
        return "straight flush"
