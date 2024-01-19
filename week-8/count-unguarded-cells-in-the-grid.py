class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    	grid=[[1 for j in range(n)] for i in range(m)]
    	# 2->walls
    	# 3->guards
    	for i,j in walls:
    		grid[i][j]=2
    	for i,j in guards:
    		grid[i][j]=3

    	for i in range(m):
    		safe=[]
    		guarded=[]
    		for j in range(n):
    			if grid[i][j]==3:
    				while safe:
    					x,y=safe.pop()
    					grid[x][y]=0
    				guarded.append((i,j))
    			elif grid[i][j]==2:
    				while guarded:
    					guarded.pop()
    				while safe:
    					safe.pop()
    			elif grid[i][j]==1:
    				if guarded:
    					grid[i][j]=0
    				else:
    					safe.append((i,j))

    	for j in range(n):
    		safe=[]
    		guarded=[]
    		for i in range(m):
    			if grid[i][j]==3:
    				while safe:
    					x,y=safe.pop()
    					grid[x][y]=0
    				guarded.append((i,j))
    			elif grid[i][j]==2:
    				while guarded:
    					guarded.pop()
    				while safe:
    					safe.pop()
    			elif grid[i][j]==1:
    				if guarded:
    					grid[i][j]=0
    				else:
    					safe.append((i,j))

    	res=0
    	for i in range(m):
    		for j in range(n):
    			if grid[i][j]==1:
    				res+=1

    	return res