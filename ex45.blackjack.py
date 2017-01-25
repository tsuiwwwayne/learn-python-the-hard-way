# Learn Python the Hard Way
# Exercise 45 - Blackjack

from sys import exit
import random

class Engine(object):

    def run(self):
        print "-" * 30
        print "Welcome to Wayne's Blackjack table!"
        print "-"  * 30
        self.menu()

    def menu(self):

        print """
        Menu:
        1. Start Game
        2. Rules
        3. Exit
        """

        try:
            menu_choice = int(raw_input("> "))
        except ValueError:
            print "Invalid Menu Choice. Try again."
            self.menu()

        if menu_choice == 1:
            Blackjack().start()

        elif menu_choice == 2:
            Rules().show()
            self.menu()

        elif menu_choice == 3:
            print "Thanks for playing!"
            exit(1)

        else:
            print "Invalid Menu Choice. Try again."
            self.menu()

class Rules(object):

    def show(self):
        print """
        Objective: Beat the dealer by getting a count as close to 21 as possible, without going over 21.\n
        Rules:
        \t1. Card Values/Scoring - It is up to each individual player if an ace is worth 1 or 11.
        \t2. Face cards are 10 and any other card is its pip value.
        \t3. You'll be dealt two cards face up.
        \t4. If you want another card to try and get you closer to 21, you 'Hit'.
        \t5. To stick with what you've got, you 'Stand'.
        \t6. If you're dealt an ace and 10 as your first two cards, that's a blackjack.
        \t7. This is an automatic win for you unless the dealer gets the same. If this happens, it's called a push and no one wins.
        """

