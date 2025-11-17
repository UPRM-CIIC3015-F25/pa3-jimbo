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
    count = 0
    for i in hand:
        if i not in suit_dict:  # Adds suit to dictionary
            suit_dict[i] = 1
        else:
            suit_dict[i] += 1

    for i in hand: # adds rank a dictionary
        if i not in rank_dict:
            rank_dict[i] = 1

        else:
            rank_dict[i] += 1




    for i in suit_dict: #chacks for flush
        if suit_dict[i] in ["hearts", "diamonds", "clubs", "spades"]:
            count += 1

        if count == 5:
            return "flush"
        else:
            pass




hand = [
    Card("hearts", Rank.ACE),
    Card("hearts", Rank.KING),
    Card("hearts", Rank.QUEEN),
    Card("hearts", Rank.JACK),
    Card("hearts", Rank.TEN)]

print(evaluate_hand(hand))
