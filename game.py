import time

import helpers


def main():

    # Get users name
    print('Welcome to BlackJack')
    time.sleep(1)
    player_name = helpers.get_users_name()

    while True:

        deck = helpers.create_deck()

        # instantiate player and dealer objects
        player_1 = helpers.Player(player_name)
        dealer = helpers.Player('Dealer')

        # deal initial 4 cards
        helpers.deal_card(player_1, deck)
        helpers.deal_card(dealer, deck)
        helpers.deal_card(player_1, deck)
        helpers.deal_card(dealer, deck)

        # show cards to user

        # player 1 cards

        helpers.print_all_cards(player_1)

        # dealer (hide first card, show 2nd)
        time.sleep(1)
        print('Dealer cards:\nUnturned')
        time.sleep(1)
        print(dealer.cards[1])
        time.sleep(1)

        # if user has black jack, set stick to true and move onto dealer
        if helpers.is_blackjack(player_1):
            player_1.stick = True
            print('You got Blackjack!')

        # stick/twist user
        if not player_1.stick:
            helpers.player_extra_cards_sequence(player_1, deck)
        if player_1.bust:
            print('You bust, Dealer Wins!')
        else:
            # show both dealers cards
            helpers.print_all_cards(dealer)
            # check if dealer has blackjack
            if helpers.is_blackjack(dealer):
                print('Blackjack! Dealer Wins!')
            elif player_1.blackjack:
                print('{} Wins!'.format(player_1))

            else:
                # neither player has blackjack and user isnt bust
                # dealer stick/twist
                helpers.dealer_extra_cards_sequence(dealer, player_1, deck)
                if not dealer.bust:
                    winner = helpers.calculate_winner(player_1, dealer)
                    print('{} Wins!'.format(winner))
                else:
                    print('{} Wins!'.format(player_1))

        input('Press ENTER play again')


if __name__ == "__main__":
    main()