class Blackjack(object):

    game_point = 0
    current_score = [0, 0]
    dealer_hand = []
    player_hand = []
    limit_hand_value = 21
    stand_hand_value = 17
    power_cards = ["Ace", "10", "Jack", "Queen", "King"]

    def get_game_point(self):
        return self.game_point

    def set_game_point(self, gp):
        self.game_point = gp

    def reset_score(self):
        self.current_score = [0, 0]

    def get_current_score(self):
        return self.current_score

    def set_dealer_score(self, dealer_score):
        self.current_score[0] = dealer_score

    def set_player_score(self, player_score):
        self.current_score[1] = player_score

    def get_hand_value(self, hand):
        total_value = 0
        num_of_aces = 0
        num_of_deductions_avail = 0
        num_of_cards_in_hand = len(hand)
        for each_card in hand:
            value = each_card.split(' ', 1)[0]
            if value == self.power_cards[0]:
                num_of_aces += 1
                num_of_deductions_avail += 1
                total_value += 11
            elif value in self.power_cards:
                total_value += 10
            else:
                total_value += int(value)

        while total_value > self.limit_hand_value and num_of_aces > 0 and num_of_deductions_avail > 0:
            total_value -= 10 # Ace value reduced from 11 to 1
            num_of_deductions_avail -= 1

        return total_value

    def start(self):
        print "How many games to victory?"
        try:
            self.game_point = int(raw_input("> "))
        except ValueError:
            print "Invalid. Input integer."
            return self.start()
        self.set_game_point(self.game_point)
        self.reset_score()

        deck_of_cards = Deck().get_cards()

        while self.game_point != max(self.current_score):
            self.show_score()
            self.shuffle_deck(deck_of_cards)
            self.deal(deck_of_cards)
            self.show_table(False)
            if self.check_blackjack():
                continue
            else:
                pass

            player_stand = False
            player_busted = False

            while not player_stand and not player_busted:
                player_choice = self.player_decision()

                if player_choice == 1:
                    self.hit(deck_of_cards, self.player_hand)
                    self.show_table(False)
                    player_busted = self.if_player_busted(self.player_hand)
                elif player_choice == 2:
                    player_stand = True
                else:
                    pass

            if player_busted:
                print "Dealer wins the round!"
                self.set_dealer_score(self.current_score[0]+1)
                continue
            else:
                pass

            self.dealer_decision(deck_of_cards)

            self.show_hand()

        self.show_score()
        self.finished()

    def finished(self):
        final_score = self.get_current_score()
        if final_score[0] > final_score[1]:
            print "You Lose! Dealer Win!"
        elif final_score[0] < final_score[1]:
            print "Congratulations! You Won!"
        else:
            print "It's a draw!"
        Engine().menu()

    def show_score(self):
        print """
        \tGame to %d
        Score:
        \tDealer: %d
        \tPlayer: %d
        """ % (self.game_point, self.current_score[0], self.current_score[1])

    def shuffle_deck(self, deck):
        deck.extend(self.player_hand)
        deck.extend(self.dealer_hand)
        self.player_hand[:] = []
        self.dealer_hand[:] = []
        random.shuffle(deck)

    def deal(self, deck):
        for i in range(0,2):
            self.player_hand.append(deck.pop(0))
            self.dealer_hand.append(deck.pop(0))

    def show_table(self, show_hand):
        if show_hand:
            print "Dealer have: ", self.dealer_hand
            print "Hand Value:", self.get_hand_value(self.dealer_hand)
            print "You have: ", self.player_hand
            print "Hand value:", self.get_hand_value(self.player_hand)
        else:
            print "Dealer have: ['HIDDEN']", self.dealer_hand[1:len(self.dealer_hand)]
            print "You have: ", self.player_hand
            print "Hand value:", self.get_hand_value(self.player_hand)


    def check_blackjack(self):
        d_bj = self.dealer_has_blackjack()
        p_bj = self.player_has_blackjack()
        if d_bj and p_bj:
            print "Both of you got blackjacks!"
            self.set_dealer_score(self.current_score[0]+1)
            self.set_player_score(self.current_score[1]+1)
            return True
        elif d_bj:
            print "Dealer has a blackjack!"
            self.set_dealer_score(self.current_score[0]+1)
            return True
        elif p_bj:
            print "Player got a blackjack!"
            self.set_player_score(self.current_score[1]+1)
            return True
        else:
            return False

    def dealer_has_blackjack(self):
        first_card = self.dealer_hand[0].split(' ', 1)[0]
        second_card = self.dealer_hand[1].split(' ', 1)[0]
        if (first_card == self.power_cards[0] and second_card in self.power_cards) or (first_card in self.power_cards and second_card == self.power_cards[0]):
            return True
        else:
            return False

    def player_has_blackjack(self):
        first_card = self.player_hand[0].split(' ', 1)[0]
        second_card = self.player_hand[1].split(' ', 1)[0]
        if (first_card == self.power_cards[0] and second_card in self.power_cards) or (first_card in self.power_cards and second_card == self.power_cards[0]):
            return True
        else:
            return False

    def player_decision(self):

        options = [
            "1. Hit",
            "2. Stand"
        ]

        must_hit = None

        player_hand_value = self.get_hand_value(self.player_hand)

        if player_hand_value < self.stand_hand_value:
            must_hit = True
            print options[0]
        else:
            must_hit = False
            print options[0]
            print options[1]

        while True:
            try:
                choice = int(raw_input("> "))
                if must_hit == True and choice != 1:
                    continue
                elif choice != 1 and choice != 2:
                    continue
                else:
                    pass
                break
            except ValueError:
                print "Invalid. Input integer choice."

        return choice


    def hit(self, deck, hand):
        hand.append(deck.pop(0))

    def if_player_busted(self, hand):
        exposed_hand_value = self.get_hand_value(hand[1:len(hand)])
        if exposed_hand_value >= self.limit_hand_value:
            return True
        else:
            return False

    def dealer_decision(self, deck):

        dealer_hand_value = self.get_hand_value(self.dealer_hand)
        dealer_busted = False

        while dealer_hand_value < self.stand_hand_value:
            self.hit(deck, self.dealer_hand)
            self.show_table(False)
            dealer_hand_value = self.get_hand_value(self.dealer_hand)

        # Algorithm to implement in order to beat human
        exposed_player_hand_value = self.get_hand_value(self.player_hand[1:len(self.player_hand)])
        player_likely_to_bust = self.limit_hand_value - exposed_player_hand_value < 3

        dealer_busted = self.get_hand_value(self.dealer_hand) > self.limit_hand_value
        dealer_likely_to_bust = self.limit_hand_value - dealer_hand_value < 3

        while not dealer_busted and not dealer_likely_to_bust and not player_likely_to_bust:

            dealer_hand_value = self.get_hand_value(self.dealer_hand)

            if dealer_hand_value - exposed_player_hand_value < 6:
                self.hit(deck, self.dealer_hand)
                self.show_table(False)
                return self.dealer_decision(deck)
            else:
                break

            dealer_busted = self.get_hand_value(self.dealer_hand) > self.limit_hand_value

    def show_hand(self):
        self.show_table(True)

        dealer_hand_value = self.get_hand_value(self.dealer_hand)
        player_hand_value = self.get_hand_value(self.player_hand)

        dealer_overlimit = dealer_hand_value > self.limit_hand_value
        player_overlimit = player_hand_value > self.limit_hand_value

        if (dealer_overlimit and player_overlimit) or (dealer_hand_value == player_hand_value):
            print "Draw!"
        elif dealer_overlimit:
            print "Player wins the round!"
            self.set_player_score(self.current_score[1]+1)
        elif player_overlimit:
            print "Dealer wins the round!"
            self.set_dealer_score(self.current_score[0]+1)
        elif dealer_hand_value > player_hand_value:
            print "Dealer wins the round!"
            self.set_dealer_score(self.current_score[0]+1)
        elif player_hand_value > dealer_hand_value:
            print "Player wins the round!"
            self.set_player_score(self.current_score[1]+1)
        else:
            pass


class Deck(object):

    cards = [
        "Ace of Diamonds",
        "2 of Diamonds",
        "3 of Diamonds",
        "4 of Diamonds",
        "5 of Diamonds",
        "6 of Diamonds",
        "7 of Diamonds",
        "8 of Diamonds",
        "9 of Diamonds",
        "10 of Diamonds",
        "Jack of Diamonds",
        "Queen of Diamonds",
        "King of Diamonds",
        "Ace of Clubs",
        "2 of Clubs",
        "3 of Clubs",
        "4 of Clubs",
        "5 of Clubs",
        "6 of Clubs",
        "7 of Clubs",
        "8 of Clubs",
        "9 of Clubs",
        "10 of Clubs",
        "Jack of Clubs",
        "Queen of Clubs",
        "King of Clubs",
        "Ace of Hearts",
        "2 of Hearts",
        "3 of Hearts",
        "4 of Hearts",
        "5 of Hearts",
        "6 of Hearts",
        "7 of Hearts",
        "8 of Hearts",
        "9 of Hearts",
        "10 of Hearts",
        "Jack of Hearts",
        "Queen of Hearts",
        "King of Hearts",
        "Ace of Spades",
        "2 of Spades",
        "3 of Spades",
        "4 of Spades",
        "5 of Spades",
        "6 of Spades",
        "7 of Spades",
        "8 of Spades",
        "9 of Spades",
        "10 of Spades",
        "Jack of Spades",
        "Queen of Spades",
        "King of Spades"
    ]

    def get_cards(self):
        return self.cards

Engine().run()
