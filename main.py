from core.player import Player
from core.dealer import Dealer
from core.config import NUMBER_CARDS_PLAYER

def main():

    dealer = Dealer()
    player_01 = Player("Player01")
    player_02 = Player("Player02")
    
    dealer.deck.start_new_deck()
    dealer.shuffle_deck()

    player_01.pick_up_cards(dealer.deal(NUMBER_CARDS_PLAYER))
    player_02.pick_up_cards(dealer.deal(NUMBER_CARDS_PLAYER))

    dealer.check_winner(player_01, player_02)

if __name__ == "__main__":
    main()