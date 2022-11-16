import random

class Card:

    def __init__(self):

        self.card_number = 0
        self.next_card_number = 0
    
    def draw_card(self):
        
        self.card_number = random.randint(1, 13)
        return self.card_number
    
    def draw_next_card(self):

        self.next_card_number = random.randint(1, 13)
        return self.next_card_number

    def compare_card_number(self, player, c_card, n_card, points):
        
        if (player.lower() == "h") and (c_card < n_card):
            points += 100
            print(f"Your score is: {points}")
        
        elif (player.lower() == "l") and (c_card > n_card):
            points += 100
            print(f"Your score is: {points}")
        
        else:
            points -= 75
            print(f"Your score is: {points}")