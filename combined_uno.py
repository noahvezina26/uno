# Alex Segal, Noah Vezina + Toranj Najafi, Zaccaria Broomhall Bedont
# Implementation: skips player turn if card is invalid or if no valid cards are in hand & plus two

import random


def start_game():
    # SET UP OF UNO
    colours = ("Red", "Yellow", "Green", "Blue")
    ranks = list(range(1, 11)) + ["+2"]

    # CREATE DECK
    deck = [(rank, colour) for rank in ranks for colour in colours]

    # SHUFFLE DECK
    random.shuffle(deck)

    # GIVE OUT SEVEN CARDS PER PERSON
    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]

    # CENTRAL CARD
    central_card = deck.pop(0)

    main_loop(p1, p2, deck, central_card, 0)


def main_loop(p1, p2, deck, central_card, whose_turn):

    while p1 and p2:

        print(f"Here is player {whose_turn}'s hand: {p1}")
        print(f"The central card is {central_card}")

        # GIVE USER CHOICE: PLAY OR DRAW

        response = int(input("\nDo you want to (0) draw or (1) play? "))

        if response:
            # PLAY
            if not can_play(p1, central_card):  # IMPLEMENTED FEATURE
                print("No cards can be played, your turn has been skipped")
            else:
                player_choice = int(input("What card do you want to play? ")) - 1
                valid = valid_play(central_card, p1[player_choice])
                if valid:
                    if p1[player_choice][1] == "+2":
                        p2 += [deck.pop(0) for _ in range(2)]
                    central_card = p1.pop(player_choice)
                else:  # IMPLEMENTED FEATURE
                    print("Invalid card, your turn has been skipped\n")
        else:
            # DRAW
            p1.append(deck.pop(0))
            print("A card has been added to your hand\n")

        # SWITCH DECKS
        p1, p2 = p2, p1
        whose_turn = (whose_turn + 1) % 2

    if not p1:
        print("Player 1 won!")
    else:
        print("Player 2 won!")


def can_play(hand, central_card):  # IMPLEMENTED FEATURE
    for card in hand:
        if card[0] == central_card[0] or card[1] == central_card[1]:
            return True
    return False


def valid_play(central_card, card_played):
    return card_played[0] == central_card[0] or card_played[1] == central_card[1]


start_game()
