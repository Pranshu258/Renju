maxDepth = 6

player = blacks
otherplayer = whites

def MinMax(board, player, depth, maxDepth):
        
    if board.isGameOver() or depth == maxDepth:
        #evaluates the game score in these cases(maximum depth or end of the game)
        return board.evaluate(player), null
    
    if depth%2 == 0:
        board.currentPlayer = player
    else:
        board.currentPlayer = otherplayer
        
    bestMove = null
    if board.currentPlayer() == player:
        bestScore = -10
    else:
        bestScore = 10

    
    for move in board.getMoves():
        newBoard = board.makeMove(move)
        score = MinMax(newBoard, player, depth+1, maxDepth)
        if board.currentplayer() == player:
            if score > bestScore:
                bestScore = score
                bestMove = move
        else:
            if score < bestScore:
                bestScore = score
                bestMove = move
    #return the best score and best move
    return bestScore, bestMove

#MinMax(board, player, 0, maxDepth) this will be the function call
        
def isGameOver():            
    I = 0
    play = board.currentPlayer
    while I < len():
        a = (play[I][0],play[I][1])
        #searching for horizontal 5
        n = 1
        while n <= 5:
            if (a[0]+40*n, a[1])in play:
                n = n+1
            else:
                break
        if n == 5:
            return True
        n= 1
        while n <= 5:
            if (a[0]+40*n, a[1]+40*n)in play:
                n = n+1
            else:
                break
        if n == 5:
            return True
        n= 1
        while n <= 5:
            if (a[0]+40*n, a[1]-40*n)in play:
                n = n+1
            else:
                break
        if n == 5:
            return True
        n= 1
        while n <= 5:
            if (a[0], a[1]+40*n)in play:
                n = n+1
            else:
                break
        if n == 5:
            return True
        I = I+1

    
