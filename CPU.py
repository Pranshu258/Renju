i = 0
while i < len(blacks):
	a = (blacks[i][0], blacks[i][1])
	#SEARCHING FOR FOURS 
	#WINNING MOVES
	#searching for horizontal 4 of blacks
	n = 1
	while n <= 4:
		if (a[0]+40*n, a[1]) in blacks:
			n = n + 1
		else:
			break
	if n == 4:
		if (a[0]-40,a[1]) not in whites:
			blacks.append((a[0]-40,a[1]))
			break
		elif(a[0]+40*5, a[1]) not in whites:
			blacks.append((a[0]+40*5, a[1]))
			break
	#searching for \ 4 of blacks
	n = 1
	while n <= 4:
		if (a[0]+40*n, a[1]+40*n) in blacks:
			n = n + 1
		else:
			break
	if n == 4:
		if (a[0]-40,a[1]-40) not in whites:
			blacks.append((a[0]-40,a[1]-40))
			break
		elif(a[0]+40*5, a[1]+40*5) not in whites:
			blacks.append((a[0]+40*5, a[1]+40*5))
			break
	#searching for vertical 4 of blacks 
	n = 1
	while n <= 4:
		if (a[0], a[1]+40*n) in blacks:
			n = n + 1
		else:
			break
	if n == 4:
		if (a[0],a[1]-40) not in whites:
			blacks.append((a[0],a[1]-40))
			break
		elif(a[0], a[1]+40*5) not in whites:
			blacks.append((a[0], a[1]+40*5))
			break
	#serching for / 4 of blacks
	n = 1
	while n <= 4:
		if (a[0]+40*n, a[1]-40*n) in blacks:
			n = n + 1
		else:
			break
	if n == 4:
		if (a[0]-40,a[1]+40) not in whites:
			blacks.append((a[0]-40,a[1]+40))
			break
		elif(a[0]+40*5, a[1]-40*5) not in whites:
			blacks.append((a[0]+40*5, a[1]-40*5))
			break
	#DEFENDING MOVES
	#SEARCHING FOR FOURS IN WHITE
	j = 0
	while j < len(whites):
	a = (whites[j][0], whites[j][1])
	#searching for horizontal 4 of whites 
	n = 1
	while n <= 4:
		if (a[0]+40*n, a[1]) in whites:
			n = n + 1
		else:
			break
	if n == 4:
		if (a[0]-40,a[1]) not in blacks:
			blacks.append((a[0]-40,a[1]))
			break
		elif(a[0]+40*5, a[1]) not in blacks:
			blacks.append((a[0]+40*5, a[1]))
			break
	#searching for \ 4 of whites
	n = 1
	while n <= 4:
		if (a[0]+40*n, a[1]+40*n) in whites:
			n = n + 1
		else:
			break
	if n == 4:
		if (a[0]-40,a[1]-40) not in blacks:
			blacks.append((a[0]-40,a[1]-40))
			break
		elif(a[0]+40*5, a[1]+40*5) not in blacks:
			blacks.append((a[0]+40*5, a[1]+40*5))
			break
	#searching for vertical 4 of whites
	n = 1
	while n <= 4:
		if (a[0], a[1]+40*n) in whites:
			n = n + 1
		else:
			break
	if n == 4:
		if (a[0],a[1]-40) not in blacks:
			blacks.append((a[0],a[1]-40))
			break
		elif(a[0], a[1]+40*5) not in blacks:
			blacks.append((a[0], a[1]+40*5))
			break
	#serching for / 4 of whites 
	n = 1
	while n <= 4:
		if (a[0]+40*n, a[1]-40*n) in whites:
			n = n + 1
		else:
			break
	if n == 4:
		if (a[0]-40,a[1]+40) not in blacks:
			blacks.append((a[0]-40,a[1]+40))
			break
		elif(a[0]+40*5, a[1]-40*5) not in blacks:
			blacks.append((a[0]+40*5, a[1]-40*5))
			break



        #SEARCH FOR BLACK UNBUNDED THREES AND MAKE THEM FOUR


	
	#SEARCHING FOR THREES IN WHITE
	possiblemv = []  #contains all possible defense moves
	prefer = []      #contains prefered defense moves
	k = 0
	while k < len(whites):
	a = (whites[k][0], whites[k][1])
	#searching for horizontal 3 of whites 
	n = 1
	while n <= 3:
		if (a[0]+40*n, a[1]) in whites:
			n = n + 1
		else:
			break
	if n == 3:
		unbounded = 0
		if (a[0]-40,a[1]) not in blacks:
			possiblemv.append((a[0]-40,a[1]))
			unbounded = 1
		if(a[0]+40*4, a[1]) not in blacks:
			possiblemv.append((a[0]+40*5, a[1]))
			unbounded = 2
		if unbounded == 2:
			prefer.append((a[0]-40,a[1]))
			prefer.append((a[0]+40*5, a[1]))
	#searching for \ 3 of whites
	n = 1
	while n <= 3:
		if (a[0]+40*n, a[1]+40*n) in whites:
			n = n + 1
		else:
			break
	if n == 3:
		unbounded = 0
		if (a[0]-40,a[1]-40) not in blacks:
			possiblemv.append((a[0]-40,a[1]-40))
			unbounded = 1
		if(a[0]+40*4, a[1]+40*4) not in blacks:
			possiblemv.append((a[0]+40*4, a[1]+40*4))
			unbounded = 2
		if unbounded == 2:
			prefer.append((a[0]-40,a[1]-40))
			prefer.append((a[0]+40*4, a[1]+40*4))
	#searching for vertical 3 of whites
	n = 1
	while n <= 3:
		if (a[0], a[1]+40*n) in whites:
			n = n + 1
		else:
			break
	if n == 3:
		unbounded = 0
		if (a[0],a[1]-40) not in blacks:
			possiblemv.append((a[0],a[1]-40))
			unbounded = 1
		if(a[0], a[1]+40*4) not in blacks:
			possiblemv.append((a[0], a[1]+40*5))
			unbounded = 2
		if unbounded == 2:
			prefer.append((a[0],a[1]-40))
			prefer.append((a[0], a[1]+40*5))
	#serching for / 3 of whites 
	n = 1
	while n <= 3:
		if (a[0]+40*n, a[1]-40*n) in whites:
			n = n + 1
		else:
			break
	if n == 4:
		unbounded = 0
		if (a[0]-40,a[1]+40) not in blacks:
			possiblemv.append((a[0]-40,a[1]+40))
			unbounded = 1
		if(a[0]+40*4, a[1]-40*4) not in blacks:
			possiblemv.append((a[0]+40*4, a[1]-40*4))
			unbounded = 2
		if unbounded == 2:
			prefer.append((a[0]-40,a[1]+40))
			prefer.append((a[0]+40*4, a[1]-40*4))
	#search for broken threes of whites
	
	#WE WILL APPLY THE minimaxetc. ON THE PREFERRED MOVES IF THEY ARE MORE THAN ONE.Thus narrowing the search space.
	#IF SOMEHOW ONLY ONE PREFFERED MOVE IS FOUND THEN IT WILL BE DONE.
        #IF THE PREFER ARRAY REMAINS EMPTY THEN WE WILL HAVE TO OPERATE THE minimax etc. ON THE POSSIBLEMV ARRAY (which contains all possible moves)
	#these statements apply for defending moves against threes and broken threes. 
