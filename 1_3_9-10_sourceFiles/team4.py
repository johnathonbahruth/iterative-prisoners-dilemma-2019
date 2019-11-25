def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b'
    else:
        return 'c'