def evaluate(player):
#higher the return score better is the move for the CPU player
#searching for fives
    play2 = board.currentPlayer
    if play2 == player:
        play1 = otherplayer
    else:
        play1 = player
        
    I = 0
    while I < len(play1):
        a = (play1[I][0],play1[I][1])
        n = 1
        while n <= 5:
            if (a[0]+40*n, a[1])in play1:
                n = n+1
            else:
                break
        if n == 5:
            return 10
        n= 1
        while n <= 5:
            if (a[0]+40*n, a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 5:
            return 10
        n= 1
        while n <= 5:
            if (a[0]+40*n, a[1]-40*n)in play1:
                n = n+1
            else:
                break
        if n == 5:
            return 10
        n= 1
        while n <= 5:
            if (a[0], a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 5:
            return 10
        I = I+1
#searching for fours 
    I = 0
    while I < len(play1):
        a = (play1[I][0],play1[I][1])
        #HORIZONTAL FOURS
        n = 1
        while n <= 4:
            if (a[0]+40*n, a[1])in play1:
                n = n+1
            else:
                break
        if n == 4:
            if (a[0]+40*5, a[1]) not in play2 or (a[0]-40, a[1]) not in play2:
                return 8
        #SOUTHEAST FOURS
        n= 1
        while n <= 4:
            if (a[0]+40*n, a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 4:
            if (a[0]+40*5, a[1]+40*5) not in play2 or (a[0]-40, a[1]-40) not in play2:
                return 8
        #SOUTHWEST FOURS
        n= 1
        while n <= 4:
            if (a[0]+40*n, a[1]-40*n)in play1:
                n = n+1
            else:
                break
        if n == 4:
            if (a[0]+40*5, a[1]-40*5) not in play2 or (a[0]+40, a[1]-40) not in play2:
                return 8
        #VERTICAL FOURS
        n= 1
        while n <= 4:
            if (a[0], a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 4:
            if (a[0], a[1]+40*5) not in play2 or (a[0], a[1]-40) not in play2:
                return 8
        I = I+1

#searching for threes and broken fours
#return score 8 for broken fours (which can give winning move) and 7 for all threes 
    I = 0
    while I < len(play1):
        a = (play1[I][0],play1[I][1])
        #HORIZONTAL THREES
        n = 1
        while n <= 3:
            if (a[0]+40*n, a[1])in play1:
                n = n+1
            else:
                break
        if n == 3:
            if (a[0]+40*4, a[1]) not in play2 and (a[0]+40*5, a[1]) in play1:
                return 8
            if (a[0]-40, a[1]) not in play2 and (a[0]-40*2, a[1]) in play1:
                return 8
            if (a[0]+40*4, a[1]) not in play2 and (a[0]-40, a[1]) not in play2:
                return 7
            if (a[0]+40*4, a[1]) not in play2 and (a[0]+40*5, a[1]) not in play2:
                return 7
            if (a[0]-40, a[1]) not in play2 and (a[0]-40*2, a[1]) not in play2:
                return 7
        #SOUTHEAST THREES
        n= 1
        while n <= 3:
            if (a[0]+40*n, a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 3:
            if (a[0]+40*4, a[1]+40*4) not in play2 and (a[0]+40*5, a[1]+40*5) in play1:
                return 8
            if (a[0]-40, a[1]-40) not in play2 and (a[0]-40*2, a[1]-40*2) in play1:
                return 8
            if (a[0]+40*4, a[1]+40*4) not in play2 and (a[0]-40, a[1]-40) not in play2:
                return 7
            if (a[0]+40*4, a[1]+40*4) not in play2 and (a[0]+40*5, a[1]+40*5) not in play2:
                return 7
            if (a[0]-40, a[1]-40) not in play2 and (a[0]-40*2, a[1]-40*2) not in play2:
                return 7
        #SOUTHWEST THREES
        n= 1
        while n <= 3:
            if (a[0]+40*n, a[1]-40*n)in play1:
                n = n+1
            else:
                break
        if n == 3:
            if (a[0]+40*4, a[1]-40*4) not in play2 and (a[0]+40*5, a[1]-40*5) in play1:
                return 8
            if (a[0]-40, a[1]+40) not in play2 and (a[0]-40*2, a[1]+40*2) in play1:
                return 8
            if (a[0]+40*4, a[1]-40*4) not in play2 and (a[0]-40, a[1]+40) not in play2:
                return 7
            if (a[0]+40*4, a[1]-40*4) not in play2 and (a[0]+40*5, a[1]-40*5) not in play2:
                return 7
            if (a[0]-40, a[1]+40) not in play2 and (a[0]-40*2, a[1]+40*2) not in play2:
                return 7
        #VERTICAL THREES
        n= 1
        while n <= 3:
            if (a[0], a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 3:
            if (a[0], a[1]+40*4) not in play2 and (a[0], a[1]+40*5) in play1:
                return 8
            if (a[0], a[1]-40) not in play2 and (a[0], a[1]-40*2) in play1:
                return 8
            if (a[0], a[1]+40*4) not in play2 and (a[0], a[1]-40) not in play2:
                return 7
            if (a[0], a[1]+40*4) not in play2 and (a[0], a[1]+40*5) not in play2:
                return 7
            if (a[0], a[1]-40) not in play2 and (a[0], a[1]-40*2) not in play2:
                return 7
        I = I+1

#search for broken threes (which are not blocked)
I = 0
    while I < len(play1):
        a = (play1[I][0],play1[I][1])
        #HORIZONTAL TWOS AND ONE
        n = 1
        while n <= 2:
            if (a[0]+40*n, a[1])in play1:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0]+40*3, a[1]) not in play2 and (a[0]+40*4, a[1]) in play1:
                if (a[0]+40*5, a[1]) not in play2 or  (a[0]-40, a[1]) not in play2:
                    return 7
            if (a[0]-40, a[1]) not in play2 and (a[0]-40*2, a[1]) in play1:
                if (a[0]-40*3, a[1]) not in play2 or (a[0]+40*3, a[1]) not in play2:
                    return 7
            
        #SOUTHEAST TWOS AND ONE
        n= 1
        while n <= 2:
            if (a[0]+40*n, a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0]+40*3, a[1]+40*3) not in play2 and (a[0]+40*4, a[1]+40*4) in play1:
                if (a[0]+40*5, a[1]+40*5) not in play2 or (a[0]-40, a[1]-40) not in play2:
                    return 7
            if (a[0]-40, a[1]-40) not in play2 and (a[0]-40*2, a[1]-40*2) in play1:
                if (a[0]-40*3, a[1]-40*3) not in play2 or (a[0]+40*3, a[1]+40*3) not in play2:
                    return 7
            
        #SOUTHWEST TWOS AND ONE
        n= 1
        while n <= 2:
            if (a[0]+40*n, a[1]-40*n)in play1:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0]+40*3, a[1]-40*3) not in play2 and (a[0]+40*4, a[1]-40*4) in play1:
                if (a[0]+40*5, a[1]-40*5) not in play2 or (a[0]-40, a[1]+40) not in play2:
                    return 7
            if (a[0]-40, a[1]+40) not in play2 and (a[0]-40*2, a[1]+40*2) in play1:
                if (a[0]-40*3, a[1]+40*3) not in play2 or (a[0]+40*3, a[1]-40*3) not in play2:
                    return 7
           
        #VERTICAL THREES
        n= 1
        while n <= 2:
            if (a[0], a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0], a[1]+40*3) not in play2 and (a[0], a[1]+40*4) in play1:
                if (a[0], a[1]+40*5) not in play2 or (a[0], a[1]-40) not in play2:
                    return 7
            if (a[0], a[1]-40) not in play2 and (a[0], a[1]-40*2) in play1:
                if (a[0], a[1]-40*3) not in play2 or (a[0], a[1]+40*3) not in play2:
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
    board.currentPlayer.append(move)
    
