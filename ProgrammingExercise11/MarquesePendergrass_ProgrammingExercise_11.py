import random

# Deck object
class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0

    def deal(self):
        # return next card from the list
        card = self.card_list[self.current_card]
        self.current_card += 1
        return card


# lists used to turn a card number into rank and suit text
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['clubs', 'diamonds', 'hearts', 'spades']


def card_to_str(card):
    # convert number 0–51 into "rank of suit"
    return ranks[card % 13] + " of " + suits[card // 13]


def main():
    deck = Deck(52)

    # deal an initial 5-card poker hand
    hand = [deck.deal() for _ in range(5)]

    print("Your hand:")
    for i, c in enumerate(hand, start=1):
        print(i, ":", card_to_str(c))

    # prompt user for card positions to replace
    choice = input("Enter card numbers to replace: ")

    # split on commas and replace each selected card
    for item in choice.split(','):
        pos = int(item)          # convert to integer position
        hand[pos - 1] = deck.deal()

    print("\nAfter draw:")
    for i, c in enumerate(hand, start=1):
        print(i, ":", card_to_str(c))


main()