def get_round_winner(player1, player2):
    if(ord(player1) < ord(player2)):
        if(ord(player1) - ord(player2) < -2):
            return 2
        return 1
    elif(ord(player1) > ord(player2)):
        if(ord(player1) - ord(player2) > 2):
            return 1
        return 2
    else:
        return 0

def get_match_winner():
    

print(get_winner('S', 'P'))