import random 
#create desk setup
designs = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = [str(i) : for i in range(2, 11)]

RANK_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11, }

#deck class
class Deck :
    def _init_({self}):
        self.cards = []
        for RANK_VALUE in RANK_VALUES :
         for design in designs :
             self.cards.append((RANK_VALUES, designs))  #do this to insert identity to the cards e.g Queen of Hearts

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
    playerhand=state.get("hand","no hand")
    player_total=total(playerhand)
    p_flag=state.get("flag","not flag")
    if player_total>21:
       state["flag"]="bust"
    elif player_total==21 or player<21:
         state["flag"]="IN_PROGRESS"
    if   playerhand["flag"]=="bust":
         return "loss"
    elif state["flag"]=="IN_PROGRESS": 
         return "take another ?"
   
#let's create our card deck
card_deck = {'2':2,'K':10,'A':11,'3':3,'5':5}

    #shuffle cards for chance #like I done in the beginning
    # random.shuffle(self.cards)
def player_hand():
   stat = card_deck

if player_total ==21 :    #I'm not to sure how to execute this properly
    return stat["card_deck"] = "win"
    
elif player_total ==21 or player_total <= 21:
    return stat["card_deck"] = ""
   
if player_total[""]=="bust":
    return "loss"
   
elif stat["card_deck"]=="IN_PROGRESS": 
    return "take another ?"

def apply_action(state, action, next_card=None):
    def draw_card(litt):
        values=list(litt.keys())
    return random.choice(values)
def initialise(cards):# we want this "Card1, Card2 | DealerUpcard | Flag"
    print("These are your cards",draw_card(cards),draw_card(cards),"This is dealer card",draw_card(cards))
    return draw_card(cards),draw_card(cards),"|",draw_card(cards),"|","IN_PROGRESS"
    
print("hi how are you welcome to our game hope you have a good time playing it")
give=input("DO YOU WANT TO START YES OR NO")
give.upper()
if give=="YES":
    game=True
    while game:
        player1=initialise()
        hand=parse_state(player)
        show=generate_actions(state)
        
        


    


