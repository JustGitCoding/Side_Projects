# Dependencies
import random

# Generate New Deck of Cards
cards = ['A ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','J ','K ']
suits = ['\u2660','\u2663','\u2665','\u2666']
deck = [card+suit for suit in suits for card in cards]


# Function to collect bets
def collect_wagers(players, money, wagers):
    for player in range(players):
        while wagers[player] < 0:
            wagers[player] = float(input(f'Player {player+1} has ${money[player]} - How much would you like to bet? (minimum = $5)\n'))
            while wagers[player] > 0 and wagers[player] < 5:
                wagers[player] = float(input(f"The minimum bet is $5. You can also bet $0 if you do not wish to play this hand.\n"))
            while wagers[player] > money[player]:
                wagers[player] = -1
                wagers[player] = float(input(f'You only have ${money[player]}. How much would you like to bet?\n'))
    return wagers

# Function to deal initial set of cards
def deal(deck, players):
    hands = [[] for player in range(players+1)] # Includes DEALER's hand as hands[-1]
    for player in range(players+1):
        hands[player] = [deck[player],deck[player+players]]
    return hands

# Function to print cards on the table
def summarize(deck, players, money, wagers, hands, final=False):
    # DEALER's CARDS
    print(f'-------------------------------------------')
    if final:
        print(f'   Dealer showing:       {hands[-1]}')
    else:
        print(f'   Dealer showing:       {hands[-1][0]}')
    print(f'\n-------------------------------------------')
    # PLAYER CARDS
    for player in range(players):
        print(f'Player {player+1} - ${money[player]:.0f} on the Table\n')
        print(f'      Current Bet:  ${wagers[player]:.0f}')
        print(f'     Current hand:       {hands[player]} --- Total: {calc_hand(hands[player])}')
        print(f'\n-------------------------------------------')

# Function to give each player a turn
def player_turns(deck, hands, players):
    hit = [[] for player in range(players)]
    player_hit_counter = 0
    for player in range(players):
        while hit[player] not in ['stay', 's']:
            hand_total = calc_hand(hands[player])
            print(f"Player {player+1} -")
            print(f"     Current hand:       {hands[player]} --- Total: {hand_total} ----- (Dealer showing: {hands[-1][0]})")
            hit[player] = input(f"Would you like to hit ('h') or stay ('s')?\n").lower()
            if hit[player] in ['hit','h']:
                player_hit_counter += 1
                hands[player].append(deck[(players*2)+player_hit_counter])
        print('\n-------------------------------------------')
    return hands

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
while players == 0:
    players = int(input('\nHow many players are with you?\nNote: Table seats up to 7\n'))
    # Reset money, wagers and hands lists based on player count
    money = [float(input(f'How much does Player {player+1} buy in for?\n')) for player in range(players)]
    wagers = [-1 for player in range(players)]
    

# Keep playing as long as there is money on the table
table_money = 0
for m in money:
    table_money += m
while table_money > 0:
    # Shuffle the deck
    random.shuffle(deck)

    # Place bets
    print('\n~~~ Place your bets! ~~~')
    wagers = collect_wagers(players, money, wagers)

    # Deal cards + print summary
    hands = deal(deck, players)
    summarize(deck, players, money, wagers, hands, final=False)

    ################ need to modify to add insurance option if dealer showing an Ace

    # Loop to give each player a turn:
    hands = player_turns(deck, hands, players)

    # Run Function for Dealer's turn

    # Run Function to sweep bets / pay winners
    # need to reset wagers to 0 or else place bets loop wont work

    # Ask for wagers

    # Check if there is still money on the table (game ends when total_money = 0)
    for m in money:
        table_money += m

