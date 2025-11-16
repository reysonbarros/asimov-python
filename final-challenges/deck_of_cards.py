import random

print('Deck of cards')

def generate_deck(copy=2, wildcard=True, shuffle=True):
    deck = []

    naipes = list('♠♥♦♣')
    numbers = list('A23456789') + ['10'] + list('JQK')

    for _ in range(copy):
        for naipe in naipes:
            for number in numbers:
                card = number + naipe
                deck.append(card)
        if wildcard:
            deck.extend(['JK1', 'JK2'])

    if shuffle:
        random.shuffle(deck)

    return deck

def show_deck(deck):
    print(f'There are {len(deck)} cards from deck')
    print('Cards:')
    print(', '.join(deck))

def deal_cards(deck, total_players=4, cards_by_player=5):
    players = {}

    for i in range(total_players):
        hand = []
        while len(hand) < cards_by_player:
            card = deck.pop(0)
            hand.append(card)
        player_name = f'Player {i + 1}'
        players[player_name] = hand

    return players

def show_players(players):
    for player, hand in players.items():
        print(f'There are {len(hand)} cards with {player}')
        print('Cards:')
        for card in hand:
            print(f' -> {card}')

deck = generate_deck()
show_deck(deck)

players = deal_cards(deck)
show_deck(deck)
show_players(players)
