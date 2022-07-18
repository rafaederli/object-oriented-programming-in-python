from random import choice, shuffle
from time import sleep
from typing import Union, List, Tuple

from constants import start_score_T


class TwentyOneGame:
    def __init__(self) -> None:
        self.__card_list: List[Union[int, str]] = [2, 3, 4, 5, 6, 7, 8, 9,
                                                   10, 'A', 'K', 'Q', 'J'] * 4
        self.player_score: int = start_score_T
        self.dealer_score: int = start_score_T
        self.__play()

    @staticmethod
    def __header() -> None:
        print('TWENTY ONE NUMBER GAME')
        print(f'Try to adding twenty-one points.')
        print(f'The game starts with the player and the dealer (opponent)'
              f' each receiving two cards.')
        print(f'After evaluating the cards received, the player chooses one'
              f' of the following options:')
        print('[1] Stand: When the player does not want to receive any more'
              ' cards.')
        print('[2] Hit: When the player wants to receive one more card.')
        print('[3] Double: When the player wants to double the bet and'
              ' receive one more card.')
        print('[4] Surrender: When the player wants to give up the game and'
              ' pay half the bet.\n')
        print('Then the player and dealer make a bet.')
        print(f'\tNote 1: Both start the game with {start_score_T} points.\n')
        print('CARD VALUES:')
        print('2, 3, 4, 5, 6, 7, 8, 9, 10, Ace(= 1 ou 11),'
              ' K(= 10), Q(= 10), J(= 10)\n')

    @staticmethod
    def __show_the_score(player_score: int, dealer_score: int) -> None:
        """
        This function presents the games.
        """
        print('SCORE')
        print('-------------------')
        print(f'Player: {player_score} points')
        print('-------------------')
        print(f'Dealer: {dealer_score} points')
        print('-------------------')
        print()

    @staticmethod
    def __give_the_cards(card_list: List[Union[int, str]],
                         player_game: List[Union[int, str]],
                         dealer_game: List[Union[int, str]]
                         ) -> Tuple[List[Union[int, str]],
                                    List[Union[int, str]],
                                    List[Union[int, str]]]:
        """
        This function gives two cards for the player and dealer from card list
        :param card_list: Card list
        :param player_game: Player game
        :param dealer_game: Dealer game
        :return: Card list, player game and dealer game
        """
        for game in [player_game, dealer_game]:
            for element in range(0, 2):
                card: int | str = choice(card_list)
                card_list.remove(card)
                game.append(card)
        return card_list, player_game, dealer_game

    @staticmethod
    def __give_one_card(card_list: List[Union[int, str]],
                        game: List[Union[int, str]]
                        ) -> Tuple[List[Union[int, str]],
                                   List[Union[int, str]]]:
        """
        This function gives one card from card list
        :param card_list: Card list
        :param game: List of cards
        :return: Card list and game
        """
        card: int | str = choice(card_list)
        card_list.remove(card)
        game.append(card)
        return card_list, game

    @staticmethod
    def __show_the_games(player_game: List[Union[int, str]],
                         dealer_game: List[Union[int, str]]) -> None:
        """
        This function shows player game and the first card of the dealer
        """
        print('GAMES')
        print('--------------------')
        print('Player')
        for index, element in enumerate(player_game):
            print(f'card {index + 1}: {element}')
        print('--------------------')
        print('Dealer: ')
        print(f'card 1: {dealer_game[0]}')
        print('--------------------')
        print()

    @staticmethod
    def __assign_to_variable_bet(dealer_score: int, count: int) -> int:
        """
        This function inputs the bet and handle possible typos
        :param count: Count
        :return: Bet
        """
        while True:
            try:
                bet: int = int(input(f'Match {count}. How much would you '
                                     f'like to bet? '))
            except ValueError:
                print('Error! Choose a integer.')
            else:
                if bet > dealer_score:
                    print('Error! The bet must to be less than or equal to '
                          'the opponent amount.')
                else:
                    print()
                    break
        return bet

    @staticmethod
    def __split_the_aces_of_the_game(game: List[Union[int, str]]
                                     ) -> Tuple[List[str],
                                                List[Union[int, str]]]:
        """
        This function divides the game into two lists: a list with aces and a
        list without aces
        :param game: List of cards
        :return: List with aces and list without aces
        """
        list_with_aces: List[str] = []
        list_without_aces: List[Union[int, str]] = []
        for card in game:
            if card == 'A':
                list_with_aces.append(card)
            else:
                list_without_aces.append(card)
        return list_with_aces, list_without_aces

    def __sum_cards(self, game: List[Union[int, str]]) -> int:
        """
        This function adds a list of cards, considering that the sum must not
        be greater than twenty-one
        :param game: List of cards
        :return: Sum of the list
        """
        # Split the list into a list without aces and a list with aces
        list_with_aces, list_without_aces = \
            self.__split_the_aces_of_the_game(game)

        # Add the list of cards without aces
        sum_of_cards: int = 0
        for card in list_without_aces:
            if type(card) is str:
                card = 10
            sum_of_cards += card

        # Add the aces
        # (Note: if possible, the sum should be less than twenty-one)
        if len(list_with_aces) > 0:
            for element in range(len(list_with_aces)):
                if sum_of_cards < 21 and sum_of_cards + 11 <= 21:
                    sum_of_cards += 11
                else:
                    sum_of_cards += 1

        return sum_of_cards

    def __player_action(self, card_list: List[Union[int, str]],
                        player_game: List[Union[int, str]],
                        dealer_bet: int, player_bet: int
                        ) -> Tuple[List[Union[int, str]],
                                   List[Union[int, str]],
                                   int, int, bool]:
        """
        This function inputs and selects player action
        :param card_list: Card list
        :param player_game: Player game
        :param dealer_bet: Dealer bet
        :param player_bet: Player bet
        :return: Card list, player game, player bet, dealer bet, stop
        """
        print('Choose a option: ')
        print('[1] Stand')
        print('[2] Hit')
        print('[3] Double')
        print('[4] Surrender')
        print()
        while True:
            try:
                action = int(input('Option: '))
                print()
            except ValueError:
                print('Error! Choose a integer.')
            else:
                # Stand
                if action == 1:
                    stop = True
                    break
                # Hit
                elif action == 2:
                    stop = False
                    card_list, player_game = \
                        self.__give_one_card(card_list, player_game)
                    break
                # Double
                elif action == 3:
                    stop = False
                    card_list, player_game = \
                        self.__give_one_card(card_list, player_game)
                    player_bet *= 2
                    dealer_bet *= 2
                    break
                # Surrender
                elif action == 4:
                    stop = True
                    player_bet *= 0.5
                    break
        return card_list, player_game, player_bet, dealer_bet, stop

    def __dealer_action(self, card_list: List[Union[int, str]],
                        dealer_game: List[Union[int, str]],
                        dealer_bet: int) -> Tuple[List[Union[int, str]],
                                                  List[Union[int, str]],
                                                  int, bool]:
        """
        This function selects dealer action
        :param card_list: Card list
        :param dealer_game: Dealer game
        :param dealer_bet: Dealer bet
        :return: Card list, dealer game, dealer bet, stop condition
        """
        # Stand
        if 17 <= self.__sum_cards(dealer_game) <= 21:
            stop = True
            print('[1] Stand')
            print()
            return card_list, dealer_game, dealer_bet, stop
        # Hit
        elif self.__sum_cards(dealer_game) < 17:
            stop = False
            deck_cards, dealer_game = \
                self.__give_one_card(card_list, dealer_game)
            print('[2] Hit')
            print()
            return card_list, dealer_game, dealer_bet, stop
        # Surrender
        elif self.__sum_cards(dealer_game) > 21:
            stop = True
            dealer_bet *= 0.5
            print('[4] Surrender')
            print()
            return card_list, dealer_game, dealer_bet, stop

    @ staticmethod
    def __if_player_wins(player_score: int,
                         dealer_score: int,
                         dealer_bet: int) -> Tuple[int, int]:
        """
        This function adds the bet to the player's amount and subtracts it
        from the dealer's amount
        :param player_score: Player amount
        :param dealer_score: Dealer amount
        :param dealer_bet: Dealer bet
        :return: Player amount and dealer amount
        """
        player_score += dealer_bet
        dealer_score -= dealer_bet
        return player_score, dealer_score

    @staticmethod
    def __if_dealer_wins(player_score: int,
                         dealer_score: int,
                         player_bet: int) -> Tuple[int, int]:
        """
        This function adds the bet to the dealer's amount and subtracts it
        from the player's amount
        :param player_score: Player amount
        :param dealer_score: Dealer amount
        :param player_bet: Player bet
        :return: Player amount and dealer amount
        """
        dealer_score += player_bet
        player_score -= player_bet
        return player_score, dealer_score

    @staticmethod
    def __scoreboard(player_score: int, dealer_score: int) -> None:
        """
        This function shows the game scores
        :param player_score: Player amount
        :param dealer_score: Player amount
        """
        print('SCORES')
        print('-------------------')
        print(f'Player: {player_score} points')
        print('-------------------')
        print(f'Dealer: {dealer_score} points')
        print('-------------------')
        print()

    def __evaluation(self, player_game: List[Union[int, str]],
                     dealer_game: List[Union[int, str]],
                     player_score: int, dealer_score: int,
                     player_bet: int, dealer_bet: int
                     ) -> Tuple[int, int]:
        """
        This functions evaluates who won the match
        :param player_game: Player game
        :param dealer_game: Dealer game
        :param player_score: Player amount
        :param dealer_score: Dealer amount
        :param player_bet: Player bet
        :param dealer_bet: Dealer bet
        :return: Player amount and dealer amount
        """
        # Add up the cards lists
        player_amount = self.__sum_cards(player_game)
        dealer_amount = self.__sum_cards(dealer_game)

        # Show match results
        print('MATCH RESULT')
        print('-------------------')
        for tpl in [('Player', player_game, player_amount, player_bet),
                    ('Dealer', dealer_game, dealer_amount, dealer_bet)]:
            print(f'{tpl[0]} cards: ', end='')
            for index, card in enumerate(tpl[1]):
                if index + 1 != len(tpl[1]):
                    print(card, end=', ')
                else:
                    print(card, end='.\n')
            print(f'Sum: {tpl[2]}')
            print(f'Bet: {tpl[3]}')
            print('--------------------')
        print()

        # Evaluate whether there is some winner or a tie
        if player_amount <= 21 and dealer_amount <= 21:
            # If both sums (scores) are less than twenty-one
            if dealer_amount < player_amount:
                print('Congratulations! You won this match.')
                print()
                player_score, dealer_score = \
                    self.__if_player_wins(player_score,
                                          dealer_score,
                                          dealer_bet)
            elif player_amount < dealer_amount:
                print('You lost this match.')
                print()
                player_score, dealer_score = \
                    self.__if_dealer_wins(player_score,
                                          dealer_score,
                                          player_bet)
            else:
                print('There was a tie.')
                print()

        elif player_amount <= 21 < dealer_amount:
            # If only the player's sum (score) is less than twenty-one
            print('Congratulations! You won this match.')
            print()
            player_score, dealer_score = \
                self.__if_player_wins(player_score,
                                      dealer_score,
                                      dealer_bet)

        elif dealer_amount <= 21 < player_amount:
            # If only the dealer's sum (score) is less than twenty-one
            print('You lost this match.')
            print()
            player_score, dealer_score = \
                self.__if_dealer_wins(player_score,
                                      dealer_score,
                                      player_bet)

        else:
            # If both sums (scores) are greater than twenty-one
            print('There were no winners.')
            print()

        # Show game scores
        self.__scoreboard(player_score, dealer_score)

        return player_score, dealer_score

    def __play(self) -> None:
        """
        This function runs the game
        """

        self.__header()
        self.__scoreboard(self.player_score, self.dealer_score)

        count = 1
        while True:
            # Shuffle the card list
            shuffle(self.__card_list)

            # Create player and dealer game lists
            p_game = []
            d_game = []

            # Assign the bet amount
            bet = self.__assign_to_variable_bet(self.dealer_score, count)
            p_bet = bet
            d_bet = bet

            # Give the cards to player and dealer
            self.__card_list, p_game, d_game =\
                self.__give_the_cards(self.__card_list, p_game, d_game)

            while True:
                # Player decision-making block
                sleep(2)
                print(f'PLAYER TURN')
                sleep(2)
                print()

                self.__show_the_games(p_game, d_game)

                self.__card_list, p_game, p_bet, d_bet, stop =\
                    self.__player_action(self.__card_list,
                                         p_game, d_bet, p_bet)
                if stop:
                    break

            while True:
                # Dealer decision-making block
                sleep(2)
                print(f'DEALER TURN')
                sleep(2)
                print()

                self.__show_the_games(p_game, d_game)

                sleep(2)
                print('Playing ...')
                sleep(2)
                print()

                self.__card_list, d_game, d_bet, stop = \
                    self.__dealer_action(self.__card_list,
                                         d_game, d_bet)
                if stop:
                    break

            # Evaluate whether there is some winner or a tie in the match
            # And update the scores
            self.player_score, self.dealer_score = \
                self.__evaluation(p_game, d_game, self.player_score,
                                  self.dealer_score, p_bet, d_bet)

            # Evaluate whether there is some winner in the game
            if self.player_score < 1 or self.dealer_score < 1:
                if self.player_score > self.dealer_score:
                    print('Congratulations! You won the game.')
                    break
                else:
                    print('Try again. You lost the game.')
                    break
            count += 1
        print()


if __name__ == '__main__':
    TwentyOneGame()
