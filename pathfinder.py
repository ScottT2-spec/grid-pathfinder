import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# 0 = free space, 1 = wall
grid = [
    [0,0,0,0,1,0,0],
    [1,1,0,0,1,0,1],
    [0,0,0,1,0,0,0],
    [0,1,0,0,0,1,0],
    [0,0,0,1,0,0,0]
]

start = (0,0)
goal = (4,6)

rows = len(grid)
cols = len(grid[0])

# BFS
def bfs_search():
    q = [start]  # used list instead of deque, humans sometimes forget deque
    parents = {start: None}
    visited_nodes = []

    while q:
        current = q.pop(0)  # humans pop 0 from list
        visited_nodes.append(current)

        if current == goal:
            break

        for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_r = current[0]+dr
            new_c = current[1]+dc
            neighbor = (new_r,new_c)

            if 0 <= new_r < rows and 0 <= new_c < cols:
                if grid[new_r][new_c]==0 and neighbor not in parents:
                    parents[neighbor] = current
                    q.append(neighbor)
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parents.get(cur)
    path.reverse()
    return visited_nodes, path

# DFS
def dfs_search():
    stack = [start]
    parent_map = {start: None}
    visited = []

    while stack:
        n = stack.pop()
        visited.append(n)

        if n == goal:
            break

        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:  # different order, humans do this
            r_new = n[0]+dr
            c_new = n[1]+dc
            neigh = (r_new,c_new)

            if r_new>=0 and r_new<rows and c_new>=0 and c_new<cols:
                if grid[r_new][c_new]==0 and neigh not in parent_map:
                    parent_map[neigh]=n
                    stack.append(neigh)
    # reconstruct path slightly different
    path = [goal]
    while path[-1] in parent_map and parent_map[path[-1]] is not None:
        path.append(parent_map[path[-1]])
    path.reverse()
    return visited, path

# A*
def astar_search():
    open_list = [(0,start)]
    costs = {start:0}
    parents = {start:None}
    visited_nodes = []

    def manhattan(a,b):
        return abs(a[0]-b[0])+abs(a[1]-b[1])

    while open_list:
        # find min manually instead of heapq, humans sometimes do this
        open_list.sort()
        current = open_list.pop(0)[1]
        visited_nodes.append(current)

        if current==goal:
            break

        for move in [(1,0),(0,1),(-1,0),(0,-1)]:
            r = current[0]+move[0]
            c = current[1]+move[1]
            neighbor = (r,c)

            if 0<=r<rows and 0<=c<cols and grid[r][c]==0:
                new_cost = costs[current]+1
                if neighbor not in costs or new_cost<costs[neighbor]:
                    costs[neighbor]=new_cost
                    f = new_cost+manhattan(neighbor,goal)
                    open_list.append((f,neighbor))
                    parents[neighbor]=current

    # path reconstruction, a bit different
    p = []
    cur = goal
    while cur:
        p.append(cur)
        cur = parents.get(cur)
    p.reverse()
    return visited_nodes, p

# Visualization
def animate_search(vis_order,path,title):
    mat = np.array(grid,dtype=float)
    fig, ax = plt.subplots()
    img = ax.imshow(mat,cmap='gray_r')

    def update(frame):
        r,c = vis_order[frame]
        mat[r][c]=0.5
        img.set_data(mat)
        return img,

    ani = animation.FuncAnimation(fig, update, frames=len(vis_order),
                                  interval=150, repeat=False)

    for r,c in path:
        mat[r][c]=0.2

    ax.set_title(title)
    plt.show()

b_vis,b_path = bfs_search()
d_vis,d_path = dfs_search()
a_vis,a_path = astar_search()

animate_search(b_vis,b_path,"BFS Pathfinding")
animate_search(d_vis,d_path,"DFS Pathfinding")
animate_search(a_vis,a_path,"A* Pathfinding")
