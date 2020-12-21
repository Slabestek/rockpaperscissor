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
            print(tie)
        elif pcHand == 'Scissor':
            print(win)
        else:
            print(lose)

    elif userHand == 'Scissor':
        if pcHand == 'Scissor':
            print(tie)
        elif pcHand == 'Paper':
            print(win)
        else:
            print(lose)

    else:
        if pcHand == 'Paper':
            print(tie)
        elif pcHand == 'Rock':
            print(win)
        else:
            print(lose)
