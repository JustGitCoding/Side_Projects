# Variables
letters = ' abcdefghijklmnopqrstuvwxyz'
values = []
val=0

# Function to get letter value
for i in range(0,len(letters)):
    values.append(val)
    val += 1

# Function
def letter_value(letter):
    position = letters.index(letter)
    return values[position]

play = 'yes'
while play == 'yes' or play == 'y':
    # INPUT
    word = input('Please input a word to calculate:')

    # Reset Total
    total = 0

    # Loop to calculate
    for i in range(0,len(word)):
        total = total + letter_value(word[i])

    # Print Total
    print(total)

    # Play again?
    play = input('Play again?').lower()
