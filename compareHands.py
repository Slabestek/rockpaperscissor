def compareHands(userHand, pcHand):
    '''(string, string) -> string

    Return whether the player wins, loses or ties in Rock, paper, scissor.

    >>> compareHands('Rock', 'Scissor')
    You win!
    >>> compareHands ('Paper', 'Rock')
    You lose...
    >>> compareHands ('Scissor', 'Scissor')
    It's a tie.
    '''

    win = 'You win! Computer played ' + pcHand
    tie = 'It\'s a tie. Computer played ' + pcHand
    lose = 'You lose... Computer played ' + pcHand

    if userHand == 'Rock':
        if pcHand == 'Rock':
            return tie
        elif pcHand == 'Scissor':
            return win
        else:
            return lose

    elif userHand == 'Scissor':
        if pcHand == 'Scissor':
            return tie
        elif pcHand == 'Paper':
            return win
        else:
            return lose

    else:
        if pcHand == 'Paper':
            return tie
        elif pcHand == 'Rock':
            return win
        else:
            return lose
