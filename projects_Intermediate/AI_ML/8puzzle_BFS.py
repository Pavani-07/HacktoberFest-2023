import queue

# The initial and goal states
given = [[1,8,2],[0,4,3],[7,6,5]]
goal = [[1,2,3],[4,5,6],[7,8,0]]


class Table:
	def __init__(self, state, parent = None, action = None):
		self.state = state   # Gives the current state of the table
		self.parent = parent   # Parent node
		self.action = action    # Action that lead to this state


def givesChildren(table):
	children = []
	row, col=None, None

	for i in range(3):      # Finding the blank tile position
		for j in range(3):
			if table.state[i][j] == 0:
				row, col = i, j
				break

	moves = [(0,1),(1,0),(0,-1),(-1,0)]     # The possible moves: right,down,left,up
	for move in moves:
		row1, col1 = row+move[0], col+move[1]
		if 0<= row1 < 3 and 0<= col1 <3:
			state1 = [list(i) for i in table.state]
			state1[row][col],state1[row1][col1] = state1[row1][col1],state1[row][col]
			if move == (0,1):
				action = "right"
			elif move == (1,0):
				action = "down"
			elif move == (0,-1):
				action = "left"
			else:
				action = "up"
			children.append(Table(state1,table,action))
	return children


def sol_path(table):
	path = []
	while table:
		if table.action:
			path.insert(0,table.action)
		table = table.parent
	return path


def bfs(initial, goal):
	visited = set()
	que = queue.Queue()
	#queue = []
	#count = 0
	que.put(Table(initial))
	while not que.empty():
		cur_table = que.get()
		#print(cur_table.state)
		#count = count + 1
		visited.add(tuple(map(tuple,cur_table.state)))
		if cur_table.state == goal:
			result = sol_path(cur_table)

			return result
		children = givesChildren(cur_table)
		for child in children:
			if tuple(map(tuple,child.state)) not in visited:
				que.put(child)
				#print(child.state)
				visited.add(tuple(map(tuple,child.state)))
	return None


def inversion(initial):
	new_list = [item for sublist in initial for item in sublist]
	inv = 0
	for i in range(0,9):
		for j in range(i+1,9):
			if new_list[j]!= 0 and new_list[i]!=0 and new_list[i] > new_list[j]:
				inv += 1
	return inv


print("No. of inversions: ",inversion(given))
print("Solution Path using BFS:")
if (inversion(given) % 2 == 0):
	ans = bfs(given,goal)
	for i,j in enumerate(ans, start=1):
		print(f"State {i}: Action {j}")
else:
	print("NO SOLUTION")
