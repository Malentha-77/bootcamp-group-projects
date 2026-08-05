#commentttttt
RANK_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11,
}


def hand_value(cards):
    total = sum(RANK_VALUES[card] for card in cards)
    aces = cards.count("A")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total
"""
    Parses state text formatted as: "Card1, Card2 | DealerUpcard | Flag"
    Returns a dictionary state representation.
    """
def parse_state(text):
    hand_str, dealer_upcard, flag = [part.strip() for part in text.split("|")] #strip and split functions clean data given that is seperated by "|"
    hand = [rank.strip() for rank in hand_str.split(",")] #clean data for hand_str return list seperated by ","                     

    return {
        "hand": tuple(hand),
        "dealer_upcard": dealer_upcard,
        "flag": flag,  # e.g., 'IN_PROGRESS', 'STAND', 'BUST', 'BLACKJACK'
    }


def generate_actions(state):#here you use the dictionary you got from parse_state as your input 
    raise NotImplementedError("This function is not implemented yet.")


def apply_action(state, action, next_card=None):
    raise NotImplementedError("This function is not implemented yet.")
