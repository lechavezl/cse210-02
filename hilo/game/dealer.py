from game.card import Card

class Dealer:
    # The Dealer is the person that distributes the cards at the start of the game

    # The responsibility of th Dealer is to control the game and calculate the points
    # earned by the player

    # Attributes =>
    # points (int): The player's points at the start of the game
    # is_playing (Boolean): A boolean that makes the game running until the players ends thhe game.
    # card (Card): An instance of the class Card
    # player_guess (str): An input that will ask for the player's guess
    # play_again (str): An input that asks if the user wants to keep playing or not

    def __init__(self):
        # The constructor of the Dealer

        # Args: self (Dealer): an instance of Dealer.

        self.points = 300
        self.is_playing = True
        self.card = Card()
        self.player_guess = ""
        self.play_again = ""
    
    def start_game(self):
        # Starts the game by running the main game loop.
        
        # Args:
            # self (Dealer): an instance of Dealer.

        while self.is_playing:
            self.guess_card()
    
    def guess_card(self):
        # Show the cards
        # Ask the user to guess if the next card is higher or lower
        # Show the score
        # Ask if the user wants to play again

        # Args:
            # self (Dealer): an instance of Dealer.

        #Args: self (Dealer): an instance of Dealer
        current_card = self.card.draw_card()
        next_card = self.card.draw_next_card()
        
        print(f"The card is: {current_card}")
        self.player_guess = input("Higher or lower? [h/l] ")

        print(f"Next card was: {next_card}")
        self.calculate_points(self.player_guess, current_card, next_card, self.points)

        if self.points > 0:
            self.play_again = input("Play again? [y/n] ")

            if self.play_again.lower() == "y":
                self.is_playing = True

            elif self.play_again.lower() == "n":
                print("Thanks for playing!")
                self.is_playing = False
            
            else:
                print('Please, type "y" or "n"')
        else:
            print("You lost all your points, game over.")
            self.is_playing = False

        print()
    
    def calculate_points(self, player_guess, current_card, next_card, points):
        # Calculate and print the points depending on the player's guess. If the guess is correct,
        # sum 100 points, but if not, subtract 75 points.

        
        # Args: self (Dealer): an instance of Dealer

            if (self.player_guess.lower() == "h") and (current_card < next_card):
                self.points += 100
                print(f"Your score is: {self.points}")
            
            elif (self.player_guess.lower() == "l") and (current_card > next_card):
                self.points += 100
                print(f"Your score is: {self.points}")
            
            else:
                self.points -= 75
                print(f"Your score is: {self.points}")