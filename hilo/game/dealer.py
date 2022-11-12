from game.card import Card

class Dealer:
    "The Dealer is the person that distributes the cards at the start of the game"

    #The responsibility of th Dealer is to control the game and calculate the points
    #earned by the player

    #Attributes =>
    #dealer: A list of card instances
    #points: The player's points at the start of the game
    #total_points: The total player's points at the end of the game
    #is_playing: A boolean that makes the game running until the players ends thhe game.
    #guess: 

    def __init__(self):
        #The constructor of the Dealer

        #Args: self (Dealer): an instance of Dealer

        card_instances = []
        points = 300
        total_points = 0
        is_playing = True
        player_guess = input("")
        card = Card()
    
    def start_game(self):


        while self.is_playing:
            self.guess_card()
            self.update_score()
            self.output_score()
    
    def guess_card(self):
        #Ask tue user to guess if the next card
        #is higher or lower

        #Args: self (Dealer): an instance of Dealer

        player_guess = input("Higher or lower? [h/l]")
        self.is_playing = (player_guess == "y")
    
    def update_score(self):
        #This method calculates and updates player's score
        
        #Args: self (Dealer): an instance of Dealer

        if not self.is_playing:
            return
        
        for i in range(len(self.card_instances)):
            card = self.card_instances[i]
            card.show_current_card()
            self.points += card.points
        self.total_points += self.points

    def output_score(self):
        #This method shows the score, current card, next card, and ask the players if they want to play again.

        #Args: self (Dealer): an instance of Dealer

        if not self.is_playing:
            return
        value
        print(f"The card is: {generate_card}")