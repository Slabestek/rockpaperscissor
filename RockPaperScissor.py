import random
from compareHands import compareHands
# Ask user to choose Rock, Paper or Scissor
userHand = input('Choose Rock, Paper or Scissor:')

# Choose Rock, Paper or Scissor at random
options = ['Rock', 'Paper', 'Scissor']
pcHand = random.choice(options)

# Compare user input to computer choice
compareHands(userHand, pcHand)
