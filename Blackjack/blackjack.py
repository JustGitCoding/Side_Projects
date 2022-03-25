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
def player_turns(deck, dealt, hits, players):
    for player in range(players):
        hit = ['ask' for player in range(players)]
        while hit[player] in ['ask', 'hit', 'h']:
            hit[player] = input(f"Player {player+1} - Would you like to hit ('h') or stay ('s')?\n").lower()
            if hit[] in ['hit','h']:
                dealt += 1
                hits[player].append(dealt)
                print(f'   Current hand:       {deck[player]}, {deck[player+players+1]}', end='')
                #------- add something here
                # -------------- print total for the player
                for hit in hits[player]:
                    print(f', {deck[hit]}', end='')
                print('\n')
        print('\n-------------------------------------------')
    return hits

# Function to calculate a hand value
def calc_hand(hand):
    values_dict = {'2 ':2,'3 ':3,'4 ':4,'5 ':5,'6 ':6,'7 ':7,'8 ':8,'9 ':9,'10':10,'J ':10,'K ':10}
    hand_value = 0
    ace_count = 0
    for card in hand:
        if card[:1] != 'A':
            hand_value += values_dict[card[:2]]
        else:
            ace_count +=1
    for ace in range(ace_count):
        if hand_value + 11 <= 21:
            hand_value += 11
        else:
            hand_value += 1
    return hand_value

# INTRO
print('\n\n#############################################')
print('#####  Welcome to the Blackjack table!  #####')
print('#############################################')

# Check how many players there are -- eventually maybe move this into the while loop so players can join/leave more easily ?
players = 0
while players not in range(1,8):
    players = int(input('\nHow many players are with you?\nNote: Table seats up to 7\n'))
    # Reset money, wagers and hands lists based on player count
    money = [float(input(f'How much does Player {player+1} buy in for?\n')) for player in range(players)]
    wagers = [0 for player in range(players)]
    hits = [[] for player in range(players+1)] # Includes DEALER's hits as hits[-1] ######## DO WE STILL NEED THIS????
    hands = [[] for player in range(players+1)] # Includes DEALER's hand as hands[-1]

# Start fresh deck, player, and hit counters
table_money = 0
for m in money:
    table_money += m
while table_money > 0:
    # Shuffle the deck
    random.shuffle(deck)

    # Place bets
    print('\nPlace your bets!')
    for player in range(players):
        while money[player] >= wagers[player]:
            wagers[player] = float(input(f'Player {player+1} has ${money[player]} - How much would you like to bet?\n'))
            if wagers[player] > money[player]:
                wagers[player] = 0
                print(f'You only have ${money[player]}.')

    # Deal cards + print summary
    dealt = (int(players)+1)*2-1
    summarize(deck, players, money, wagers, hits, final=False)

    ################ need to modify to add insurance option if dealer showing an Ace

    # Loop to give each player a turn
    for player in range(players):
        hits = player_turns(deck, dealt, hits, players)

    # Run Function for Dealer's turn

    # Run Function to sweep bets / pay winners
    # need to reset wagers to 0 or else place bets loop wont work

    # Ask for wagers

    # Check if there is still money on the table (game ends when total_money = 0)
    for m in money:
        table_money += m



hits = [[],['hello'],[]]

for hit in hits:
    if hit:
        print('good')
    else:
        print(hit)