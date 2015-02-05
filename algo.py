def attack(player, otherplayer, depth, maxdepth, A, B):
    a = []
    b = []
    if isgameover(player) or depth == maxdepth:
        e = evaluate(player, otherplayer)
        return e
    bestmove = None
    bestscore = -1000
    move = getmoves(player, otherplayer)
    for m in move:
        a = player+[(m)]
        b = otherplayer+[]
        score = attack(b, a, depth+1, maxdepth, -B, -max(A, bestscore))            
        score = -score
        if score > bestscore:
            bestscore = score
            bestmove = m
            if bestscore >= B:
                return bestscore
    if depth == 0:
        player.append((bestmove))
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
    s1 = 0
    des = []
    for m in moves:
        if m[0] > 0 and m[0] < 600 and m[1] > 0 and m[1] < 600:
            p = []
            p = play1+[m]
            s2 = evaluate(p, play2)
            if s2 > s1:
                s1 = s2
                des = []
                if m not in des:
                    des.append((m))
            if s2 == s1:
                if m not in des:
                    des.append((m))
    return des


def evaluate(play1, play):
    p = []
    p = play1 + []
    play2 = play + []
    p.remove(p[len(p)-1])
    m = play1[len(play1)-1]
    #SEARCHING FOR FIVES
    #HORIZONTAL 
    if (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) in p and (m[0]+160,m[1]) in p:
        return 10
    if (m[0]-40,m[1]) in p and (m[0]-80,m[1]) in p and (m[0]-120,m[1]) in p and (m[0]-160,m[1]) in p:
        return 10
    #VERTICAL 
    if (m[0],m[1]+40) in p and (m[0],m[1]+80) in p and (m[0],m[1]+120) in p and (m[0],m[1]+160) in p:
        return 10
    if (m[0],m[1]-40) in p and (m[0],m[1]-80) in p and (m[0],m[1]-120) in p and (m[0],m[1]-160) in p:
        return 10
    #SOUTHEAST 
    if (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) in p and (m[0]+160,m[1]+160) in p:
        return 10
    if (m[0]-40,m[1]-40) in p and (m[0]-80,m[1]-80) in p and (m[0]-120,m[1]-120) in p and (m[0]-160,m[1]-160) in p:
        return 10
    #SOUTHWEST 
    if (m[0]-40,m[1]+40) in p and (m[0]-80,m[1]+80) in p and (m[0]-120,m[1]+120) in p and (m[0]-160,m[1]+160) in p:
        return 10
    if (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) in p and (m[0]+160,m[1]-160) in p:
        return 10
    #HORIZONTAL
    if (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) in p:
        return 10
    if (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p:
        return 10
    if (m[0]-120,m[1]) in p and (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p:
        return 10
    #SOUTHEAST
    if (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) in p:
        return 10
    if (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p:
        return 10
    if (m[0]-120,m[1]-120) in p and (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p:
        return 10
    #SOUTHWEST
    if (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) in p:
        return 10
    if (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p:
        return 10
    if (m[0]-120,m[1]+120) in p and (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p:
        return 10
    #VERTICAL
    if (m[0],m[1]-40) in p and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p and (m[0],m[1]+120) in p:
        return 10
    if (m[0],m[1]-80) in p and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p:
        return 10
    if (m[0],m[1]-120) in p and (m[0],m[1]-80) in p and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p:
        return 10

    #SEARCHING FOR MOVES THAT BLOCK OPPONENT'S FOURS WHICH HAVE UNBLOCKED ADJACENT NODES.IT WILL RETURN 9.
    #HORIZONTAL FOURS
    if (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2 and (m[0]+120,m[1]) in play2 and (m[0]+160,m[1]) in play2:
        return 9
    if (m[0]-40,m[1]) in play2 and (m[0]-80,m[1]) in play2 and (m[0]-120,m[1]) in play2 and (m[0]-160,m[1]) in play2:
        return 9
    #VERTICAL FOURS
    if (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2 and (m[0],m[1]+120) in play2 and (m[0],m[1]+160) in play2:
        return 9
    if (m[0],m[1]-40) in play2 and (m[0],m[1]-80) in play2 and (m[0],m[1]-120) in play2 and (m[0],m[1]-160) in play2:
        return 9
    #SOUTHEAST FOURS
    if (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2 and (m[0]+120,m[1]+120) in play2 and (m[0]+160,m[1]+160) in play2:
        return 9
    if (m[0]-40,m[1]-40) in play2 and (m[0]-80,m[1]-80) in play2 and (m[0]-120,m[1]-120) in play2 and (m[0]-160,m[1]-160) in play2:
        return 9
    #SOUTHWEST FOURS
    if (m[0]-40,m[1]+40) in play2 and (m[0]-80,m[1]+80) in play2 and (m[0]-120,m[1]+120) in play2 and (m[0]-160,m[1]+160) in play2:
        return 9
    if (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2 and (m[0]+120,m[1]-120) in play2 and (m[0]+160,m[1]-160) in play2:
        return 9
    #HORIZONTAL BROKEN FOURS
    if (m[0]-40,m[1]) in play2 and (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2 and (m[0]+120,m[1]) in play2:
        return 9
    if (m[0]-80,m[1]) in play2 and (m[0]-40,m[1]) in play2 and (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2:
        return 9
    if (m[0]-120,m[1]) in play2 and (m[0]-80,m[1]) in play2 and (m[0]-40,m[1]) in play2 and (m[0]+40,m[1]) in play2:
        return 9
    #SOUTHEAST BROKEN FOURS
    if (m[0]-40,m[1]-40) in play2 and (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2 and (m[0]+120,m[1]+120) in play2:
        return 9
    if (m[0]-80,m[1]-80) in play2 and (m[0]-40,m[1]-40) in play2 and (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2:
        return 9
    if (m[0]-120,m[1]-120) in play2 and (m[0]-80,m[1]-80) in play2 and (m[0]-40,m[1]-40) in play2 and (m[0]+40,m[1]+40) in play2:
        return 9
    #SOUTHWEST BROKEN FOURS
    if (m[0]-40,m[1]+40) in play2 and (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2 and (m[0]+120,m[1]-120) in play2:
        return 9
    if (m[0]-80,m[1]+80) in play2 and (m[0]-40,m[1]+40) in play2 and (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2:
        return 9
    if (m[0]-120,m[1]+120) in play2 and (m[0]-80,m[1]+80) in play2 and (m[0]-40,m[1]+40) in play2 and (m[0]+40,m[1]-40) in play2:
        return 9
    #VERTICAL BROKEN FOURS
    if (m[0],m[1]-40) in play2 and (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2 and (m[0],m[1]+120) in play2:
        return 9
    if (m[0],m[1]-80) in play2 and (m[0],m[1]-40) in play2 and (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2:
        return 9
    if (m[0],m[1]-120) in play2 and (m[0],m[1]-80) in play2 and (m[0],m[1]-40) in play2 and (m[0],m[1]+40) in play2:
        return 9
          
    #SEARCHING FOR FOURS (BOTH SIDES UNBLOCKED) 
    #HORIZONTAL FOURS
    if (m[0]-40,m[1]) not in play2 and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) in p and (m[0]+160,m[1]) not in play2:
        return 8
    if (m[0]-80,m[1]) not in play2 and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) not in play2:
        return 8
    if (m[0]-120,m[1]) not in play2 and (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) not in play2:
        return 8
    if (m[0]-160,m[1]) not in play2 and (m[0]-120,m[1]) in p and (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) not in play2:
        return 8
    #SOUTHEAST FOURS
    if (m[0]-40,m[1]-40) not in play2 and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) in p and (m[0]+160,m[1]+160) not in play2:
        return 8
    if (m[0]-80,m[1]-80) not in play2 and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) not in play2:
        return 8
    if (m[0]-120,m[1]-120) not in play2 and (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) not in play2:
        return 8
    if (m[0]-160,m[1]-160) not in play2 and (m[0]-120,m[1]-120) in p and (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) not in play2:
        return 8
    #SOUTHWEST FOURS
    if (m[0]-40,m[1]+40) not in play2 and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) in p and (m[0]+160,m[1]-160) not in play2:
        return 8
    if (m[0]-80,m[1]+80) not in play2 and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) not in play2:
        return 8
    if (m[0]-120,m[1]+120) not in play2 and (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) not in play2:
        return 8
    if (m[0]-160,m[1]+160) not in play2 and (m[0]-120,m[1]+120) in p and (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) not in play2:
        return 8
    #VERTICAL FOURS
    if (m[0],m[1]-40) not in play2 and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p and (m[0],m[1]+120) in p and (m[0],m[1]+160) not in play2:
        return 8
    if (m[0],m[1]-80) not in play2 and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p and (m[0],m[1]+120) not in play2:
        return 8
    if (m[0],m[1]-120) not in play2 and (m[0],m[1]-80) in p and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p and (m[0],m[1]+80) not in play2:
        return 8
    if (m[0],m[1]-160) not in play2 and (m[0],m[1]-120) in p and (m[0],m[1]-80) in p and (m[0],m[1]-40) in p and (m[0],m[1]+40) not in play2:
        return 8
    
    pin = 0
    #SEARCHING FOR FOURS (ONE SIDE UNBLOCKED) 
    #HORIZONTAL FOURS
    if ((m[0]-40,m[1]) not in play2 or (m[0]+160,m[1]) not in play2) and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) in p:
        pin = 7
    elif ((m[0]-80,m[1]) not in play2 or (m[0]+120,m[1]) not in play2) and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p :
        pin = 7
    elif ((m[0]-120,m[1]) not in play2 or (m[0]+80,m[1]) not in play2) and (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p:
        pin = 7
    elif ((m[0]-160,m[1]) not in play2 or (m[0]+40,m[1]) not in play2) and (m[0]-120,m[1]) in p and (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p:
        pin = 7
    #SOUTHEAST FOURS
    elif ((m[0]-40,m[1]-40) not in play2 or (m[0]+160,m[1]+160) not in play2) and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) in p:
        pin = 7
    elif ((m[0]-80,m[1]-80) not in play2 or (m[0]+120,m[1]+120) not in play2) and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p :
        pin = 7
    elif ((m[0]-120,m[1]-120) not in play2 or (m[0]+80,m[1]+80) not in play2) and (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p:
        pin = 7
    elif ((m[0]-160,m[1]-160) not in play2 or (m[0]+40,m[1]+40) not in play2) and (m[0]-120,m[1]-120) in p and (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p:
        pin = 7
    #SOUTHWEST FOURS
    elif ((m[0]-40,m[1]+40) not in play2 or (m[0]+160,m[1]-160) not in play2) and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) in p:
        pin = 7
    elif ((m[0]-80,m[1]+80) not in play2 or (m[0]+120,m[1]-120) not in play2) and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p :
        pin = 7
    elif ((m[0]-120,m[1]+120) not in play2 or (m[0]+80,m[1]-80) not in play2) and (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p:
        pin = 7
    elif ((m[0]-160,m[1]+160) not in play2 or (m[0]+40,m[1]-40) not in play2) and (m[0]-120,m[1]+120) in p and (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p:
        pin = 7
    #VERTICAL FOURS
    elif ((m[0],m[1]-40) not in play2 or (m[0],m[1]+160) not in play2) and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p and (m[0],m[1]+120) in p:
        pin = 7
    elif ((m[0],m[1]-80) not in play2 or (m[0],m[1]+120) not in play2) and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p :
        pin = 7
    elif ((m[0],m[1]-120) not in play2 or (m[0],m[1]+80) not in play2) and (m[0],m[1]-80) in p and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p:
        pin = 7
    elif ((m[0],m[1]-160) not in play2 or (m[0],m[1]+40) not in play2) and (m[0],m[1]-120) in p and (m[0],m[1]-80) in p and (m[0],m[1]-40) in p:
        pin = 7
    #HORIZONTAL THREES AND ONE
    elif (m[0]+40,m[1]) not in play2 and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) in p and (m[0]+160,m[1]) in p:
        pin = 7
    elif (m[0]-40,m[1]) not in play2 and (m[0]-80,m[1]) in p and (m[0]-120,m[1]) in p and (m[0]-160,m[1]) in p:
        pin = 7
    #SOUTHEAST THREES AND ONE
    elif (m[0]+40,m[1]+40) not in play2 and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) in p and (m[0]+160,m[1]+160) in p:
        pin = 7
    elif (m[0]-40,m[1]-40) not in play2 and (m[0]-80,m[1]-80) in p and (m[0]-120,m[1]-120) in p and (m[0]-160,m[1]-160) in p:
        pin = 7
    #SOUTHWEST THREES AND ONE
    elif (m[0]+40,m[1]-40) not in play2 and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) in p and (m[0]+160,m[1]-160) in p:
        pin = 7
    elif (m[0]-40,m[1]+40) not in play2 and (m[0]-80,m[1]+80) in p and (m[0]-120,m[1]+120) in p and (m[0]-160,m[1]+160) in p:
        pin = 7
    #VERTICAL THREES AND ONE 
    elif (m[0],m[1]+40) not in play2 and (m[0],m[1]+80) in p and (m[0],m[1]+120) in p and (m[0],m[1]+160) in p:
        pin = 7
    elif (m[0],m[1]-40) not in play2 and (m[0],m[1]-80) in p and (m[0],m[1]-120) in p and (m[0],m[1]-160) in p:
        pin = 7
    temp = 1   
    #SEARCH FOR THREES (THREE UNBLOCKED ADJACENT NODES)&(TWO UBLOCKED ADJACENT NODES)
    #HORIZONTAL THREES
    if (m[0]-40,m[1]) not in play2 and (m[0]+40, m[1]) in p and (m[0]+80, m[1]) in p and (m[0]+120,m[1]) not in play2:
        if (m[0]-80,m[1]) not in play2 and (m[0]+160,m[1]) not in play2:
            temp = 5
        elif (m[0]-80,m[1]) not in play2 or (m[0]+160,m[1]) not in play2:
            temp = 0
        else:
            temp = 2
    #SOUTHEAST THREES
    if (m[0]-40,m[1]-40) not in play2 and (m[0]+40, m[1]+40) in p and (m[0]+80, m[1]+80) in p and (m[0]+120,m[1]+120) not in play2:
        if (m[0]-80,m[1]-80) not in play2 and (m[0]+160,m[1]+160) not in play2:
            temp = 5
        elif (m[0]-80,m[1]-80) not in play2 or (m[0]+160,m[1]+160) not in play2:
            temp = 0
        else:
            temp = 2
    #SOUTHWEST THREES
    if (m[0]-40,m[1]+40) not in play2 and (m[0]+40, m[1]-40) in p and (m[0]+80, m[1]-80) in p and (m[0]+120,m[1]-120) not in play2:
        if (m[0]-80,m[1]+80) not in play2 and (m[0]+160,m[1]-160) not in play2:
            temp = 5
        elif (m[0]-80,m[1]+80) not in play2 or (m[0]+160,m[1]-160) not in play2:
            temp = 0
        else:
            temp = 2
    #VERTICAL THREES
    if (m[0],m[1]-40) not in play2 and (m[0], m[1]+40) in p and (m[0], m[1]+80) in p and (m[0],m[1]+120) not in play2:
        if (m[0],m[1]-80) not in play2 and (m[0],m[1]+160) not in play2:
            temp = 5
        elif (m[0],m[1]-80) not in play2 or (m[0],m[1]+160) not in play2:
            temp = 0
        else:
            temp = 2
    if pin == 7:
        if temp == 5:
            return 7.5
        else:
            return 7


    #SEARCHING FOR MOVES THAT BLOCK OPPONENT'S THREES WITH THREE ADJACENT EMPTY NODES. IT WILL RETURN 6
    #HORIZONTAL THREES
    if (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2 and (m[0]+120,m[1]) in play2 and (m[0]+160,m[1]) not in p and (m[0]+200,m[1]) not in p:
        return 6
    if (m[0]-40,m[1]) in play2 and (m[0]-80,m[1]) in play2 and (m[0]-120,m[1]) in play2 and (m[0]-160,m[1]) not in p and (m[0]-200,m[1]) not in p:
        return 6
    if (m[0]-40,m[1]) not in p and (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2 and (m[0]+120,m[1]) in play2 and (m[0]+160,m[1]) not in p:
        return 6
    if (m[0]+40,m[1]) not in p and (m[0]-40,m[1]) in play2 and (m[0]-80,m[1]) in play2 and (m[0]-120,m[1]) in play2 and (m[0]-160,m[1]) not in p:
        return 6    
    #SOUTHEAST THREES
    if (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2 and (m[0]+120,m[1]+120) in play2 and (m[0]+160,m[1]+160) not in p and (m[0]+200,m[1]+200) not in p:
        return 6
    if (m[0]-40,m[1]-40) in play2 and (m[0]-80,m[1]-80) in play2 and (m[0]-120,m[1]-120) in play2 and (m[0]-160,m[1]-160) not in p and (m[0]-200,m[1]-200) not in p:
        return 6
    if (m[0]-40,m[1]-40) not in p and (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2 and (m[0]+120,m[1]+120) in play2 and (m[0]+160,m[1]+160) not in p:
        return 6
    if (m[0]+40,m[1]+40) not in p and (m[0]-40,m[1]-40) in play2 and (m[0]-80,m[1]-80) in play2 and (m[0]-120,m[1]-120) in play2 and (m[0]-160,m[1]-160) not in p:
        return 6    
    #SOUTHWEST THREES
    if (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2 and (m[0]+120,m[1]-120) in play2 and (m[0]+160,m[1]-160) not in p and (m[0]+200,m[1]-200) not in p:
        return 6
    if (m[0]-40,m[1]+40) in play2 and (m[0]-80,m[1]+80) in play2  and (m[0]-120,m[1]+120) in play2 and (m[0]-160,m[1]+160) not in p and (m[0]-200,m[1]+200) not in p:
        return 6
    if (m[0]-40,m[1]+40) not in p and (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2 and (m[0]+120,m[1]-120) in play2 and (m[0]+160,m[1]-160) not in p:
        return 6
    if (m[0]+40,m[1]-40) not in p and (m[0]-40,m[1]+40) in play2 and (m[0]-80,m[1]+80) in play2 and (m[0]-120,m[1]+120) in play2 and (m[0]-160,m[1]+160) not in p:
        return 6    
    #VERTICAL THREES
    if (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2 and (m[0],m[1]+120) in play2 and (m[0],m[1]+160) not in p and (m[0],m[1]+200) not in p:
        return 6
    if (m[0],m[1]-40) in play2 and (m[0],m[1]-80) in play2 and (m[0],m[1]-120) in play2 and (m[0],m[1]-160) not in p and (m[0],m[1]-200) not in p:
        return 6
    if (m[0],m[1]-40) not in p and (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2 and (m[0],m[1]+120) in play2 and (m[0],m[1]+160) not in p:
        return 6
    if (m[0],m[1]+40) not in p and (m[0],m[1]-40) in play2 and (m[0],m[1]-80) in play2 and (m[0],m[1]-120) in play2 and (m[0],m[1]-160) not in p:
        return 6    

    #BLOCKING OPPONENT'S BROKEN THREES
    #HORIZONTAL TWOS AND ONE
    if (m[0]-80,m[1]) not in p and (m[0]-40,m[1]) in play2 and (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2 and (m[0]+120,m[1]) not in p:
        return 6
    if (m[0]-120,m[1]) not in p and (m[0]-80,m[1]) in play2 and (m[0]-40,m[1]) in play2 and (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) not in p:
        return 6
    #SOUTHEAST TWOS AND ONE
    if (m[0]-80,m[1]-80) not in p and (m[0]-40,m[1]-40) in play2 and (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2 and (m[0]+120,m[1]+120) not in p:
        return 6
    if (m[0]-120,m[1]-120) not in p and (m[0]-80,m[1]-80) in play2  and (m[0]-40,m[1]-40) in play2 and (m[0]+40,m[1]+40) in play2  and (m[0]+80,m[1]+80) not in p:
        return 6
    #SOUTHWEST TWOS AND ONE
    if (m[0]-80,m[1]+80) not in p and (m[0]-40,m[1]+40) in play2 and (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2 and (m[0]+120,m[1]-120) not in p:
        return 6
    if (m[0]-120,m[1]+120) not in p and (m[0]-80,m[1]+80) in play2 and (m[0]-40,m[1]+40) in play2 and (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) not in p:
        return 6
    #VERTICAL TWOS AND ONE
    if (m[0],m[1]-80) not in p and (m[0],m[1]-40) in play2 and (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2 and (m[0],m[1]+120) not in p:
        return 6
    if (m[0],m[1]-120) not in p and (m[0],m[1]-80) in play2 and (m[0],m[1]-40) in play2 and (m[0],m[1]+40) in play2 and (m[0],m[1]+80) not in p:
        return 6

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if temp == 5:
        return 5

    if temp == 0:
        return 4
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    #SEARCH FOR BROKEN THREES
    #HORIZONTAL TWOS AND ONE
    if (m[0]+40,m[1]) in p and (m[0]+80, m[1]) not in play2 and (m[0]+120,m[1]) in p:
        if (m[0]-40,m[1]) not in play2 or (m[0]+160,m[1]) not in play2:
            return 3         
    #SOUTHEAST TWOS AND ONE
    if (m[0]+40,m[1]+40) in p and (m[0]+80, m[1]+80) not in play2 and (m[0]+120,m[1]+120) in p:
        if (m[0]-40,m[1]-40) not in play2 or (m[0]+160,m[1]+160) not in play2:
            return 3                     
    #SOUTHWEST TWOS AND ONE
    if (m[0]+40,m[1]-40) in p and (m[0]+80, m[1]-80) not in play2 and (m[0]+120,m[1]-120) in p:
        if (m[0]-40,m[1]+40) not in play2 or (m[0]+160,m[1]-160) not in play2:
            return 3                     
    #VERTICAL TWOS AND ONE
    if (m[0],m[1]+40) in p and (m[0], m[1]+80) not in play2 and (m[0],m[1]+120) in p:
        if (m[0],m[1]-40) not in play2 or (m[0],m[1]+160) not in play2:
            return 3                    
    

    #SEARCHING FOR TWOS
    if ((m[0]-40,m[1]) in p or (m[0]+40, m[1])in p) and (m[0]-80,m[1]) not in play2 and (m[0]-40,m[1]) not in play2 and (m[0]+40, m[1]) not in play2 and (m[0]+80,m[1]) not in play2:
        return 2
    if ((m[0]-40,m[1]-40) in p or (m[0]+40, m[1]+40)in p) and (m[0]-80,m[1]-80) not in play2 and (m[0]-40,m[1]-40) not in play2 and (m[0]+40, m[1]+40) not in play2 and (m[0]+80,m[1]+80) not in play2:
        return 2
    if ((m[0]-40,m[1]+40) in p or (m[0]+40, m[1]-40)in p) and (m[0]-80,m[1]+80) not in play2 and (m[0]-40,m[1]+40) not in play2 and (m[0]+40, m[1]-40) not in play2 and (m[0]+80,m[1]-80) not in play2:
        return 2
    if ((m[0],m[1]-40) in p or (m[0], m[1]+40)in p) and (m[0],m[1]-80) not in play2 and (m[0],m[1]-40) not in play2 and (m[0], m[1]+40) not in play2 and (m[0],m[1]+80) not in play2:
        return 2
    if (m[0]-40,m[1]) in p and (m[0]+40,m[1]) not in play2 and (m[0]+80,m[1]) not in play2 and (m[0]+120,m[1]) not in play2:
        return 2
    if (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) not in play2 and (m[0]+80,m[1]+80) not in play2 and (m[0]+120,m[1]+120) not in play2:
        return 2    
    if (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) not in play2 and (m[0]+80,m[1]-80) not in play2 and (m[0]+120,m[1]-120) not in play2:
        return 2
    if (m[0],m[1]-40) in p and (m[0],m[1]+40) not in play2 and (m[0],m[1]+80) not in play2 and (m[0],m[1]+120) not in play2:
        return 2
    if (m[0]+40,m[1]) in p and (m[0]+80,m[1]) not in play2 and (m[0]+120,m[1]) not in play2 and (m[0]+160,m[1]) not in play2:
        return 2
    if (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) not in play2 and (m[0]+120,m[1]+120) not in play2 and (m[0]+160,m[1]+160) not in play2:
        return 2
    if (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) not in play2 and (m[0]+120,m[1]-120) not in play2 and (m[0]+160,m[1]-160) not in play2:
        return 2
    if (m[0],m[1]+40) in p and (m[0],m[1]+80) not in play2 and (m[0],m[1]+120) not in play2 and (m[0],m[1]+160) not in play2:
        return 2
    if (m[0]-40,m[1]) not in play2 and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) not in play2 and (m[0]+120,m[1]) not in play2:
        return 2
    if (m[0]-40,m[1]-40) not in play2 and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) not in play2 and (m[0]+120,m[1]+120) not in play2:
        return 2
    if (m[0]-40,m[1]+40) not in play2 and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) not in play2 and (m[0]+120,m[1]-120) not in play2:
        return 2
    if (m[0],m[1]-40) not in play2 and (m[0],m[1]+40) in p and (m[0],m[1]+80) not in play2 and (m[0],m[1]+120) not in play2:
        return 2
    if (m[0]-40,m[1]) in p and (m[0]-80,m[1]) not in play2 and (m[0]-120,m[1]) not in play2 and (m[0]+40,m[1]) not in play2:
        return 2
    if (m[0]-40,m[1]-40) in p and (m[0]-80,m[1]-80) not in play2 and (m[0]-120,m[1]-120) not in play2 and (m[0]+40,m[1]+40) not in play2:
        return 2
    if (m[0]-40,m[1]+40) in p and (m[0]-80,m[1]+80) not in play2 and (m[0]-120,m[1]+120) not in play2 and (m[0]+40,m[1]+40) not in play2:
        return 2
    if (m[0],m[1]-40) in p and (m[0],m[1]-80) not in play2 and (m[0],m[1]-120) not in play2 and (m[0],m[1]+40) not in play2:
        return 2
    if (m[0]-40,m[1]) in p and (m[0]-80,m[1]) not in play2 and (m[0]-120,m[1]) not in play2 and (m[0]-160,m[1]) not in play2:
        return 2
    if (m[0]-40,m[1]-40) in p and (m[0]-80,m[1]-80) not in play2 and (m[0]-120,m[1]-120) not in play2 and (m[0]-160,m[1]-160) not in play2:
        return 2
    if (m[0]-40,m[1]+40) in p and (m[0]-80,m[1]+80) not in play2 and (m[0]-120,m[1]+120) not in play2 and (m[0]-160,m[1]+160) not in play2:
        return 2
    if (m[0],m[1]-40) in p and (m[0],m[1]-80) not in play2 and (m[0],m[1]-120) not in play2 and (m[0],m[1]-160) not in play2:
        return 2
    if (m[0]-40,m[1]) not in play2 and (m[0]-80,m[1]) not in play2 and (m[0]-120,m[1]) not in play2 and (m[0]+40,m[1]) in p:
        return 2
    if (m[0]-40,m[1]-40) not in play2 and (m[0]-80,m[1]-80) not in play2 and (m[0]-120,m[1]-120) not in play2 and (m[0]+40,m[1]+40) in p:
        return 2
    if (m[0]-40,m[1]+40) not in play2 and (m[0]-80,m[1]+80) not in play2 and (m[0]-120,m[1]+120) not in play2 and (m[0]+40,m[1]-40) in p:
        return 2
    if (m[0],m[1]-40) not in play2 and (m[0],m[1]-80) not in play2 and (m[0],m[1]-120) not in play2 and (m[0],m[1]+40) in p:
        return 2
    

    

    return 0

    
def attack(player, otherplayer, depth, maxdepth, A, B):
    a = []
    b = []
    if isgameover(player) or depth == maxdepth:
        e = evaluate(player, otherplayer)
        return e
    bestmove = None
    bestscore = -1000
    move = getmoves(player, otherplayer)
    for m in move:
        a = player+[(m)]
        b = otherplayer+[]
        score = attack(b, a, depth+1, maxdepth, -B, -max(A, bestscore))            
        score = -score
        if score > bestscore:
            bestscore = score
            bestmove = m
            if bestscore >= B:
                return bestscore
    if depth == 0:
        player.append((bestmove))
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
    s1 = 0
    des = []
    for m in moves:
        if m[0] > 0 and m[0] < 600 and m[1] > 0 and m[1] < 600:
            p = []
            p = play1+[m]
            s2 = evaluate(p, play2)
            if s2 > s1:
                s1 = s2
                des = []
                if m not in des:
                    des.append((m))
            if s2 == s1:
                if m not in des:
                    des.append((m))
    return des


def evaluate(play1, play):
    p = []
    p = play1 + []
    play2 = play + []
    p.remove(p[len(p)-1])
    m = play1[len(play1)-1]
    #SEARCHING FOR FIVES
    #HORIZONTAL 
    if (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) in p and (m[0]+160,m[1]) in p:
        return 10
    if (m[0]-40,m[1]) in p and (m[0]-80,m[1]) in p and (m[0]-120,m[1]) in p and (m[0]-160,m[1]) in p:
        return 10
    #VERTICAL 
    if (m[0],m[1]+40) in p and (m[0],m[1]+80) in p and (m[0],m[1]+120) in p and (m[0],m[1]+160) in p:
        return 10
    if (m[0],m[1]-40) in p and (m[0],m[1]-80) in p and (m[0],m[1]-120) in p and (m[0],m[1]-160) in p:
        return 10
    #SOUTHEAST 
    if (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) in p and (m[0]+160,m[1]+160) in p:
        return 10
    if (m[0]-40,m[1]-40) in p and (m[0]-80,m[1]-80) in p and (m[0]-120,m[1]-120) in p and (m[0]-160,m[1]-160) in p:
        return 10
    #SOUTHWEST 
    if (m[0]-40,m[1]+40) in p and (m[0]-80,m[1]+80) in p and (m[0]-120,m[1]+120) in p and (m[0]-160,m[1]+160) in p:
        return 10
    if (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) in p and (m[0]+160,m[1]-160) in p:
        return 10
    #HORIZONTAL
    if (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) in p:
        return 10
    if (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p:
        return 10
    if (m[0]-120,m[1]) in p and (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p:
        return 10
    #SOUTHEAST
    if (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) in p:
        return 10
    if (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p:
        return 10
    if (m[0]-120,m[1]-120) in p and (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p:
        return 10
    #SOUTHWEST
    if (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) in p:
        return 10
    if (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p:
        return 10
    if (m[0]-120,m[1]+120) in p and (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p:
        return 10
    #VERTICAL
    if (m[0],m[1]-40) in p and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p and (m[0],m[1]+120) in p:
        return 10
    if (m[0],m[1]-80) in p and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p:
        return 10
    if (m[0],m[1]-120) in p and (m[0],m[1]-80) in p and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p:
        return 10

    #SEARCHING FOR MOVES THAT BLOCK OPPONENT'S FOURS WHICH HAVE UNBLOCKED ADJACENT NODES.IT WILL RETURN 9.
    #HORIZONTAL FOURS
    if (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2 and (m[0]+120,m[1]) in play2 and (m[0]+160,m[1]) in play2:
        return 9
    if (m[0]-40,m[1]) in play2 and (m[0]-80,m[1]) in play2 and (m[0]-120,m[1]) in play2 and (m[0]-160,m[1]) in play2:
        return 9
    #VERTICAL FOURS
    if (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2 and (m[0],m[1]+120) in play2 and (m[0],m[1]+160) in play2:
        return 9
    if (m[0],m[1]-40) in play2 and (m[0],m[1]-80) in play2 and (m[0],m[1]-120) in play2 and (m[0],m[1]-160) in play2:
        return 9
    #SOUTHEAST FOURS
    if (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2 and (m[0]+120,m[1]+120) in play2 and (m[0]+160,m[1]+160) in play2:
        return 9
    if (m[0]-40,m[1]-40) in play2 and (m[0]-80,m[1]-80) in play2 and (m[0]-120,m[1]-120) in play2 and (m[0]-160,m[1]-160) in play2:
        return 9
    #SOUTHWEST FOURS
    if (m[0]-40,m[1]+40) in play2 and (m[0]-80,m[1]+80) in play2 and (m[0]-120,m[1]+120) in play2 and (m[0]-160,m[1]+160) in play2:
        return 9
    if (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2 and (m[0]+120,m[1]-120) in play2 and (m[0]+160,m[1]-160) in play2:
        return 9
    #HORIZONTAL BROKEN FOURS
    if (m[0]-40,m[1]) in play2 and (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2 and (m[0]+120,m[1]) in play2:
        return 9
    if (m[0]-80,m[1]) in play2 and (m[0]-40,m[1]) in play2 and (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2:
        return 9
    if (m[0]-120,m[1]) in play2 and (m[0]-80,m[1]) in play2 and (m[0]-40,m[1]) in play2 and (m[0]+40,m[1]) in play2:
        return 9
    #SOUTHEAST BROKEN FOURS
    if (m[0]-40,m[1]-40) in play2 and (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2 and (m[0]+120,m[1]+120) in play2:
        return 9
    if (m[0]-80,m[1]-80) in play2 and (m[0]-40,m[1]-40) in play2 and (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2:
        return 9
    if (m[0]-120,m[1]-120) in play2 and (m[0]-80,m[1]-80) in play2 and (m[0]-40,m[1]-40) in play2 and (m[0]+40,m[1]+40) in play2:
        return 9
    #SOUTHWEST BROKEN FOURS
    if (m[0]-40,m[1]+40) in play2 and (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2 and (m[0]+120,m[1]-120) in play2:
        return 9
    if (m[0]-80,m[1]+80) in play2 and (m[0]-40,m[1]+40) in play2 and (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2:
        return 9
    if (m[0]-120,m[1]+120) in play2 and (m[0]-80,m[1]+80) in play2 and (m[0]-40,m[1]+40) in play2 and (m[0]+40,m[1]-40) in play2:
        return 9
    #VERTICAL BROKEN FOURS
    if (m[0],m[1]-40) in play2 and (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2 and (m[0],m[1]+120) in play2:
        return 9
    if (m[0],m[1]-80) in play2 and (m[0],m[1]-40) in play2 and (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2:
        return 9
    if (m[0],m[1]-120) in play2 and (m[0],m[1]-80) in play2 and (m[0],m[1]-40) in play2 and (m[0],m[1]+40) in play2:
        return 9
          
    #SEARCHING FOR FOURS (BOTH SIDES UNBLOCKED) 
    #HORIZONTAL FOURS
    if (m[0]-40,m[1]) not in play2 and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) in p and (m[0]+160,m[1]) not in play2:
        return 8
    if (m[0]-80,m[1]) not in play2 and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) not in play2:
        return 8
    if (m[0]-120,m[1]) not in play2 and (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) not in play2:
        return 8
    if (m[0]-160,m[1]) not in play2 and (m[0]-120,m[1]) in p and (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) not in play2:
        return 8
    #SOUTHEAST FOURS
    if (m[0]-40,m[1]-40) not in play2 and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) in p and (m[0]+160,m[1]+160) not in play2:
        return 8
    if (m[0]-80,m[1]-80) not in play2 and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) not in play2:
        return 8
    if (m[0]-120,m[1]-120) not in play2 and (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) not in play2:
        return 8
    if (m[0]-160,m[1]-160) not in play2 and (m[0]-120,m[1]-120) in p and (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) not in play2:
        return 8
    #SOUTHWEST FOURS
    if (m[0]-40,m[1]+40) not in play2 and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) in p and (m[0]+160,m[1]-160) not in play2:
        return 8
    if (m[0]-80,m[1]+80) not in play2 and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) not in play2:
        return 8
    if (m[0]-120,m[1]+120) not in play2 and (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) not in play2:
        return 8
    if (m[0]-160,m[1]+160) not in play2 and (m[0]-120,m[1]+120) in p and (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) not in play2:
        return 8
    #VERTICAL FOURS
    if (m[0],m[1]-40) not in play2 and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p and (m[0],m[1]+120) in p and (m[0],m[1]+160) not in play2:
        return 8
    if (m[0],m[1]-80) not in play2 and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p and (m[0],m[1]+120) not in play2:
        return 8
    if (m[0],m[1]-120) not in play2 and (m[0],m[1]-80) in p and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p and (m[0],m[1]+80) not in play2:
        return 8
    if (m[0],m[1]-160) not in play2 and (m[0],m[1]-120) in p and (m[0],m[1]-80) in p and (m[0],m[1]-40) in p and (m[0],m[1]+40) not in play2:
        return 8
    
    pin = 0
    #SEARCHING FOR FOURS (ONE SIDE UNBLOCKED) 
    #HORIZONTAL FOURS
    if ((m[0]-40,m[1]) not in play2 or (m[0]+160,m[1]) not in play2) and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) in p:
        pin = 7
    if ((m[0]-80,m[1]) not in play2 or (m[0]+120,m[1]) not in play2) and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) in p :
        pin = 7
    if ((m[0]-120,m[1]) not in play2 or (m[0]+80,m[1]) not in play2) and (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p and (m[0]+40,m[1]) in p:
        pin = 7
    if ((m[0]-160,m[1]) not in play2 or (m[0]+40,m[1]) not in play2) and (m[0]-120,m[1]) in p and (m[0]-80,m[1]) in p and (m[0]-40,m[1]) in p:
        pin = 7
    #SOUTHEAST FOURS
    if ((m[0]-40,m[1]-40) not in play2 or (m[0]+160,m[1]+160) not in play2) and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) in p:
        pin = 7
    if ((m[0]-80,m[1]-80) not in play2 or (m[0]+120,m[1]+120) not in play2) and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) in p :
        pin = 7
    if ((m[0]-120,m[1]-120) not in play2 or (m[0]+80,m[1]+80) not in play2) and (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) in p:
        pin = 7
    if ((m[0]-160,m[1]-160) not in play2 or (m[0]+40,m[1]+40) not in play2) and (m[0]-120,m[1]-120) in p and (m[0]-80,m[1]-80) in p and (m[0]-40,m[1]-40) in p:
        pin = 7
    #SOUTHWEST FOURS
    if ((m[0]-40,m[1]+40) not in play2 or (m[0]+160,m[1]-160) not in play2) and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) in p:
        pin = 7
    if ((m[0]-80,m[1]+80) not in play2 or (m[0]+120,m[1]-120) not in play2) and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) in p :
        pin = 7
    if ((m[0]-120,m[1]+120) not in play2 or (m[0]+80,m[1]-80) not in play2) and (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) in p:
        pin = 7
    if ((m[0]-160,m[1]+160) not in play2 or (m[0]+40,m[1]-40) not in play2) and (m[0]-120,m[1]+120) in p and (m[0]-80,m[1]+80) in p and (m[0]-40,m[1]+40) in p:
        pin = 7
    #VERTICAL FOURS
    if ((m[0],m[1]-40) not in play2 or (m[0],m[1]+160) not in play2) and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p and (m[0],m[1]+120) in p:
        pin = 7
    if ((m[0],m[1]-80) not in play2 or (m[0],m[1]+120) not in play2) and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p and (m[0],m[1]+80) in p :
        pin = 7
    if ((m[0],m[1]-120) not in play2 or (m[0],m[1]+80) not in play2) and (m[0],m[1]-80) in p and (m[0],m[1]-40) in p and (m[0],m[1]+40) in p:
        pin = 7
    if ((m[0],m[1]-160) not in play2 or (m[0],m[1]+40) not in play2) and (m[0],m[1]-120) in p and (m[0],m[1]-80) in p and (m[0],m[1]-40) in p:
        pin = 7
    #HORIZONTAL THREES AND ONE
    if (m[0]+40,m[1]) not in play2 and (m[0]+80,m[1]) in p and (m[0]+120,m[1]) in p and (m[0]+160,m[1]) in p:
        pin = 7
    if (m[0]-40,m[1]) not in play2 and (m[0]-80,m[1]) in p and (m[0]-120,m[1]) in p and (m[0]-160,m[1]) in p:
        pin = 7
    #SOUTHEAST THREES AND ONE
    if (m[0]+40,m[1]+40) not in play2 and (m[0]+80,m[1]+80) in p and (m[0]+120,m[1]+120) in p and (m[0]+160,m[1]+160) in p:
        pin = 7
    if (m[0]-40,m[1]-40) not in play2 and (m[0]-80,m[1]-80) in p and (m[0]-120,m[1]-120) in p and (m[0]-160,m[1]-160) in p:
        pin = 7
    #SOUTHWEST THREES AND ONE
    if (m[0]+40,m[1]-40) not in play2 and (m[0]+80,m[1]-80) in p and (m[0]+120,m[1]-120) in p and (m[0]+160,m[1]-160) in p:
        pin = 7
    if (m[0]-40,m[1]+40) not in play2 and (m[0]-80,m[1]+80) in p and (m[0]-120,m[1]+120) in p and (m[0]-160,m[1]+160) in p:
        pin = 7
    #VERTICAL THREES AND ONE 
    if (m[0],m[1]+40) not in play2 and (m[0],m[1]+80) in p and (m[0],m[1]+120) in p and (m[0],m[1]+160) in p:
        pin = 7
    if (m[0],m[1]-40) not in play2 and (m[0],m[1]-80) in p and (m[0],m[1]-120) in p and (m[0],m[1]-160) in p:
        pin = 7
    temp = 1   
    #SEARCH FOR THREES (THREE UNBLOCKED ADJACENT NODES)&(TWO UBLOCKED ADJACENT NODES)
    #HORIZONTAL THREES
    if (m[0]-40,m[1]) not in play2 and (m[0]+40, m[1]) in p and (m[0]+80, m[1]) in p and (m[0]+120,m[1]) not in play2:
        if (m[0]-80,m[1]) not in play2 and (m[0]+160,m[1]) not in play2:
            temp = 5
        elif (m[0]-80,m[1]) not in play2 or (m[0]+160,m[1]) not in play2:
            temp = 0
        else:
            temp = 2
    #SOUTHEAST THREES
    if (m[0]-40,m[1]-40) not in play2 and (m[0]+40, m[1]+40) in p and (m[0]+80, m[1]+80) in p and (m[0]+120,m[1]+120) not in play2:
        if (m[0]-80,m[1]-80) not in play2 and (m[0]+160,m[1]+160) not in play2:
            temp = 5
        elif (m[0]-80,m[1]-80) not in play2 or (m[0]+160,m[1]+160) not in play2:
            temp = 0
        else:
            temp = 2
    #SOUTHWEST THREES
    if (m[0]-40,m[1]+40) not in play2 and (m[0]+40, m[1]-40) in p and (m[0]+80, m[1]-80) in p and (m[0]+120,m[1]-120) not in play2:
        if (m[0]-80,m[1]+80) not in play2 and (m[0]+160,m[1]-160) not in play2:
            temp = 5
        elif (m[0]-80,m[1]+80) not in play2 or (m[0]+160,m[1]-160) not in play2:
            temp = 0
        else:
            temp = 2
    #VERTICAL THREES
    if (m[0],m[1]-40) not in play2 and (m[0], m[1]+40) in p and (m[0], m[1]+80) in p and (m[0],m[1]+120) not in play2:
        if (m[0],m[1]-80) not in play2 and (m[0],m[1]+160) not in play2:
            temp = 5
        elif (m[0],m[1]-80) not in play2 or (m[0],m[1]+160) not in play2:
            temp = 0
        else:
            temp = 2
    if pin == 7:
        if temp == 5:
            return 7.5
        else:
            return 7


    #SEARCHING FOR MOVES THAT BLOCK OPPONENT'S THREES WITH THREE ADJACENT EMPTY NODES. IT WILL RETURN 6
    #HORIZONTAL THREES
    if (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2 and (m[0]+120,m[1]) in play2 and (m[0]+160,m[1]) not in p and (m[0]+200,m[1]) not in p:
        return 6
    if (m[0]-40,m[1]) in play2 and (m[0]-80,m[1]) in play2 and (m[0]-120,m[1]) in play2 and (m[0]-160,m[1]) not in p and (m[0]-200,m[1]) not in p:
        return 6
    if (m[0]-40,m[1]) not in p and (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2 and (m[0]+120,m[1]) in play2 and (m[0]+160,m[1]) not in p:
        return 6
    if (m[0]+40,m[1]) not in p and (m[0]-40,m[1]) in play2 and (m[0]-80,m[1]) in play2 and (m[0]-120,m[1]) in play2 and (m[0]-160,m[1]) not in p:
        return 6    
    #SOUTHEAST THREES
    if (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2 and (m[0]+120,m[1]+120) in play2 and (m[0]+160,m[1]+160) not in p and (m[0]+200,m[1]+200) not in p:
        return 6
    if (m[0]-40,m[1]-40) in play2 and (m[0]-80,m[1]-80) in play2 and (m[0]-120,m[1]-120) in play2 and (m[0]-160,m[1]-160) not in p and (m[0]-200,m[1]-200) not in p:
        return 6
    if (m[0]-40,m[1]-40) not in p and (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2 and (m[0]+120,m[1]+120) in play2 and (m[0]+160,m[1]+160) not in p:
        return 6
    if (m[0]+40,m[1]+40) not in p and (m[0]-40,m[1]-40) in play2 and (m[0]-80,m[1]-80) in play2 and (m[0]-120,m[1]-120) in play2 and (m[0]-160,m[1]-160) not in p:
        return 6    
    #SOUTHWEST THREES
    if (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2 and (m[0]+120,m[1]-120) in play2 and (m[0]+160,m[1]-160) not in p and (m[0]+200,m[1]-200) not in p:
        return 6
    if (m[0]-40,m[1]+40) in play2 and (m[0]-80,m[1]+80) in play2  and (m[0]-120,m[1]+120) in play2 and (m[0]-160,m[1]+160) not in p and (m[0]-200,m[1]+200) not in p:
        return 6
    if (m[0]-40,m[1]+40) not in p and (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2 and (m[0]+120,m[1]-120) in play2 and (m[0]+160,m[1]-160) not in p:
        return 6
    if (m[0]+40,m[1]-40) not in p and (m[0]-40,m[1]+40) in play2 and (m[0]-80,m[1]+80) in play2 and (m[0]-120,m[1]+120) in play2 and (m[0]-160,m[1]+160) not in p:
        return 6    
    #VERTICAL THREES
    if (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2 and (m[0],m[1]+120) in play2 and (m[0],m[1]+160) not in p and (m[0],m[1]+200) not in p:
        return 6
    if (m[0],m[1]-40) in play2 and (m[0],m[1]-80) in play2 and (m[0],m[1]-120) in play2 and (m[0],m[1]-160) not in p and (m[0],m[1]-200) not in p:
        return 6
    if (m[0],m[1]-40) not in p and (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2 and (m[0],m[1]+120) in play2 and (m[0],m[1]+160) not in p:
        return 6
    if (m[0],m[1]+40) not in p and (m[0],m[1]-40) in play2 and (m[0],m[1]-80) in play2 and (m[0],m[1]-120) in play2 and (m[0],m[1]-160) not in p:
        return 6    

    #BLOCKING OPPONENT'S BROKEN THREES
    #HORIZONTAL TWOS AND ONE
    if (m[0]-80,m[1]) not in p and (m[0]-40,m[1]) in play2 and (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) in play2 and (m[0]+120,m[1]) not in p:
        return 6
    if (m[0]-120,m[1]) not in p and (m[0]-80,m[1]) in play2 and (m[0]-40,m[1]) in play2 and (m[0]+40,m[1]) in play2 and (m[0]+80,m[1]) not in p:
        return 6
    #SOUTHEAST TWOS AND ONE
    if (m[0]-80,m[1]-80) not in p and (m[0]-40,m[1]-40) in play2 and (m[0]+40,m[1]+40) in play2 and (m[0]+80,m[1]+80) in play2 and (m[0]+120,m[1]+120) not in p:
        return 6
    if (m[0]-120,m[1]-120) not in p and (m[0]-80,m[1]-80) in play2  and (m[0]-40,m[1]-40) in play2 and (m[0]+40,m[1]+40) in play2  and (m[0]+80,m[1]+80) not in p:
        return 6
    #SOUTHWEST TWOS AND ONE
    if (m[0]-80,m[1]+80) not in p and (m[0]-40,m[1]+40) in play2 and (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) in play2 and (m[0]+120,m[1]-120) not in p:
        return 6
    if (m[0]-120,m[1]+120) not in p and (m[0]-80,m[1]+80) in play2 and (m[0]-40,m[1]+40) in play2 and (m[0]+40,m[1]-40) in play2 and (m[0]+80,m[1]-80) not in p:
        return 6
    #VERTICAL TWOS AND ONE
    if (m[0],m[1]-80) not in p and (m[0],m[1]-40) in play2 and (m[0],m[1]+40) in play2 and (m[0],m[1]+80) in play2 and (m[0],m[1]+120) not in p:
        return 6
    if (m[0],m[1]-120) not in p and (m[0],m[1]-80) in play2 and (m[0],m[1]-40) in play2 and (m[0],m[1]+40) in play2 and (m[0],m[1]+80) not in p:
        return 6

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if temp == 5:
        return 5

    if temp == 0:
        return 4
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    #SEARCH FOR BROKEN THREES
    #HORIZONTAL TWOS AND ONE
    if (m[0]+40,m[1]) in p and (m[0]+80, m[1]) not in play2 and (m[0]+120,m[1]) in p:
        if (m[0]-40,m[1]) not in play2 or (m[0]+160,m[1]) not in play2:
            return 3         
    #SOUTHEAST TWOS AND ONE
    if (m[0]+40,m[1]+40) in p and (m[0]+80, m[1]+80) not in play2 and (m[0]+120,m[1]+120) in p:
        if (m[0]-40,m[1]-40) not in play2 or (m[0]+160,m[1]+160) not in play2:
            return 3                     
    #SOUTHWEST TWOS AND ONE
    if (m[0]+40,m[1]-40) in p and (m[0]+80, m[1]-80) not in play2 and (m[0]+120,m[1]-120) in p:
        if (m[0]-40,m[1]+40) not in play2 or (m[0]+160,m[1]-160) not in play2:
            return 3                     
    #VERTICAL TWOS AND ONE
    if (m[0],m[1]+40) in p and (m[0], m[1]+80) not in play2 and (m[0],m[1]+120) in p:
        if (m[0],m[1]-40) not in play2 or (m[0],m[1]+160) not in play2:
            return 3                    
    

    #SEARCHING FOR TWOS
    if ((m[0]-40,m[1]) in p or (m[0]+40, m[1])in p) and (m[0]-80,m[1]) not in play2 and (m[0]-40,m[1]) not in play2 and (m[0]+40, m[1]) not in play2 and (m[0]+80,m[1]) not in play2:
        return 2
    if ((m[0]-40,m[1]-40) in p or (m[0]+40, m[1]+40)in p) and (m[0]-80,m[1]-80) not in play2 and (m[0]-40,m[1]-40) not in play2 and (m[0]+40, m[1]+40) not in play2 and (m[0]+80,m[1]+80) not in play2:
        return 2
    if ((m[0]-40,m[1]+40) in p or (m[0]+40, m[1]-40)in p) and (m[0]-80,m[1]+80) not in play2 and (m[0]-40,m[1]+40) not in play2 and (m[0]+40, m[1]-40) not in play2 and (m[0]+80,m[1]-80) not in play2:
        return 2
    if ((m[0],m[1]-40) in p or (m[0], m[1]+40)in p) and (m[0],m[1]-80) not in play2 and (m[0],m[1]-40) not in play2 and (m[0], m[1]+40) not in play2 and (m[0],m[1]+80) not in play2:
        return 2
    if (m[0]-40,m[1]) in p and (m[0]+40,m[1]) not in play2 and (m[0]+80,m[1]) not in play2 and (m[0]+120,m[1]) not in play2:
        return 2
    if (m[0]-40,m[1]-40) in p and (m[0]+40,m[1]+40) not in play2 and (m[0]+80,m[1]+80) not in play2 and (m[0]+120,m[1]+120) not in play2:
        return 2    
    if (m[0]-40,m[1]+40) in p and (m[0]+40,m[1]-40) not in play2 and (m[0]+80,m[1]-80) not in play2 and (m[0]+120,m[1]-120) not in play2:
        return 2
    if (m[0],m[1]-40) in p and (m[0],m[1]+40) not in play2 and (m[0],m[1]+80) not in play2 and (m[0],m[1]+120) not in play2:
        return 2
    if (m[0]+40,m[1]) in p and (m[0]+80,m[1]) not in play2 and (m[0]+120,m[1]) not in play2 and (m[0]+160,m[1]) not in play2:
        return 2
    if (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) not in play2 and (m[0]+120,m[1]+120) not in play2 and (m[0]+160,m[1]+160) not in play2:
        return 2
    if (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) not in play2 and (m[0]+120,m[1]-120) not in play2 and (m[0]+160,m[1]-160) not in play2:
        return 2
    if (m[0],m[1]+40) in p and (m[0],m[1]+80) not in play2 and (m[0],m[1]+120) not in play2 and (m[0],m[1]+160) not in play2:
        return 2
    if (m[0]-40,m[1]) not in play2 and (m[0]+40,m[1]) in p and (m[0]+80,m[1]) not in play2 and (m[0]+120,m[1]) not in play2:
        return 2
    if (m[0]-40,m[1]-40) not in play2 and (m[0]+40,m[1]+40) in p and (m[0]+80,m[1]+80) not in play2 and (m[0]+120,m[1]+120) not in play2:
        return 2
    if (m[0]-40,m[1]+40) not in play2 and (m[0]+40,m[1]-40) in p and (m[0]+80,m[1]-80) not in play2 and (m[0]+120,m[1]-120) not in play2:
        return 2
    if (m[0],m[1]-40) not in play2 and (m[0],m[1]+40) in p and (m[0],m[1]+80) not in play2 and (m[0],m[1]+120) not in play2:
        return 2
    if (m[0]-40,m[1]) in p and (m[0]-80,m[1]) not in play2 and (m[0]-120,m[1]) not in play2 and (m[0]+40,m[1]) not in play2:
        return 2
    if (m[0]-40,m[1]-40) in p and (m[0]-80,m[1]-80) not in play2 and (m[0]-120,m[1]-120) not in play2 and (m[0]+40,m[1]+40) not in play2:
        return 2
    if (m[0]-40,m[1]+40) in p and (m[0]-80,m[1]+80) not in play2 and (m[0]-120,m[1]+120) not in play2 and (m[0]+40,m[1]+40) not in play2:
        return 2
    if (m[0],m[1]-40) in p and (m[0],m[1]-80) not in play2 and (m[0],m[1]-120) not in play2 and (m[0],m[1]+40) not in play2:
        return 2
    if (m[0]-40,m[1]) in p and (m[0]-80,m[1]) not in play2 and (m[0]-120,m[1]) not in play2 and (m[0]-160,m[1]) not in play2:
        return 2
    if (m[0]-40,m[1]-40) in p and (m[0]-80,m[1]-80) not in play2 and (m[0]-120,m[1]-120) not in play2 and (m[0]-160,m[1]-160) not in play2:
        return 2
    if (m[0]-40,m[1]+40) in p and (m[0]-80,m[1]+80) not in play2 and (m[0]-120,m[1]+120) not in play2 and (m[0]-160,m[1]+160) not in play2:
        return 2
    if (m[0],m[1]-40) in p and (m[0],m[1]-80) not in play2 and (m[0],m[1]-120) not in play2 and (m[0],m[1]-160) not in play2:
        return 2
    if (m[0]-40,m[1]) not in play2 and (m[0]-80,m[1]) not in play2 and (m[0]-120,m[1]) not in play2 and (m[0]+40,m[1]) in p:
        return 2
    if (m[0]-40,m[1]-40) not in play2 and (m[0]-80,m[1]-80) not in play2 and (m[0]-120,m[1]-120) not in play2 and (m[0]+40,m[1]+40) in p:
        return 2
    if (m[0]-40,m[1]+40) not in play2 and (m[0]-80,m[1]+80) not in play2 and (m[0]-120,m[1]+120) not in play2 and (m[0]+40,m[1]-40) in p:
        return 2
    if (m[0],m[1]-40) not in play2 and (m[0],m[1]-80) not in play2 and (m[0],m[1]-120) not in play2 and (m[0],m[1]+40) in p:
        return 2
    

    

    return 0
