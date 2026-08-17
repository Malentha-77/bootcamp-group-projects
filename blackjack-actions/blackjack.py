import random 
#create desk setup
designs = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = {str(i) for i in range(2, 11)}

RANK_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11, }

#deck class
class Deck :
    def __init__(self):
        self.cards = []
        for RANK_VALUE in RANK_VALUES :
         for design in designs :
             self.cards.append((RANK_VALUE, designs))  #do this to insert identity to the cards e.g Queen of Hearts

        #shuffle cards for chance
        random.shuffle(self.cards)
        

def hand_value(cards):
    total = sum(RANK_VALUES[card] for card in cards)
    aces = cards.count("A")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total
"""
    function that parses a decision-point string into a convenient representation.
    """
def parse_state(text):
    hand_str, dealer_upcard, flag = [part.strip() for part in text.split("|")] #strip and split functions clean data given that is seperated by "|"
    hand = [rank.strip() for rank in hand_str.split(",")] #clean data for hand_str return list seperated by ","                     

    return {
        "hand": tuple(hand),
        "dealer_upcard": dealer_upcard,
        "flag": flag.lower()  # first or later
    }


def generate_actions(state):#here you use the dictionary you got from parse_state as your input 
    playerhand=state.get("hand","no hand")
    player_total=hand_value(playerhand)
    p_flag=state.get("flag","not flag")
    p_flag=p_flag.lower()
    if player_total>21:
       return []
    actions = ["hit", "stand"] 
    if p_flag=="first":
       actions.append("double")
       actions.append("surrender")
     if len(hand) == 2 and hand[0] == hand[1]:
            actions.append("split")    
     return actions   
   
def apply_action(actions):
    pass

def draw_card(litt): # we want this "Card1, Card2 | DealerUpcard | Flag"
    values=list(litt.keys())
    return random.choice(values)  
    
print("hi how are you welcome to our game hope you have a good time playing it")
give=input("DO YOU WANT TO START YES OR NO")
give.upper()
if give == "YES":
    while game:
        player1 = (card_deck)
        hand = parse_state(player1)
        game = False # this is added to prevent infinit loops
        
        
