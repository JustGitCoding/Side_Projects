# Dependencies
import random

# Variables
player_count = 2
ss = '\u2660'
cc = '\u2663'
hh = '\u2665'
dd = '\u2666'

# Function to shuffle the deck
def shuffle_deck():
    unshuffled_deck = [f'A {dd}', f'2 {dd}', f'3 {dd}', f'4 {dd}', f'5 {dd}', f'6 {dd}', f'7 {dd}', f'8 {dd}', f'9 {dd}', f'10{dd}', f'J {dd}', f'Q {dd}', f'K {dd}',
                        f'A {cc}', f'2 {cc}', f'3 {cc}', f'4 {cc}', f'5 {cc}', f'6 {cc}', f'7 {cc}', f'8 {cc}', f'9 {cc}', f'10{cc}', f'J {cc}', f'Q {cc}', f'K {cc}',
                        f'A {hh}', f'2 {hh}', f'3 {hh}', f'4 {hh}', f'5 {hh}', f'6 {hh}', f'7 {hh}', f'8 {hh}', f'9 {hh}', f'10{hh}', f'J {hh}', f'Q {hh}', f'K {hh}',
                        f'A {ss}', f'2 {ss}', f'3 {ss}', f'4 {ss}', f'5 {ss}', f'6 {ss}', f'7 {ss}', f'8 {ss}', f'9 {ss}', f'10{ss}', f'J {ss}', f'Q {ss}', f'K {ss}']
    shuffled_deck = []
    for i in range (0,52):
        draw_card = random.choice(unshuffled_deck)
        unshuffled_deck.pop(unshuffled_deck.index(draw_card))
        shuffled_deck.append(draw_card)
    return shuffled_deck

# Function to print game summary
def prnt_summ(deck, player_count):
    print(f'Dealer showing: {deck[player_count]}.\n')
    for i in range(0,player_count):
        print(f'Player {i+1}: {deck[i]}, {deck[i+player_count+1]}')

# Shuffle Deck
new_deck = shuffle_deck()

# Ask how many players
player_count = int(input('How many players are there?\n'))

# Start game
prnt_summ(new_deck, player_count)