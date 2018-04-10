import unittest

from helpers import is_blackjack, Card, Player, calculate_winner, calc_score, create_deck, set_user_status


class GameTests(unittest.TestCase):

    def test_deck_4_aces(self):
        deck = create_deck()
        aces = [card for card in deck if card.value == 1]
        self.assertEqual(len(aces), 4)

    def test_deck_13_suit(self):
        deck = create_deck()
        spades = [card for card in deck if card.suit == 'Spades']
        self.assertEqual(len(spades), 13)

    def test_deck_num_of_cards(self):
        self.assertEqual(len(create_deck()), 52)

    def test_blackjack_true(self):
        card_1 = Card(11, 'Spades')
        card_2 = Card(1, 'Spades')
        test_player = Player('Test')
        test_player.cards.extend((card_1, card_2))
        self.assertIs(is_blackjack(test_player), True)

    def test_blackjack_False(self):
        card_1 = Card(10, 'Spades')
        card_2 = Card(1, 'Spades')
        test_player = Player('Test')
        test_player.cards.extend((card_1, card_2))
        self.assertIs(is_blackjack(test_player), False)

    def test_blackjack_2_aces(self):
        card_1 = Card(1, 'Spades')
        card_2 = Card(1, 'Spades')
        test_player = Player('Test')
        test_player.cards.extend((card_1, card_2))
        self.assertIs(is_blackjack(test_player), False)

    def test_blackjack_2_pictures(self):
        card_1 = Card(11, 'Spades')
        card_2 = Card(11, 'Spades')
        test_player = Player('Test')
        test_player.cards.extend((card_1, card_2))
        self.assertIs(is_blackjack(test_player), False)

    def test_calc_winner_user(self):
        card_1 = Card(10, 'Spades')
        card_2 = Card(9, 'Spades')
        test_player = Player('Test')
        card_3 = Card(10, 'Spades')
        card_4 = Card(8, 'Spades')
        test_dealer = Player('Dealer')
        test_player.cards.extend((card_1, card_2))
        test_dealer.cards.extend((card_3, card_4))
        self.assertEqual(calculate_winner(test_player, test_dealer), test_player)

    def test_calc_winner_dealer(self):
        card_1 = Card(10, 'Spades')
        card_2 = Card(9, 'Spades')
        test_player = Player('Test')
        card_3 = Card(10, 'Spades')
        card_4 = Card(8, 'Spades')
        card_5 = Card(3, 'Spades')
        test_dealer = Player('Dealer')
        test_player.cards.extend((card_1, card_2))
        test_dealer.cards.extend((card_3, card_4, card_5))
        self.assertEqual(calculate_winner(test_player, test_dealer), test_dealer)

    def test_calc_score(self):
        card_1 = Card(10, 'Spades')
        card_2 = Card(9, 'Spades')
        test_player = Player('Test')
        test_player.cards.extend((card_1, card_2))
        self.assertEqual(calc_score(test_player), 19)

    def test_calc_score_more_cards(self):
        card_3 = Card(1, 'Spades')
        card_4 = Card(8, 'Spades')
        card_5 = Card(3, 'Spades')
        card_6 = Card(2, 'Spades')
        card_7 = Card(1, 'Spades')
        test_dealer = Player('Dealer')
        test_dealer.cards.extend((card_3, card_4, card_5, card_6, card_7))
        self.assertEqual(calc_score(test_dealer), 15)

    def test_calc_score_aces(self):
        card_3 = Card(1, 'Spades')
        card_4 = Card(1, 'Spades')
        test_dealer = Player('Dealer')
        test_dealer.cards.extend((card_3, card_4))
        self.assertEqual(calc_score(test_dealer), 12)

    def test_calc_score_aces_and_picture(self):
        card_3 = Card(1, 'Spades')
        card_4 = Card(1, 'Spades')
        card_5 = Card(11, 'Spades')
        test_dealer = Player('Dealer')
        test_dealer.cards.extend((card_3, card_4, card_5))
        self.assertEqual(calc_score(test_dealer), 12)

    # card class tests

    def test_card_name(self):

        card1 = Card(1, 'Spades')
        card2 = Card(11, 'Spades')
        card3 = Card(4, 'Spades')
        self.assertEqual(card1.card_name, 'Ace')
        self.assertEqual(card2.card_name, 'Jack')
        self.assertEqual(card3.card_name, 4)

    def test_card_str(self):

        card1 = Card(1, 'Spades')
        card2 = Card(11, 'Clubs')
        card3 = Card(4, 'Hearts')
        self.assertEqual(str(card1), 'Ace of Spades')
        self.assertEqual(str(card2), 'Jack of Clubs')
        self.assertEqual(str(card3), '4 of Hearts')

    def test_card_real_value(self):

        card1 = Card(13, 'Spades')
        card2 = Card(11, 'Clubs')
        card3 = Card(4, 'Hearts')
        self.assertEqual(card1.real_value, 10)
        self.assertEqual(card2.real_value, 10)
        self.assertEqual(card3.real_value, 4)

