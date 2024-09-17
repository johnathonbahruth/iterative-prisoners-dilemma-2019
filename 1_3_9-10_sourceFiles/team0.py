
team_name = 'Betray Squad' 
strategy_name = 'BBCB'
strategy_description = 'only c after both b'
    
def move(my_history, their_history, my_score, their_score):
    
    if len(my_history)==0:
       return 'b'
    elif my_history[-1]=='c' and their_history [-1]=='b':
        return 'b'
    elif my_history[-1]=='c' and their_history [-1]=='c':
        return 'b'
    elif my_history[-1]=='b' and their_history [-1]=='b':
        return 'c'
    elif my_history[-1]=='b' and their_history [-1]=='c':
        return 'b'