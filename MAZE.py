from pprint import pprint
maze = [                                    # 迷宮地圖
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1]
       ] 
direction = [                              # 使用串列設計走迷宮方向
              lambda x, y: (x-1, y),        # 往上走
              lambda x, y: (x+1, y),        # 往下走
              lambda x, y: (x, y-1),        # 往左走
              lambda x, y: (x, y+1),        # 往右走       
             ]
def maze_solve(x,y,gol_x,gol_y):
	global stack
	maze[x][y]=2
	stack=[]
	
	stack.append((x,y))
	print('start')
	while (len(stack)>0):
		cur=stack[-1]
		if cur[0]==gol_x and cur[1]==gol_y:
			print('end')
			return True
		for dir in direction :
			pprint(maze)
			next = dir(cur[0],cur[1])
			if maze[next[0]][next[1]]==0:
				stack.append(next)
				maze[next[0]][next[1]]=2
				break
		else:
			maze[cur[0]][cur[1]]=3
			stack.pop()
	else:
		print("沒有路徑")
		return False

maze_solve(1,1,4,4)
pprint(maze)
print(stack)
