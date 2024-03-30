import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.value == "Ace":
                num_aces += 1
            elif card.value in ["Jack", "Queen", "King"]:
                value += 10
            else:
                value += int(card.value)

        for _ in range(num_aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        return value


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


def play_blackjack():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    while True:
        print("\nГравцева рука:")
        for card in player_hand.cards:
            print(card)
        print(f"Загальна сума: {player_hand.get_value()}")

        if player_hand.get_value() > 21:
            print("Перебір!")
            break

        action = input("Будете взяти ще одну карту? (Так/Ні): ").lower()
        if action == "так":
            player_hand.add_card(deck.deal_card())
        else:
            break

    print("\nРука дилера:")
    for card in dealer_hand.cards:
        print(card)
    print(f"Загальна сума: {dealer_hand.get_value()}")

    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
    print("\nРука дилера:")
    for card in dealer_hand.cards:
        print(card)
    print(f"Загальна сума: {dealer_hand.get_value()}")

    player_score = player_hand.get_value()
    dealer_score = dealer_hand.get_value()

    if player_score > 21:
        print("Гравець перебрав. Дилер виграв!")
    elif dealer_score > 21:
        print("Дилер перебрав. Гравець виграв!")
    elif player_score > dealer_score:
        print("Гравець виграв!")
    elif dealer_score > player_score:
        print("Дилер виграв!")
    else:
        print("Нічия!")


play_blackjack()
