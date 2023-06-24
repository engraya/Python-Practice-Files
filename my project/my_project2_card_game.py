from ast import Return
from os import readlink
import random
from tabnanny import check

#setting up the game of cards

suits = ["spades", "clubs", "hearts", "diamonds"]
suit = suits[2]
rank = "K"
value = 10
print("your card is: " + rank  + " of " +  suit )
suits.append("snakes")
for suit in suits:
    print(suit)


cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit, ranks])

random.shuffle(cards)

card = cards.pop()
print(card)


"""method 1"""
cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()
cards_dealt = deal(2)
card = cards_dealt[0]
rank = card[1]


if rank == "A":
    value = 11
elif rank == "J" or rank == "Q" or rank =="K":
    value = 10
else:
    value = rank

rank_dict = {"rank" : rank, "value" : value}
    
print(rank_dict["rank"], rank_dict["value"]) 


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):

        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank" : "A" , "value" : "11"},
            {"rank" : "2" , "value" : "2"},
            {"rank" : "3" , "value" : "3"},
            {"rank" : "4" , "value" : "4"},
            {"rank" : "5" , "value" : "5"},
            {"rank" : "6" , "value" : "6"},
            {"rank" : "7" , "value" : "7"},
            {"rank" : "8" , "value" : "8"},
            {"rank" : "9" , "value" : "9"},
            {"rank" : "10" , "value" : "10"},
            {"rank" : "J" , "value" : "10"},
            {"rank" : "Q" , "value" : "10"},
            {"rank" : "K" , "value" : "10"},
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
          random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt


random_card1 = Card("hearts", {"rank" : "J" , "value" : "10"},)
print(random_card1)
random_card2 = Card("clubs", {"rank" : "A" , "value" : "11"},)
print(random_card2)
random_card3 = Card("spades", {"rank" : "K" , "value" : "10"},)
prom_card = print(random_card3)

class Hand:
    def __init__(self, dealer= False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value = self.value + card_value
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value = self.value - 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_black_jack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards =False):
        print(f'''{"Dealer's" if self.dealer else "Your"} Hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                 and not show_all_dealer_cards and not self.is_black_jack():
                print("Hidden")
            else:
                print(card) 

        if not self.dealer:
            print("Value:", self.get_value())
            print()


class Game:
    def play(self):
        self.game_number = game_number
        self.games_to_play = games_to_play

    while games_to_play <= 0:    
        try:
            games_to_play = int(input("How many games do you want to play?  "))
        except:
            print("Sorry! only number index is accepted, you must enter a number.....")



    while game_number < games_to_play:
        game_number = game_number + 1


        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand(dealer=True)

        for i in range(2):
            player_hand.add_card(deck.deal(1))
            dealer_hand.add_card(deck.deal(1))


            print()
            print("*" * 50)
            print(f" Game {game_number} of {games_to_play}")
            print("*" * 50)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand':  (or H/S)").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal())
                    player_hand.display()
                    print()

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()


            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results: ")
            print("your hand:", player_hand_value)
            print("Dealers Hand:", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)
        

        print("\n Thanks for playing!!!!")




    def check_winner(self, player_hand, dealer_hand, game_over = False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You Busted!!!, Dealer wins.....!!!!!!")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer Buested!!!, You wins.......!!!!!")
                return True
            elif dealer_hand.is_black_jack() and player_hand.is_black_jack(): 
                print("OOOOHHHH-----both players have black jack......tie!!!")
                return True
            elif player_hand.is_black_jack():
                print("you have a black jack !!! you win")
                return True
            elif dealer_hand.is_black_jack():
                print("Dealer has a black jack !!! Dealer win")

            else:
                if player_hand.get_value() > dealer_hand.get_value():
                    print("You win.......")
                elif player_hand.get_value == dealer_hand.get_value():
                    print("drawn/tie....")
                else:
                    print("Dealer wins!!!.....")
                    return True
                return False
            
g = Game()
g.play()


