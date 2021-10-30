import random
from .deck import Deck
import core.helper as helper

class Dealer:
    def __init__(self):
        self.deck = Deck("Poker", 2)

    def shuffle_deck(self):
        random.shuffle(self.deck.cards)

    def deal(self, quantity):

        hand = self.deck.cards[0:quantity]

        while not self.__one_wild_in_hand(hand):
            self.shuffle_deck()
            hand = self.deck.cards[0:quantity]

        self.deck.cards = self.deck.cards[quantity:]
        return hand

    def check_winner(self, player01, player02): 

        print(player01.hand)       
        print(player02.hand)       

        # player01.hand = [[{'name': '2', 'value': 2}], [{'name': 'A', 'value': 14}], [{'name': 'K', 'value': 13}], [{'name': 'k', 'value': 13}], [{'name': 'Q', 'value': 11}]]
        # player02.hand = [{'name': '4', 'value': 4}, {'name': '4', 'value': 4}, {'name': '3', 'value': 3}, {'name': '3', 'value': 3}, {'name': '2', 'value': 2}]

        self.__check_players_power([player01, player02])
        self.__show_result(player01, player02)


    def __show_result(self, player01, player02):
            
        if player01.power['value'] > player02.power['value']:
            print(f"{player01} vs {player02}: {player01.power['name']} >  {player02.power['name']} -> {player01.name} wins")

        if player01.power['value'] < player02.power['value']:
            print(f"{player01} vs {player02}: {player01.power['name']} <  {player02.power['name']} -> {player02.name} wins")

        if player01.power['value'] == player02.power['value']:

            tie = self.__untie(player01, player02)

            if tie:
                print(f"{player01} vs {player02}: {player01.power['name']} ==  {player02.power['name']} -> Tie")
            else:
                self.__show_result(player01, player02)
            


    def __untie(self, player01, player02):
            
        tie = True

        count = 0

        while tie and count < len(player01.hand):

            # if player01.power['type'] in ["highcard", "straight"]:
            #     player01.power['value'] += player01.hand[count]['value']
            #     player02.power['value'] += player02.hand[count]['value']
            # else:    
            player01.power['value'] += player01.hand[count][0]['value']
            player02.power['value'] += player02.hand[count][0]['value']

            if player01.power['value'] != player02.power['value']:
                tie = False

            count += 1

        return player01.power['value'] == player02.power['value']



    def __check_players_power(self, players):
        
        for player in players:

            if helper.has_four_of_kind(player.hand):
                player.power = {
                    "type": "4kind", 
                    "name": "Four of kind", 
                    "value": 1000 
                }
                continue

            if helper.has_full_house(player.hand):
                player.power = {
                    "type": "fullhouse", 
                    "name": "Full House", 
                    "value": 800 
                }
                continue

            if len(player.hand) == 5 and helper.is_straight(player.hand, True):
                player.power = {
                    "type": "straight", 
                    "name": "Straight", 
                    "value": 500
                }
                continue

            if helper.has_three_of_kind(player.hand):
                player.power = {
                    "type": "3kind", 
                    "name": "Three of a kind", 
                    "value": 300
                }
                continue

            if helper.has_two_pair(player.hand):
                player.power = {
                    "type": "2pair", 
                    "name": "Two pair", 
                    "value": 100 
                }
                continue

            if helper.has_pair(player.hand):
                player.power = {
                    "type": "pair", 
                    "name": "Pair", 
                    "value": 15  
                }
                continue

            if helper.has_high_card(player.hand):
                player.power = {
                    "type": "highcard", 
                    "name": "High Card", 
                    "value": player.hand[0]['value']
                }
                continue
       
    def __one_wild_in_hand(self, hand):
        wilds = 0
        for  card in hand:
            if card['name'] == "*":
                wilds += 1

        
        return wilds <= 1