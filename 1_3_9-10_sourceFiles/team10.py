team_name = 'Nats Team'
strategy_name = 'betray if lossing'
strategy_description = 'If their score is higher then mine then I betray otherwise I colude.'
    
def move(my_history, their_history, my_score, their_score):
    if their_score>my_score:
        return 'b'
    else:
        return "c"  