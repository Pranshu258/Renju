maxDepth = 5
def MinMax(board, player, depth, maxDepth):
    if board.isGameOver() or depth == maxDepth:
        #evaluates the game score in these cases(maximum depth or end of the game)
        return board.evaluate(player), null

    bestMove = null
    if board.currentPlayer() == player:
        bestScore = -10
    else:
        bestScore = +10

    
    for move in board.getMoves():
        newBoard = board.makeMove(move)
        score = MinMax(newBoard, player, depth+1, maxDepth)
        if board.currentplayer() == player:
            if score > bestScore:
                bestScore = score
                bestMove = move
        elif score < bestScore:
            bestScore = score
            bestMove = move
    #return the best score and best move
    return bestScore, bestMove

#MinMax(board, player, 0, maxDepth) this will be the function call
        
def isGameOver():            
    I = 0
    while I < len(player):
        a = (player[I][0],player[I][1])
        #searching for horizontal 5
        n = 1
        while n <= 5:
            if (a[0]+40*n, a[1])in player:
                n = n+1
            else:
                break
        if n == 5:
            return True
        n= 1
        while n <= 5:
            if (a[0]+40*n, a[1]+40*n)in player:
                n = n+1
            else:
                break
        if n == 5:
            return True
        n= 1
        while n <= 5:
            if (a[0]+40*n, a[1]-40*n)in player:
                n = n+1
            else:
                break
        if n == 5:
            return True
        n= 1
        while n <= 5:
            if (a[0], a[1]+40*n)in player:
                n = n+1
            else:
                break
        if n == 5:
            return True
        I = I+1

    
def evaluate(player):
#higher the return score better is the move for the CPU player
#searching for fives
    I = 0
    while I < len(player):
        a = (player[I][0],player[I][1])
        n = 1
        while n <= 5:
            if (a[0]+40*n, a[1])in player:
                n = n+1
            else:
                break
        if n == 5:
            return 10
        n= 1
        while n <= 5:
            if (a[0]+40*n, a[1]+40*n)in player:
                n = n+1
            else:
                break
        if n == 5:
            return 10
        n= 1
        while n <= 5:
            if (a[0]+40*n, a[1]-40*n)in player:
                n = n+1
            else:
                break
        if n == 5:
            return 10
        n= 1
        while n <= 5:
            if (a[0], a[1]+40*n)in player:
                n = n+1
            else:
                break
        if n == 5:
            return 10
        I = I+1
#searching for fours 
    I = 0
    while I < len(player):
        a = (player[I][0],player[I][1])
        #HORIZONTAL FOURS
        n = 1
        while n <= 4:
            if (a[0]+40*n, a[1])in player:
                n = n+1
            else:
                break
        if n == 4:
            if (a[0]+40*5, a[1]) not in otherplayer or (a[0]-40, a[1]) not in otherplayer:
                return 8
        #SOUTHEAST FOURS
        n= 1
        while n <= 4:
            if (a[0]+40*n, a[1]+40*n)in player:
                n = n+1
            else:
                break
        if n == 4:
            if (a[0]+40*5, a[1]+40*5) not in otherplayer or (a[0]-40, a[1]-40) not in otherplayer:
                return 8
        #SOUTHWEST FOURS
        n= 1
        while n <= 4:
            if (a[0]+40*n, a[1]-40*n)in player:
                n = n+1
            else:
                break
        if n == 4:
            if (a[0]+40*5, a[1]-40*5) not in otherplayer or (a[0]+40, a[1]-40) not in otherplayer:
                return 8
        #VERTICAL FOURS
        n= 1
        while n <= 4:
            if (a[0], a[1]+40*n)in player:
                n = n+1
            else:
                break
        if n == 4:
            if (a[0], a[1]+40*5) not in otherplayer or (a[0], a[1]-40) not in otherplayer:
                return 8
        I = I+1

