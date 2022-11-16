from game.card import Card

class Dealer:
    "The Dealer is the person that distributes the cards at the start of the game"

    #The responsibility of th Dealer is to control the game and calculate the points
    #earned by the player

    # Attributes =>
    # dealer: A list of card instances
    # points: The player's points at the start of the game
    # total_points: The total player's points at the end of the game
    # is_playing: A boolean that makes the game running until the players ends thhe game.
    # guess: 

    def __init__(self):
        # The constructor of the Dealer

        # Args: self (Dealer): an instance of Dealer

        self.card_instances = []
        self.points = 300
        self.total_points = 0
        self.is_playing = True
        self.card = Card()
        self.player_guess = ""
    
    def start_game(self):

        while self.is_playing:
            self.guess_card()
            # self.calculate_score()
            # self.output_score()
    
    def guess_card(self):
        # Show card
        # Ask the user to guess if the next card is higher or lower
        # calculate the show the score

        #Args: self (Dealer): an instance of Dealer
        current_card = self.card.draw_card()
        next_card = self.card.draw_next_card()
        
        print(f"The card is: {current_card}")
        self.player_guess = input("Higher or lower? [h/l] ")

        if current_card != next_card:
            print(f"Next card was: {next_card}")

        if (self.player_guess.lower() == "h") and (current_card < next_card):
            self.points += 100
            print(f"Your score is: {self.points}")
        
        elif (self.player_guess.lower() == "l") and (current_card > next_card):
            self.points += 100
            print(f"Your score is: {self.points}")
        
        else:
            self.points -= 75
            print(f"Your score is: {self.points}")
        
        self.player_guess = input("Play again? [y/n] ")
        self.is_playing = (self.player_guess == "y")
        print()
    
    def calculate_points(self, guess, c_card, n_card, score):

        # This method calculates and updates player's score
        
        # Args: self (Dealer): an instance of Dealer

            if (guess.lower() == "h") and (c_card < n_card):
                score += 100
                print(f"Your score is: {score}")
            
            elif (guess.lower() == "l") and (c_card > n_card):
                score += 100
                print(f"Your score is: {score}")
            
            else:
                score -= 75
                print(f"Your score is: {score}")
            
            self.total_points += self.points
            
            return self.total_points

        # self.card.compare_card_number()
        # self.points += self.card.score

        # for i in range(len(self.card_instances)):
        #     card = self.card_instances[i]
        #     self.points += card.points
        # self.total_points += self.points

    def output_score(self):
        # This method shows the score, current card, next card, and ask the players if they want to play again.

        # Args: self (Dealer): an instance of Dealer

        if not self.is_playing:
            return
        # value
        # print(f"The card is: {generate_card}")