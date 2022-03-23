# Dependencies
import random

# Generate New Deck of Cards
cards = ['A ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','J ','K ']
suits = ['\u2660','\u2663','\u2665','\u2666']
deck = [card+suit for suit in suits for card in cards]

# Function to print cards on the table
def summarize(deck, players, money, wagers, hits, final=False):
    # DEALER's CARDS
    print(f'-------------------------------------------')
    if final:
        print(f' Dealer showing:       {deck[players]}, {deck[players+players+1]}', end = '')
        if hits[-1] > 0:
            for hit in hits[-1]:
                print(f', {deck[hit]}', end='')
    else:
        print(f' Dealer showing:       {deck[players]}', end = '')
    print(f'\n-------------------------------------------')
    # PLAYER CARDS
    for player in range(players):
        print(f'Player {player+1} -- ${money[player]:.0f} on the Table --\n')
        print(f'    Current Bet:  ${wagers[player]:.0f}')
        print(f'   Current hand:       {deck[player]}, {deck[player+players+1]}', end='')
        for hit in hits[player]:
            print(f', {deck[hit]}', end='')
        print(f'\n-------------------------------------------')

# Function to give each player a turn
def play(deck, dealt, hits, players):
    hit = ''
    for player in range(players):
        while hit not in ['stay', 's']:
            hit = input(f"Player {player+1} - Would you like to hit ('h') or stay ('s')?\n").lower()
            if hit in ['hit','h']:
                dealt += 1
                hits[player].append(dealt)
                print(f'   Current hand:       {deck[player]}, {deck[player+players+1]}', end='')
                for hit in hits[player]:
                    print(f', {deck[hit]}', end='')
        print('\n-------------------------------------------')
    return hits

# INTRO
print('\n\n#############################################')
print('#####  Welcome to the Blackjack table!  #####')
print('#############################################')

# Check how many players there are -- eventually maybe move this into the while loop so players can join/leave more easily ?
players = 0
while players not in range(1,8):
    players = int(input('\nHow many players are with you?\nNote: Table seats up to 7\n'))
    # Reset money, wagers and hits lists based on player count
    money = [float(input(f'How much does Player {player+1} buy in for?\n')) for player in range(players)]
    wagers = [0 for player in range(players)]
    hits = [[] for player in range(players+1)] # Includes DEALER's hits as hits[-1]

# Start fresh deck, player, and hit counters
playing = True
while playing:
    # Shuffle the deck
    random.shuffle(deck)

    # Place bets
    print('\nPlace your bets!')
    for player in range(players):
        wagers[player] = float(input(f'How much is Player {player+1} betting?\n'))

    # Deal cards + print summary
    dealt = (int(players)+1)*2-1
    summarize(deck, players, money, wagers, hits, final=False)

    ################ need to modify to add insurance option if dealer showing an Ace

    # Loop to give each player a turn
    for player in range(players):
        hits = play(deck, dealt, hits, players)