#searching for threes and broken fours
#return score 8 for broken fours (which can give winning move) and 7 for all threes 
    I = 0
    while I < len(player):
        a = (player[I][0],player[I][1])
        #HORIZONTAL THREES
        n = 1
        while n <= 3:
            if (a[0]+40*n, a[1])in player:
                n = n+1
            else:
                break
        if n == 3:
            if (a[0]+40*4, a[1]) not in otherplayer and (a[0]+40*5, a[1]) in player:
                return 8
            if (a[0]-40, a[1]) not in otherplayer and (a[0]-40*2, a[1]) in player:
                return 8
            if (a[0]+40*4, a[1]) not in otherplayer and (a[0]-40, a[1]) not in otherplayer:
                return 7
            if (a[0]+40*4, a[1]) not in otherplayer and (a[0]+40*5, a[1]) not in otherplayer:
                return 7
            if (a[0]-40, a[1]) not in otherplayer and (a[0]-40*2, a[1]) not in otherplayer:
                return 7
        #SOUTHEAST THREES
        n= 1
        while n <= 3:
            if (a[0]+40*n, a[1]+40*n)in player:
                n = n+1
            else:
                break
        if n == 3:
            if (a[0]+40*4, a[1]+40*4) not in otherplayer and (a[0]+40*5, a[1]+40*5) in player:
                return 8
            if (a[0]-40, a[1]-40) not in otherplayer and (a[0]-40*2, a[1]-40*2) in player:
                return 8
            if (a[0]+40*4, a[1]+40*4) not in otherplayer and (a[0]-40, a[1]-40) not in otherplayer:
                return 7
            if (a[0]+40*4, a[1]+40*4) not in otherplayer and (a[0]+40*5, a[1]+40*5) not in otherplayer:
                return 7
            if (a[0]-40, a[1]-40) not in otherplayer and (a[0]-40*2, a[1]-40*2) not in otherplayer:
                return 7
        #SOUTHWEST THREES
        n= 1
        while n <= 3:
            if (a[0]+40*n, a[1]-40*n)in player:
                n = n+1
            else:
                break
        if n == 3:
            if (a[0]+40*4, a[1]-40*4) not in otherplayer and (a[0]+40*5, a[1]-40*5) in player:
                return 8
            if (a[0]-40, a[1]+40) not in otherplayer and (a[0]-40*2, a[1]+40*2) in player:
                return 8
            if (a[0]+40*4, a[1]-40*4) not in otherplayer and (a[0]-40, a[1]+40) not in otherplayer:
                return 7
            if (a[0]+40*4, a[1]-40*4) not in otherplayer and (a[0]+40*5, a[1]-40*5) not in otherplayer:
                return 7
            if (a[0]-40, a[1]+40) not in otherplayer and (a[0]-40*2, a[1]+40*2) not in otherplayer:
                return 7
        #VERTICAL THREES
        n= 1
        while n <= 3:
            if (a[0], a[1]+40*n)in player:
                n = n+1
            else:
                break
        if n == 3:
            if (a[0], a[1]+40*4) not in otherplayer and (a[0], a[1]+40*5) in player:
                return 8
            if (a[0], a[1]-40) not in otherplayer and (a[0], a[1]-40*2) in player:
                return 8
            if (a[0], a[1]+40*4) not in otherplayer and (a[0], a[1]-40) not in otherplayer:
                return 7
            if (a[0], a[1]+40*4) not in otherplayer and (a[0], a[1]+40*5) not in otherplayer:
                return 7
            if (a[0], a[1]-40) not in otherplayer and (a[0], a[1]-40*2) not in otherplayer:
                return 7
        I = I+1

#search for broken threes (which are not blocked)
I = 0
    while I < len(player):
        a = (player[I][0],player[I][1])
        #HORIZONTAL TWOS AND ONE
        n = 1
        while n <= 2:
            if (a[0]+40*n, a[1])in player:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0]+40*3, a[1]) not in otherplayer and (a[0]+40*4, a[1]) in player:
                if (a[0]+40*5, a[1]) not in otherplayer or  (a[0]-40, a[1]) not in otherplayer:
                    return 7
            if (a[0]-40, a[1]) not in otherplayer and (a[0]-40*2, a[1]) in player:
                if (a[0]-40*3, a[1]) not in otherplayer or (a[0]+40*3, a[1]) not in otherplayer:
                    return 7
            
        #SOUTHEAST TWOS AND ONE
        n= 1
        while n <= 2:
            if (a[0]+40*n, a[1]+40*n)in player:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0]+40*3, a[1]+40*3) not in otherplayer and (a[0]+40*4, a[1]+40*4) in player:
                if (a[0]+40*5, a[1]+40*5) not in otherplayer or (a[0]-40, a[1]-40) not in otherplayer:
                    return 7
            if (a[0]-40, a[1]-40) not in otherplayer and (a[0]-40*2, a[1]-40*2) in player:
                if (a[0]-40*3, a[1]-40*3) not in otherplayer or (a[0]+40*3, a[1]+40*3) not in otherplayer:
                    return 7
            
        #SOUTHWEST TWOS AND ONE
        n= 1
        while n <= 2:
            if (a[0]+40*n, a[1]-40*n)in player:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0]+40*3, a[1]-40*3) not in otherplayer and (a[0]+40*4, a[1]-40*4) in player:
                if (a[0]+40*5, a[1]-40*5) not in otherplayer or (a[0]-40, a[1]+40) not in other player:
                    return 7
            if (a[0]-40, a[1]+40) not in otherplayer and (a[0]-40*2, a[1]+40*2) in player:
                if (a[0]-40*3, a[1]+40*3) not in otherplayer or (a[0]+40*3, a[1]-40*3) not in otherplayer:
                    return 7
           
        #VERTICAL THREES
        n= 1
        while n <= 2:
            if (a[0], a[1]+40*n)in player:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0], a[1]+40*3) not in otherplayer and (a[0], a[1]+40*4) in player:
                if (a[0], a[1]+40*5) not in otherplayer or (a[0], a[1]-40) not in otherplayer:
                    return 7
            if (a[0], a[1]-40) not in otherplayer and (a[0], a[1]-40*2) in player:
                if (a[0], a[1]-40*3) not in otherplayer or (a[0], a[1]+40*3) not in otherplayer:
                    return 7
            
        I = I+1
  
def getMoves():
    moves = []
    used = player + otherplayer
    for u in used:
        if (u[0]+40,u[1]) not in used:
            moves.append(u[0]+40,u[1])
        if (u[0]+40,u[1]+40) not in used:
            moves.append(u[0]+40,u[1]+40)
        if (u[0]+40,u[1]-40) not in used:
            moves.append(u[0]+40,u[1]-40)
        if (u[0]-40,u[1]) not in used:
            moves.append(u[0]-40,u[1])
        if (u[0]-40,u[1]) not in used:
            moves.append(u[0]-40,u[1])
        if (u[0]-40,u[1]-40) not in used:
            moves.append(u[0],u[1]-40)
        if (u[0],u[1]-40) not in used:
            moves.append(u[0],u[1]-40)
        if (u[0],u[1]+40) not in used:
            moves.append(u[0],u[1]+40)
        if (u[0]-40,u[1]+40) not in used:
            moves.append(u[0]-40,u[1]+40)
        return moves

def makeMove(move):
    player.append(move)
    
