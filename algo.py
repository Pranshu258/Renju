def minmax(player, otherplayer, depth, maxdepth, A, B):
    a = []
    b = []
    print 'PLAYER'
    print player
    print 'OTHERPLAYER'
    print otherplayer
    if isgameover(player) or depth == maxdepth:
        e = evaluate(player, otherplayer)
        print 'e '+str(e)
        return e
    bestmove = None
    bestscore = -1000
    move = getmoves(player, otherplayer)
    for m in move:
        print 'm'
        print m
        a = player+[(m)]
        b = otherplayer+[]
        score = minmax(b, a, depth+1, maxdepth, -B, -max(A, bestscore))            
        print 'depth '+str(depth)
        print 'score '+ str(score)
        score = -score
        if score > bestscore:
            print 'beta'
            bestscore = score
            bestmove = move
            if bestscore >= B:
                print 'alpha'
                return bestscore
    print 'bestmove '+str(bestmove)
    if depth == 0:
        player.append((bestmove[0]))
    return bestscore
    
def isgameover(play):            
    I = 0
    while I < len(play):
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
        
def getmoves(play1, play2):
    moves = []
    used = play1 + play2
    p = []
    s1 = 0
    for u in used:
        if (u[0],u[1]-40) not in used:
            if (u[0],u[1]-40) not in moves:
                moves.append((u[0],u[1]-40))
        if (u[0]+40,u[1]-40) not in used:
            if (u[0]+40,u[1]-40) not in moves:
                moves.append((u[0]+40,u[1]-40))
        if (u[0]+40,u[1]) not in used:
            if (u[0]+40,u[1]) not in moves:
                moves.append((u[0]+40,u[1]))
        if (u[0]+40,u[1]+40) not in used:
            if (u[0]+40,u[1]+40) not in moves:
                moves.append((u[0]+40,u[1]+40))
        if (u[0],u[1]+40) not in used:
            if (u[0],u[1]+40) not in moves:
                moves.append((u[0],u[1]+40))
        if (u[0]-40,u[1]+40) not in used:
            if (u[0]-40,u[1]+40) not in moves:
                moves.append((u[0]-40,u[1]+40))
        if (u[0]-40,u[1]) not in used:
            if (u[0]-40,u[1]) not in moves:
                moves.append((u[0]-40,u[1]))
        if (u[0]-40,u[1]-40) not in used:
            if (u[0]-40,u[1]-40) not in moves:
                moves.append((u[0]-40,u[1]-40))
    print 'moves ' + str(moves)
    s1 = 0
    des = []
    for m in moves:
        p = []
        p = play1+[m]
        s2 = evaluate(p, play2)
        if s2 > s1:
            s1 = s2
            des = []
            des.append((m))
        if s2 == s1:
            des.append((m))
        if s2 < s1:
            continue
    print 'des'+ str(des)
    return des


