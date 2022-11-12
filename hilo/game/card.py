import random
from game.dealer import Dealer

class Card:

    def __init__(self):

        card_number = 0
        next_card = 0
        shown = True
        dealer = Dealer()
        points = 0
    
    def show_current_card(self):

        # RECORDAR tengo que comparar si la respuesta del jugador (h/l) es mayor o menor que el card_number
        # Respectuvamente, si es as[i, asignar el valor adecuado]
        print(f"Your card is: {self.card_number}")

    
    def compare_card_number(self):
        
        if dealer.player_guess.lower() == "h" and self.card_number > self.next_card:
            self.points = 100
        
        elif dealer.player_guess.lower() == "l" and self.card_number < self.next_card:
            self.points = 100
        
        else:
            points = 0

        # if dealer.player_guess == "h" and # y luego compararlo con la siguiente carta si la carta no es igual a la anterior
    
    def draw_card(self):
        
        self.card_number = random.randint(1, 13)

        self.next_card = random.randint(1, 13)