def MinMax(board, player, depth, maxDepth):
    if board.isGameOver() or depth == maxDepth:
        #evaluates the game score in these cases(maximum deph or end of the game)
        return board.evaluate(player), null

    bestMove = null
    if board.currentPlayer() == player:
        bestScore = -INFINITY
    else:
        bestScore = +INFINITY

    
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
MinMax(board, player, 0, maxDepth)
        
def isGameOver():            
    I = 0
    while I < len(player):
        a = (player[I][0],player[I][1])
        #searching for horizontal 4
        n = 1
        while n <= 5:
            if (a[0]+40*n, a[1])in player:
                n = n+1
            else:
                break
            if n == 5:
                return
        n= 1
        while n <= 5:
            if (a[0]+40*n, a[1]+40*n)in player:
                n = n+1
            else:
                break
            if n == 5:
                return
        n= 1
        while n <= 5:
            if (a[0]+40*n, a[1]-40*n)in player:
                n = n+1
            else:
                break
            if n == 5:
                return
        n= 1
        while n <= 5:
            if (a[0], a[1]+40*n)in player:
                n = n+1
            else:
                break
        if n == 5:
            return
        I = I+1
