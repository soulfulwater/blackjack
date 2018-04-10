from random import shuffle

import time


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @property
    def card_name(self):
        if self.value == 1:
            return 'Ace'
        elif self.value == 11:
            return 'Jack'
        elif self.value == 12:
            return 'Queen'
        elif self.value == 13:
            return 'King'
        else:
            return self.value
    @property
    def real_value(self):
        if self.value == 11:
            return 10
        elif self.value == 12:
            return 10
        elif self.value == 13:
            return 10
        else:
            return self.value

    def __str__(self):
        return '{} of {}'.format(self.card_name, self.suit)


class Player:
    def __init__(self, player_name):
        self.cards = []
        self.name = player_name
        self.bust = False
        self.stick = False
        self.blackjack = False

    def __str__(self):
        return self.name




def is_blackjack(player):
    ace = False
    picture = False
    card_values_list = []
    # a card has to have a value of 1 and another card 11, 12, 13
    for card in player.cards:
        card_values_list.append(card.value)

    if 1 in card_values_list:
        ace = True
    for card in card_values_list:
        if card > 10:
            picture = True

    if ace and picture:
        player.blackjack = True
        return True
    else:
        return False


def calc_score(player):
    cards_values_list = [card.real_value for card in player.cards]
    if 1 in cards_values_list:
        high_ace_sum = sum(cards_values_list) + 10
        if high_ace_sum < 22:
            return high_ace_sum
    return sum(cards_values_list)


def set_user_status(score, player):
        if score > 21:
            player.bust = True
        if score == 21:
            player.stick = True
        return player


def player_extra_cards_sequence(player, deck):
    # player 1 hit/stick
    while not player.stick and not player.bust:
        try:
            choice = int(input('{} - Type 0 to stick or 1 to twist:'.format(player.name)))
            if choice < 0 or choice > 1:
                print('Not a valid option, please try again')
            elif choice == 1:
                deal_card(player, deck)
                card = player.cards[-1]
                print(card)
                time.sleep(1)
                score = calc_score(player)
                set_user_status(score, player)
                if player.bust:
                    break
                print('Your cards total {}'.format(score))
            elif choice == 0:
                player.stick = True
        except ValueError:
            print('Not a valid option, please try again')

def create_deck():
    suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs', ]
    deck = [Card(value, suit) for value in range(1, 14) for suit in suits]

    shuffle(deck)
    return deck

def deal_card(player, deck):
    player.cards.append(deck[0])
    deck.pop(0)


def get_users_name():
    valid_name = False
    while not valid_name:
        player_name = input('Please enter your name (Uppercase and Lowercase letters only):')
        if player_name.isalpha():
            return player_name


def print_all_cards(player):
    print("{}'s cards:".format(player))
    time.sleep(1)

    for card in player.cards:
        time.sleep(1)
        print(card)
    time.sleep(1)


def dealer_extra_cards_sequence(dealer, player, deck):
    dealer_score = calc_score(dealer)
    player_score = calc_score(player)

    while dealer_score < player_score and not dealer.bust:
        deal_card(dealer, deck)
        print(dealer.cards[-1])
        time.sleep(1)
        dealer_score = calc_score(dealer)
        print('Dealer cards total {}'.format(dealer_score))
        if dealer_score > 21:
            dealer.bust = True
            time.sleep(1)
            print('Dealer bust!')


def calculate_winner(player, dealer):
    user_score = calc_score(player)
    dealer_score = calc_score(dealer)
    print('{} score: {}'.format(player, user_score))
    print('{} score: {}'.format(dealer, dealer_score))
    if dealer_score >= user_score:
        return dealer
    else:
        return player
