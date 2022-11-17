import random

class Card:

    # The card is the key piece of this game. The player will try to guess if the
    # next card will be higher or lower than the current card.

    # The responsibility of Card if to generate two random numbers cards. One for the current card
    # and other for the next card

    # Atributes:
    # card_number (int): The first random card number
    # next_card_number (int): The second random card number

    def __init__(self):

        self.card_number = 0
        self.next_card_number = 0
        # Constructs a new instance of Card with a card_number and next_card_number attribute.

        # Args:
            # self (Card): An instance of Card.
    
    def draw_card(self):
        # Generate a random card number to show to the user

        # Args:
            # self: (Card) An instance of Card
        
        self.card_number = random.randint(1, 13)
        return self.card_number
    
    def draw_next_card(self):
        # Generate another random card number to show to the user

        # Args:
            # self: (Card) An instance of Card
        

        self.next_card_number = random.randint(1, 13)
        return self.next_card_number