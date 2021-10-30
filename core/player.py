import core.helper as helper

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.power = 0

    def __repr__(self):
        return f"{self.show_hand()}"

    def pick_up_cards(self, cards):
        self.hand += cards
        self.__organize_hand()

    def show_hand(self):
        cards = ""
        
        if type(self.hand[0]) == type([]):
            for group in self.hand:
                if type(group) != type([]):
                    cards += group['name']
                else:
                    cards += "".join([card['name'] for card in group ])
        else:
            cards = "".join([card['name'] for card in self.hand ])
        
        return cards

    def __organize_hand(self):

        types = self.__get_types_hand()
        self.__sort_raw_hand()

        wild = self.hand.pop() if "*" in types else None
              
        if len(types) > 4 :
            self.__organize_sequence(wild)
        else:
            self.__organize_groups(wild, types)
            

    def __organize_groups(self, wild, types):
        grouped_list = []

        for type in types:
            list_same_type = []
            for card in self.hand:
                if type == card['name']:
                    list_same_type.append(card)
            if list_same_type:
                grouped_list.append(list_same_type)

        self.hand = sorted(
            grouped_list, 
            key=lambda group: (len(group), group[0]['value']), 
            reverse=True
        )

        if wild:
            self.hand[0].append(wild)

    def __organize_sequence(self, wild):
        is_straight = helper.is_straight(self.hand)

        if is_straight:
            self.hand.reverse()
            if wild:
                self.hand.append(wild)
        else:
            if wild:
                new_hand = []
                new_hand.append( [self.hand[0], wild])

                for card in self.hand[1:]:
                    new_hand.append([card])

                self.hand = new_hand

    def __get_types_hand(self):
        return set([ card['name'] for card in self.hand ])

    def __sort_raw_hand(self):
        self.hand.sort(key=lambda card: card['value'],reverse=True)
