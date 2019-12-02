team_name = 'Team 3333'
strategy_name = 'Betray 2'
strategy_description = 'If my history is c, and their history is c, I will betray.'

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    if my_history=='c':
        their_history=='c'
        return 'b'