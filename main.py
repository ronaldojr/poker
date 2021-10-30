from core.player import Player
from core.dealer import Dealer

def main():

    dealer = Dealer()
    player_01 = Player("Player01")
    player_02 = Player("Player02")
    
    dealer.deck.start_new_deck()
    dealer.shuffle_deck()

    player_01.pick_up_cards(dealer.deal())
    player_02.pick_up_cards(dealer.deal())

    dealer.check_winner(player_01, player_02)

if __name__ == "__main__":
    main()