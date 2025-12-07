from typing import List

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
def evaluate_hand(hand: List[Card]):
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



    if straight_flush(suit_dict, rank_dict) == "Straight Flush":
        return "Straight Flush"
    if four_of_a_kind(rank_dict) == "Four of a Kind":
        return "Four of a Kind"
    if full_house(rank_dict) == "Full House":
        return "Full House"
    if flush(suit_dict) == "Flush":
        return "Flush"
    if straight(rank_dict) == "Straight":
        return "Straight"
    if three_of_a_kind(rank_dict) == "Three of a Kind":
        return "Three of a Kind"
    if two_pair(rank_dict) == "Two Pair":
        return "Two Pair"
    if one_pair(rank_dict) == "One Pair":
        return "One Pair"
    else:
        return "High Card"

def straight_flush(suit, rank):
    check_straight = straight(rank)
    check_flush = flush(suit)
    if check_straight == "Straight" and check_flush == "Flush":
        return "Straight Flush"


def four_of_a_kind(rank):
    for i in rank:
        if rank[i] == 4:
            return "Four of a Kind"


def full_house(rank):

    count_for_3 = 0
    count_for_2 = 0

    for i in rank:
        if rank[i] == 3:
            count_for_3 += 1
        elif rank[i] == 2:
            count_for_2 += 1

    if count_for_3 == 1 and count_for_2 == 1:
        return "Full House"


def flush(suit):  # def that takes a dict of suits to see if its a flush or not
    for i in suit:  # checks for flush
        if suit[i] == 5:
            return "Flush"


def straight(rank):
     unique_ranks = list(set(rank))
     unique_ranks = sorted(unique_ranks, key=lambda f: f.value)
     original = 0
     count = 0

     for i in unique_ranks:
        if count == 0:
            count += i.value
            original += i.value

        elif i.value == count + 1:
            count += 1

     if count == original + 4:
           return "Straight"

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
             return "Straight"


def three_of_a_kind(rank):
    for i in rank:
        if rank[i] == 3:
            return "Three of a Kind"


def two_pair(rank):
    count = 0
    for i in rank:
        if rank[i] == 2:
            count += 1

    if count == 2:
        return "Two Pair"


def one_pair(rank):
    for i in rank:
        if rank[i] == 2:
            return "One Pair"



# def flush (suit): #def that takes a dict of suits to see if its a flush or not
#
#     for i in suit:  # chacks for flush
#         if suit[i] == 5:
#             return "Flush"
#
# def straight (rank):
#      unique_ranks = list(set(rank))
#      unique_ranks = sorted(unique_ranks, key=lambda f: f.value)
#      original = 0
#      count = 0
#
#
#
#      for i in unique_ranks:
#         if  count == 0:
#             count += i.value
#             original += i.value
#
#         elif i.value == count + 1:
#             count += 1
#
#      if count == original + 4:
#            return "Straight"
#
#      else:
#          if Rank.ACE in unique_ranks:
#              new_unique_ranks = []
#              for i in unique_ranks:
#                  new_unique_ranks.append(i.value)
#
#              new_unique_ranks.pop()
#              new_unique_ranks.insert(0, 1)
#              new_unique_ranks.sort()
#
#
#              count = 0
#              original = 0
#              for i in new_unique_ranks:
#                 if count == 0:
#                     count = i
#                     original = i
#                 elif i == count + 1:
#                      count += 1
#
#          if count == original + 4:
#              return "Straight"
#
#
#
#
# def two_pair (rank):
#     count = 0
#     for i in rank:
#         if rank[i] == 2:
#             count += 1
#
#     if count == 2:
#         return "Two Pair"
#
#
# def three_of_a_kind (rank):
#     for i in rank:
#         if rank[i] == 3:
#             return "Three of a Kind"
#
# def full_house (rank):
#     count_for_3 = 0
#     count_for_2 = 0
#
#     for i in rank:
#         if rank[i] == 3:
#             count_for_3 += 1
#         elif rank[i] >= 2:
#             count_for_2 += 1
#     if count_for_3 == count_for_2:
#         return "Full House"
#
# def four_of_a_kind (rank):
#     for i in rank:
#         if rank[i] == 4:
#             return "Four of a Kind"
#
#
# def one_pair (rank):
#     for i in rank:
#         if rank[i] == 2:
#             return "One Pair"
#
#
#
# def straight_flush (suit,rank):
#     check_straight = straight(rank)
#     check_flush = flush(suit)
#     if check_straight == "Straight" and check_flush == "Flush":
#         return "Straight Flush"