def evaluate(play1, play2):
    #higher the return score better is the move for the CPU player
    #searching for fives
       
    I = 0
    while I < len(play1):
        a = (play1[I][0],play1[I][1])
        n = 1
        while n < 5:
            if (a[0]+40*n, a[1])in play1:
                n = n+1
            else:
                break
        if n == 5:
            return 10
        n= 1
        while n < 5:
            if (a[0]+40*n, a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 5:
            return 10
        n= 1
        while n < 5:
            if (a[0]+40*n, a[1]-40*n)in play1:
                n = n+1
            else:
                break
        if n == 5:
            return 10
        n= 1
        while n < 5:
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
        while n < 4:
            if (a[0]+40*n, a[1])in play1:
                n = n+1
            else:
                break
        if n == 4:
            if (a[0]+40*5, a[1]) not in play2 or (a[0]-40, a[1]) not in play2:
                return 8
        #SOUTHEAST FOURS
        n= 1
        while n < 4:
            if (a[0]+40*n, a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 4:
            if (a[0]+40*5, a[1]+40*5) not in play2 or (a[0]-40, a[1]-40) not in play2:
                return 8
        #SOUTHWEST FOURS
        n= 1
        while n < 4:
            if (a[0]+40*n, a[1]-40*n)in play1:
                n = n+1
            else:
                break
        if n == 4:
            if (a[0]+40*5, a[1]-40*5) not in play2 or (a[0]+40, a[1]-40) not in play2:
                return 8
        #VERTICAL FOURS
        n= 1
        while n < 4:
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
        while n < 3:
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
        while n < 3:
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
        while n < 3:
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
        while n < 3:
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
        while n < 2:
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
        while n < 2:
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
        while n < 2:
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
        while n < 2:
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
        
    #search for unblocked twos
    I = 0
    while I < len(play1):
        a = (play1[I][0],play1[I][1])
        #HORIZONTAL TWOS
        n = 1
        while n < 2:
            if (a[0]+40*n, a[1])in play1:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0]+40*2, a[1]) not in play2 and (a[0]+40*3, a[1]) not in play2 and (a[0]+40*4, a[1]) not in play2:
                return 4
            if (a[0]-40, a[1]) not in play2 and (a[0]+40*2, a[1]) not in play2 and (a[0]+40*3, a[1]) not in play2:
                return 4
            if (a[0]-40*2, a[1]) not in play2 and (a[0]-40, a[1]) not in play2 and (a[0]+40*2, a[1]) not in play2:
                return 4
            if (a[0]-40*2, a[1]) not in play2 and (a[0]-40, a[1]) not in play2 and (a[0]-40*3, a[1]) not in play2:
                return 4
        #SOUTHEAST TWOS
        n= 1
        while n < 2:
            if (a[0]+40*n, a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0]+40*2, a[1]+40*2) not in play2 and (a[0]+40*3, a[1]+40*3) not in play2 and (a[0]+40*4, a[1]+40*4) not in play2:
                return 4
            if (a[0]-40, a[1]-40) not in play2 and (a[0]+40*2, a[1]+40*2) not in play2 and (a[0]+40*3, a[1]+40*3) not in play2:
                return 4
            if (a[0]-40*2, a[1]-40*2) not in play2 and (a[0]-40, a[1]-40) not in play2 and (a[0]+40*2, a[1]+40*2) not in play2:
                return 4
            if (a[0]-40*2, a[1]-40*2) not in play2 and (a[0]-40, a[1]-40) not in play2 and (a[0]-40*3, a[1]-40*3) not in play2:
                return 4
        #SOUTHWEST TWOS
        n= 1
        while n < 2:
            if (a[0]+40*n, a[1]-40*n)in play1:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0]+40*2, a[1]-40*2) not in play2 and (a[0]+40*3, a[1]-40*3) not in play2 and (a[0]+40*4, a[1]-40*4) not in play2:
                return 4
            if (a[0]-40, a[1]+40) not in play2 and (a[0]+40*2, a[1]-40*2) not in play2 and (a[0]+40*3, a[1]-40*3) not in play2:
                return 4
            if (a[0]-40*2, a[1]+40*2) not in play2 and (a[0]-40, a[1]+40) not in play2 and (a[0]+40*2, a[1]-40*2) not in play2:
                return 4
            if (a[0]-40*2, a[1]+40*2) not in play2 and (a[0]-40, a[1]+40) not in play2 and (a[0]-40*3, a[1]+40*3) not in play2:
                return 4
        #VERTICAL TWOS
        n= 1
        while n < 2:
            if (a[0], a[1]+40*n)in play1:
                n = n+1
            else:
                break
        if n == 2:
            if (a[0], a[1]-40) not in play2 and (a[0], a[1]-40*2) not in play2 and (a[0], a[1]-40*3) not in play2:
                return 4
            if (a[0], a[1]+40*2) not in play2 and (a[0], a[1]+40*3) not in play2 and (a[0], a[1]+40*4) not in play2:
                return 4
            if (a[0], a[1]+40*2) not in play2 and (a[0], a[1]-40) not in play2 and (a[0], a[1]+40*3) not in play2:
                return 4
            if (a[0], a[1]-40*2) not in play2 and (a[0], a[1]-40) not in play2 and (a[0], a[1]+40*2) not in play2:
                return 4
        I = I+1

    #SEARCHING FOR UNBLOCKED ONES:
    I = 0
    while I < len(play1):
        a = (play1[I][0],play1[I][1])
        
        if (a[0], a[1]+40) not in play2 and (a[0], a[1]+40*2) not in play2 and (a[0], a[1]+40*3) not in play2 and (a[0], a[1]+40*4) not in play2:
            return 2
        if (a[0]+40, a[1]+40) not in play2 and (a[0]+40*2, a[1]+40*2) not in play2 and (a[0]+40*3, a[1]+40*3) not in play2 and (a[0]+40*4, a[1]+40*4) not in play2:
            return 2
        if (a[0]+40, a[1]-40) not in play2 and (a[0]+40*2, a[1]-40*2) not in play2 and (a[0]+40*3, a[1]-40*3) not in play2 and (a[0]+40*4, a[1]-40*4) not in play2:
            return 2
        if (a[0]+40, a[1]) not in play2 and (a[0]+40*2, a[1]) not in play2 and (a[0]+40*3, a[1]) not in play2 and (a[0]+40*4, a[1]) not in play2:
            return 2
        
        if (a[0], a[1]+40) not in play2 and (a[0], a[1]+40*2) not in play2 and (a[0], a[1]+40*3) not in play2 and (a[0], a[1]-40) not in play2:
            return 2
        if (a[0]+40, a[1]+40) not in play2 and (a[0]+40*2, a[1]+40*2) not in play2 and (a[0]+40*3, a[1]+40*3) not in play2 and (a[0]-40, a[1]-40) not in play2:
            return 2
        if (a[0]+40, a[1]-40) not in play2 and (a[0]+40*2, a[1]-40*2) not in play2 and (a[0]+40*3, a[1]-40*3) not in play2 and (a[0]-40, a[1]+40) not in play2:
            return 2
        if (a[0]+40, a[1]) not in play2 and (a[0]+40*2, a[1]) not in play2 and (a[0]+40*3, a[1]) not in play2 and (a[0]-40, a[1]) not in play2:
            return 2

        if (a[0], a[1]+40) not in play2 and (a[0], a[1]+40*2) not in play2 and (a[0], a[1]-40) not in play2 and (a[0], a[1]-40*2) not in play2:
            return 2
        if (a[0]+40, a[1]+40) not in play2 and (a[0]+40*2, a[1]+40*2) not in play2 and (a[0]-40, a[1]-40) not in play2 and (a[0]-40*2, a[1]-40*2) not in play2:
            return 2
        if (a[0]+40, a[1]-40) not in play2 and (a[0]+40*2, a[1]-40*2) not in play2 and (a[0]-40, a[1]+40) not in play2 and (a[0]-40*2, a[1]+40*2) not in play2:
            return 2
        if (a[0]+40, a[1]) not in play2 and (a[0]+40*2, a[1]) not in play2 and (a[0]-40, a[1]) not in play2 and (a[0]-40*2, a[1]) not in play2:
            return 2

        if (a[0], a[1]+40) not in play2 and (a[0], a[1]-40*3) not in play2 and (a[0], a[1]-40) not in play2 and (a[0], a[1]-40*2) not in play2:
            return 2
        if (a[0]+40, a[1]+40) not in play2 and (a[0]-40*3, a[1]-40*3) not in play2 and (a[0]-40, a[1]-40) not in play2 and (a[0]-40*2, a[1]-40*2) not in play2:
            return 2
        if (a[0]+40, a[1]-40) not in play2 and (a[0]-40*3, a[1]+40*3) not in play2 and (a[0]-40, a[1]+40) not in play2 and (a[0]-40*2, a[1]+40*2) not in play2:
            return 2
        if (a[0]+40, a[1]) not in play2 and (a[0]-40*3, a[1]) not in play2 and (a[0]-40, a[1]) not in play2 and (a[0]-40*2, a[1]) not in play2:
            return 2

        if (a[0], a[1]-40*4) not in play2 and (a[0], a[1]-40*3) not in play2 and (a[0], a[1]-40) not in play2 and (a[0], a[1]-40*2) not in play2:
            return 2
        if (a[0]-40*4, a[1]-40*4) not in play2 and (a[0]-40*3, a[1]-40*3) not in play2 and (a[0]-40, a[1]-40) not in play2 and (a[0]-40*2, a[1]-40*2) not in play2:
            return 2
        if (a[0]-40*4, a[1]+40*4) not in play2 and (a[0]-40*3, a[1]+40*3) not in play2 and (a[0]-40, a[1]+40) not in play2 and (a[0]-40*2, a[1]+40*2) not in play2:
            return 2
        if (a[0]-40*4, a[1]) not in play2 and (a[0]-40*3, a[1]) not in play2 and (a[0]-40, a[1]) not in play2 and (a[0]-40*2, a[1]) not in play2:
            return 2
    return 0

    
